from flask import Flask, render_template, request
from controller import *
from model import *

import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home_er.html")

@app.route("/adding", methods = ['POST', 'GET'])
def adding():
	if request.method == "GET":
		return render_template("login_form.html")
	if request.method == "POST":
		try:
			student = add_d()
			print student.id_num
			message = chen(student)
		except:
			message="Fail to Add student"
		finally:	
			rows = alldata()
			return render_template("result_list.html", rows = rows, message = message)
		

#For Delete

@app.route("/deleting", methods = ['POST', 'GET'])
def deleting_done():
	if request.method =="GET":
		rows = alldata()
		return render_template("delete_er.html", rows = rows)
	elif request.method == "POST":
		try:
			id_no = get_id()
			message=del_stud(id_no)

		except:
			message = "Fail to Delete"

		finally:
			
			rows = alldata()
			return render_template("result_list.html", rows = rows, message = message)
			conn.close()

#For Update


@app.route("/update", methods = ['POST', 'GET'])
def update():
	if request.method =="GET":
		rows = alldata()
		return render_template("update_er.html",rows=rows)
	if request.method == "POST":
		try:
			student = add_d()
			message = ups(student)
		except:
			message = "Failure to Update."

		finally:
			rows = alldata()
			return render_template("result_list.html", rows = rows, message = message)
		


#For List

@app.route("/list")
def rec_list():
	rows = alldata()
	return render_template("record_list.html", rows = rows)

@app.route("/CourseTable")
def course_list():
	rows=show_cur()
	return render_template("Course_table.html", rows = rows)

#For Search

@app.route("/search", methods = ['POST', 'GET'])
def search():
	return render_template("search_er.html")

@app.route("/searching", methods = ['POST', 'GET'])
def searching():
	if request.method == "POST":
		try:
			find = get_id()
			print find
			coffee = find_stud(find)
			
			msg = "existed"
		except:
			coffee = " "
			msg="not found"
		finally:
			return render_template("search_rec.html",msg=msg,coffee=coffee)


if __name__ == "__main__":
	app.run(debug = True)



