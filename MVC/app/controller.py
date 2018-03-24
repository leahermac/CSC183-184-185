import sqlite3 as sql
from model import *

conn = sql.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS stud_cour (cour_id TEXT PRIMARY KEY, cour_name TEXT, col_sch TEXT)')
cur = conn.cursor()

cur.execute("INSERT OR IGNORE INTO stud_cour(cour_id, cour_name, col_sch) VALUES ('BSCS', 'Bachelor of Science in Computer Science', 'SCS')")
cur.execute("INSERT OR IGNORE INTO stud_cour(cour_id, cour_name, col_sch) VALUES ('BSIT', 'Bachelor of Science in Information Technology', 'SCS')")
cur.execute("INSERT OR IGNORE INTO stud_cour(cour_id, cour_name, col_sch) VALUES ('BSECT', 'Bachelor of Science in Electronics and Computer Technology', 'SCS')")
cur.execute("INSERT OR IGNORE INTO stud_cour(cour_id, cour_name, col_sch) VALUES ('ECET', 'Electrical and Computer Engineering Technology', 'SCS')")

conn.execute('CREATE TABLE IF NOT EXISTS stud_record(ID TEXT PRIMARY KEY  NOT NULL CHECK(length(ID)=9), f_name TEXT  CHECK(length(f_name)>0 AND length(f_name)<=20 ), m_name TEXT CHECK (length(m_name)>0 AND length(m_name)<=20 ), l_name TEXT CHECK (length(l_name)>0 AND length(l_name)<=20 ), Sex TEXT CHECK(length(Sex)=1), Course TEXT CHECK(length(Course)>0 AND length(Course)<=20 ), yr_lvl INTEGER CHECK(length(yr_lvl)=1), FOREIGN KEY(Course) REFERENCES stud_Courses(course_id))')

print"Successfully Executed"

conn.execute("CREATE VIEW IF NOT EXISTS result AS SELECT cour_id, col_sch, l_name, f_name, m_name, cour_name, yr_lvl FROM stud_record JOIN stud_cour WHERE stud_cour.cour_id = stud_record.Course")
conn.execute("CREATE VIEW IF NOT EXISTS ALL_info AS SELECT cour_id, col_sch, cour_name, ID, f_name, m_name, l_name, Sex, yr_lvl FROM stud_record JOIN stud_cour WHERE stud_cour.cour_id = stud_record.Course")

print"Successfully Executed"	

conn.close()


def add_d():
	id_no = request.form['ID_Number']

	firstname = request.form['FirstName']
	middlename = request.form['MiddleName']
	lastname = request.form['LastName']
	sex = request.form['Sex']
	course = request.form['Course']
	Year = request.form['SchoolYear']
	student = Student(id_no, firstname, lastname, middlename, sex, course, Year)
	
	return student

def get_id():
	id_no = request.form['ID_Number']
	return id_no