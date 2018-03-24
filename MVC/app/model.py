from view import *
from controller import *

class Student(object):
	def __init__(self, idnum, firstname, lastname, middlename, sex, Course, Yr):
		self.id_num = idnum
		self.fname = firstname
		self.lname = lastname
		self.mname = middlename
		self.sex = sex
		self.course = Course
		self.year = Yr


def chen(student):
	with sql.connect("database.db") as conn:
		cur = conn.cursor()
		cur.execute("INSERT INTO stud_record(ID,f_name,m_name,l_name, Sex, Course,yr_lvl) VALUES(?,?,?,?,?,?,?)",(student.id_num, student.fname, student.lname, student.mname, student.sex, student.course, student.year))
		conn.commit()
		message = "Successfully Added to the Record."
		return message


def alldata():
	conn = sql.connect("database.db")
	conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT * FROM stud_Record")
	rows = cur.fetchall()
	return rows

def del_stud(id_no):
	with sql.connect("database.db") as conn:
		cur = conn.cursor()
		cur.execute("SELECT * FROM stud_record")
		for row in cur.fetchall():
			print row
			if row[0] == id_no:
				cur.execute("DELETE FROM stud_record WHERE ID = ?", (id_no,))
				conn.commit()
				message = "Successfully Deleted"
				break
			else:
				message = "Failure to detect that student."
	return message

def ups(student):
	with sql.connect("database.db") as conn:
		cur = conn.cursor()	
		cur.execute("UPDATE stud_record set f_name = ?, l_name = ?, m_name = ?, Sex = ?, Course = ?, yr_lvl = ? where ID = ?", (student.fname, student.lname, student.mname, student.sex, student.course, student.year, student.id_num))
		conn.commit()
		message = "Successfully Updated"

			
	return message

def show_cur():
	conn = sql.connect("database.db")

	conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT * FROM result")
	rows = cur.fetchall()

	return rows

def find_stud(search):
	find = '%'+search+'%'
	conn = sql.connect("database.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM ALL_info where ID like ? or f_name like ? or m_name like ? or l_name like ? or sex=? or yr_lvl like? or cour_id like ? or cour_name like ? or col_sch like ? ", (find,find,find,find,find,find,find,find,find))

	coffee = cur.fetchall()
	return coffee