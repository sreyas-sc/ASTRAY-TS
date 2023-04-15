import mysql.connector
password=""
database="text_summarization"

def select(q):
	cnx=mysql.connector.connect(password=password,database=database,host="localhost",user="root",port=3306)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cnx.close()
	cur.close()
	return result

def delete(q):
	cnx=mysql.connector.connect(password=password,database=database,host="localhost",user="root",port=3306)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
	return result

def update(q):
	cnx=mysql.connector.connect(password=password,database=database,host="localhost",user="root",port=3306)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
	return result

def insert(q):
	cnx=mysql.connector.connect(password=password,database=database,host="localhost",user="root",port=3306)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.lastrowid
	cur.close()
	cnx.close()
	return result
