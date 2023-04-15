from flask import *
from database import *
import uuid 
from summerize import *
from functions import *
import pyttsx3

user=Blueprint('user',__name__)

@user.route('/userhome')
def userhome():
	return render_template('userhome.html')

@user.route('/Manual_news_content_uploading',methods=['get','post'])
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
			# speech(result)
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
			# speech(result)
			data['details']=result
			session['result']=result
	if 'submit' in request.form:
		speech(session['result'])


	return render_template('Manual_news_content_uploading.html',data=data)


@user.route('/doc_upload',methods=['get','post'])
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


	return render_template('user_upload_file.html',data=data)

@user.route('/file_upload',methods=['get','post'])
def file_upload():
	data={}

	if 'news' in request.form:
		news1=request.form['news1']
		news2=request.form['news2']
		if 'news2'=="":
			valmain = news1
			result = run_summarization(valmain)
			print(result)
			# speech(result)
			data['details']=result
			session['result']=result
		else:
			valmain = news1 + news2
			result = run_summarization(valmain)
			print(result)
			# speech(result)
			data['details']=result
			session['result']=result
	if 'submit' in request.form:
		speech(result)

	return render_template('file_upload.html',data=data)


@user.route('/user_view_news_providers')
def user_view_news_providers():
	data={}

	q="SELECT * FROM `news_providers` "
	select(q)
	res=select(q)
	data['pro']=res
	return render_template('user_view_news_providers.html',data=data)

@user.route('/user_view_news_categories')
def user_view_news_categories():
	data={}

	q="SELECT * FROM `news_categories`"
	select(q)
	res=select(q)
	data['category']=res
	return render_template('user_view_news_categories.html',data=data)





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

# speech("hai")


@user.route('/user_send_feedback',methods=['get','post'])
def user_send_feedback():
	data={}
	if 'submit' in request.form:
		feedback=request.form['feedback']
		q="insert into feedback values(NULL,'%s','%s',now())"%(session['user_id'],feedback)
		insert(q)
		return redirect(url_for('user.user_send_feedback'))
	q="select * from feedback where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['feedback']=res


	return render_template('user_send_feedback.html',data=data)