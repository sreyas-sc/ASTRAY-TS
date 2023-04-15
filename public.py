from  flask import Blueprint,render_template,request,redirect,url_for,session
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')


@public.route('/about')
def about():
	return render_template('about.html')

@public.route('/privacy')
def privacy():
	return render_template('privacy.html')

@public.route('/registration',methods=['get','post'])
def registration():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		pno=request.form['phno']
		mail=request.form['mail']
		place=request.form['place']
		uname=request.form['uname']
		pas=request.form['passw']
		q="INSERT INTO `login`(`username`,`password`,`user_type`) VALUES ('%s','%s','user')"%(uname,pas,)
		id=insert(q)
		q1="INSERT INTO `users`(login_id,`first_name`,`last_name`,`Phone`,`Email`,`Place`) VALUES ('%s','%s','%s','%s','%s','%s')"%(id,fname,lname,pno,mail,place)
		insert(q1)
		return redirect(url_for("public.registration"))
	return render_template('registration.html')



@public.route('/login',methods=['get','post'])
def login():
	if 'login' in request.form:
		uname=request.form['uname']
		passw=request.form['passw']
		q="SELECT * FROM `login` WHERE `Username`='%s' AND `Password`='%s'"%(uname,passw)
		res=select(q)
		if res:
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['user_type']=="user":

				q="select * from users where login_id='%s'"%(res[0]['login_id'])
				res=select(q)
				session['user_id']=res[0]['user_id']
				return redirect(url_for('user.userhome'))
	return render_template('login.html')




