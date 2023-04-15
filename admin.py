from flask import Blueprint,render_template,request,redirect,url_for,session
from database import *
import uuid
from summerize import *
from functions import *
import pyttsx3

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')

@admin.route('/Manual_news_content_uploading',methods=['get','post'])
def Manual_news_content_uploading():
	data={}

	if 'link' in request.form:
		content1=request.form['link1']
		content2=request.form['link2']
		if content2=="":
			val=trade_spider(content1)
			print("checked",val)
			#vals = trade_spiders(content2)
		    # print("checkedval", vals)

			#valmain=val+vals

			result = run_summarization(val)
			print(result)
			data['details']=result
			session['result']=result
			
		else:
			print("sfgkj")
			val=trade_spider(content1)
			print("checked",val)
			vals = trade_spiders(content2)
		    # print("checkedval", vals)

			valmain=val+vals

			result = run_summarization(valmain)
			print(result)
			data['details']=result
			session['result']=result
	if 'submit' in request.form:
		speech(session['result'])

	return render_template('admin_manual_file_upload.html',data=data)


@admin.route('/doc_upload',methods=['get','post'])
def doc_upload():
	data={}

	data={}

	if 'upld' in request.form:
		file1=request.files['File1']
		file2=request.files['File2']
		print(file1.filename,"________________________")
		print(len(file2.filename),"********************************")
		if len(file2.filename)==0:
			print("ok")

			path1='static/files/'+str(uuid.uuid4())+str(file1.filename)
			file1.save(path1)
			
			splitpath=path1.split('.')
			types=splitpath[1]
			print(types,'.........................')
			if types=='txt':
				value=txtreader(path1)
			if types=='docx':
				value=docreader(path1)
			if types=='doc':
				value=docreader(path1)
			
			if types=='pdf':
				value=pdfreader(path1)

			result = run_summarization(value)
			print(result)
			print("/////////////////////////////////")
			# speech(result)
			data['details']=result
			session['result']=result
		else:
			path1='static/files/'+str(uuid.uuid4())+str(file1.filename)
			file1.save(path1)
			
			splitpath=path1.split('.')
			types=splitpath[1]
			print(types,'.........................')
			if types=='txt':
				value=txtreader(path1)
			if types=='docx':
				value=docreader(path1)
			
			if types=='pdf':
				value=pdfreader(path1)

			


			# upfl=trade_spider(file1)
			path2='static/files/'+str(uuid.uuid4())+str(file2.filename)
			file2.save(path2)


			splitpath2=path2.split('.')
			types1=splitpath2[1]
			print(types1)
			if types=='txt':
				value1=txtreader(path2)
			if types=='docx':
				value1=docreader(path2)
			if types=='pdf':
				value1=pdfreader(path2)

			print(value1)
			vals=value+value1
			print("........................")
			result = run_summarization(vals)
			print(result)
			print("/////////////////////////////////")
			# speech(result)
			data['details']=result
			session['result']=result
	if 'submit' in request.form:


		speech(session['result'])
		data['s']=session['result']


	return render_template('doc_upload.html',data=data)

@admin.route('/file_upload',methods=['get','post'])
def file_upload():
	data={}
	if 'news' in request.form:
		news1=request.form['news1']
		news2=request.form['news2']
		if 'news2'=="":
			valmain = news1
			result = run_summarization(valmain)
			print(result)

			data['details']=result
			session['result']=result

		else:
			valmain = news1 + news2
			result = run_summarization(valmain)
			print(result)
			
			data['details']=result
			session['result']=result

	if 'submit' in request.form:


		speech(session['result'])
		data['s']=session['result']

	return render_template('admin_file_upload.html',data=data)	

@admin.route('/admin_manage_news_providers',methods=['get','post'])
def admin_manage_news_providers():
	data={}

	if 'submit' in request.form:
		pname=request.form['pname']
		pcontact=request.form['pcontact']
		description=request.form['description']

		q="INSERT INTO `news_providers`(`provider_name`,`provider_contact`,`Description`) VALUES ('%s','%s','%s')"%(pname,pcontact,description)
		insert(q)
		return redirect(url_for('admin.admin_manage_news_providers'))

	q="SELECT * FROM `news_providers` "
	select(q)
	res=select(q)
	data['pro']=res


	if 'action' in request.args:
		action=request.args['action']
		proid=request.args['id']
	else:
		action=None

	if action=='delete':
		q="DELETE FROM `news_providers` WHERE `provider_id`='%s'"%(proid)
		delete(q)

		return redirect(url_for('admin.admin_manage_news_providers'))


		##

	if action=='update':
		q="SELECT * FROM `news_providers` WHERE `provider_id`='%s'"%(proid)
		res5=select(q)
		data['uppro']=res5
	if 'update' in request.form:
		pname=request.form['pname']
		pcontact=request.form['pcontact']
		description=request.form['description']
		q="update `news_providers` set `provider_name`='%s',`provider_contact`='%s',`description`='%s' WHERE `provider_id`='%s'"%(pname,pcontact,description,proid)
		update(q)

		return redirect(url_for('admin.admin_manage_news_providers'))


	return render_template('admin_manage_news_providers.html',data=data)

@admin.route('/admin_manage_news_categories',methods=['get','post'])
def admin_manage_news_categories():
	data={}

	if 'submit' in request.form:
		cname=request.form['cname']
		categorydescription=request.form['categorydescription']

		q="INSERT INTO`news_categories`(`category_name`,`category_description`) VALUES('%s','%s')"%(cname,categorydescription)
		insert(q)
		return redirect(url_for('admin.admin_manage_news_categories'))

	q="SELECT * FROM `news_categories`"
	select(q)
	res=select(q)
	data['category']=res


	if 'action' in request.args:
		action=request.args['action']
		catid=request.args['id']
	else:
		action=None

	if action=='delete':
		q="DELETE FROM `news_categories` WHERE `category_id`='%s'"%(catid)
		delete(q)

		return redirect(url_for('admin.admin_manage_news_categories'))
	if action=='update':
		q="SELECT * FROM `news_categories` WHERE `category_id`='%s'"%(catid)
		res1=select(q)
		data['up']=res1
	if 'update' in request.form:
		cname=request.form['cname']
		categorydescription=request.form['categorydescription']
		catid=request.args['id']
		q="UPDATE `news_categories` SET `category_name`='%s',`category_description`='%s' WHERE `category_id`='%s'"%(cname,categorydescription,catid)
		update(q)
		return redirect(url_for('admin.admin_manage_news_categories'))

	return render_template('admin_manage_news_categories.html',data=data)

@admin.route('/admin_manage_news_content',methods=['get','post'])
def admin_manage_news_content():
	data={}
	
	q="SELECT * FROM `news_categories`"
	res=select(q)
	data['cat']=res

	if 'submit' in request.form:
		cid=request.form['cname']
		title=request.form['title']
		desc=request.form['desc']

		q="INSERT INTO `news_content`(category_id,`Title`,`Date`,`Description`) VALUES('%s','%s',curdate(),'%s')"%(cid,title,desc)
		insert(q)
		return redirect(url_for('admin.admin_manage_news_content'))

	q="SELECT * FROM `news_categories` INNER JOIN `news_content` USING(`category_id`)"
	select(q)
	res2=select(q)
	data['content']=res2



	if 'action' in request.args:
		action=request.args['action']
		contid=request.args['id']
	else:
		action=None

	if action=='delete':
		q="DELETE FROM `news_content` WHERE `news_id`='%s'"%(contid)
		delete(q)

		return redirect(url_for('admin.admin_manage_news_content'))

	if action=='update':
		q="SELECT * FROM `news_content` INNER JOIN `news_categories` USING (`category_id`) WHERE `news_id`='%s'"%(contid)
		res1=select(q)
		data['upnews']=res1

	if 'update' in request.form:
		cname=request.form['cname']
		Title=request.form['title']
		descr=request.form['desc']
		q="UPDATE `news_content` SET `category_id`='%s',`Title`='%s',`Description`='%s' WHERE news_id='%s'"%(cname,Title,descr,contid)
		update(q)

		return redirect(url_for('admin.admin_manage_news_content'))

		

	return render_template('admin_manage_news_content.html',data=data)



@admin.route('/admin_view_feedbacks',methods=['get','post'])
def admin_view_feedbacks():
	data={}
	q="select *  from feedback inner join users using(user_id)"
	res=select(q)
	data['feedbacks']=res
	return render_template('admin_view_feedbacks.html',data=data)




def speech(text):
	print("sg")
	engine = pyttsx3.init() # object creation

	""" RATE"""
	rate = engine.getProperty('rate')   # getting details of current speaking rate
	print (rate)                        #printing current voice rate
	engine.setProperty('rate', 125)     # setting up new voice rate


	"""VOLUME"""
	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
	print (volume)                          #printing current volume level
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

	"""VOICE"""
	voices = engine.getProperty('voices')       #getting details of current voice
	#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
	engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

	engine.say(text)
	# engine.say('My current speaking rate is ' + str(rate))
	engine.runAndWait()
	engine.stop()