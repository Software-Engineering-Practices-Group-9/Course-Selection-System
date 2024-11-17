import sys
import time
from flask import Flask, render_template, redirect, url_for,request,session
import json 
course_file = "database/course.json"
coursetemp = []
def AddCourse(self,coursename,StudentID,courseID,instructor,location,day_of_week):
	student_file = "database/%d_courses.json" % StudentID
	with open (student_file, 'r', encoding='utf-8') as a:
		try:
			studenttemp=json.load(a)
		except json.JSONDecodeError:
			studenttemp=[]
	with open (course_file, 'r', encoding='utf-8') as a:
		try:
			coursetemp=json.load(a)
		except json.JSONDecodeError:
			coursetemp=[]
	for course in coursetemp:
		if(course["name"]==coursename):
			if(self.limitdetecting(coursename)=="Course full"):
				return "Course full"

			studenttemp["courses"].append(coursename)
			studenttemp["act_students"]+=1
			with open(student_file, 'r', encoding='utf-8') as wa:
				json.dump(studenttemp, wa, ensure_ascii=False, indent=4)
			return 'Added Successed!'
		elif(course["course_id"]==courseID):
			if(self.limitdetecting(coursename)=="Course full"): #這個是我故意用coursename當索引的 如果有衝突到再改
				return "Course full"

			studenttemp["courses"].append(coursename)
			studenttemp["act_students"]+=1
			with open(student_file, 'r', encoding='utf-8') as wa:
				json.dump(studenttemp, wa, ensure_ascii=False, indent=4)
			return 'Added Successed!'
		elif(course["instructor"]==instructor):
			if(self.limitdetecting(coursename)=="Course full"): #這個是我故意用coursename當索引的 如果有衝突到再改
				return "Course full"

			studenttemp["courses"].append(coursename)
			studenttemp["act_students"]+=1
			with open(student_file, 'r', encoding='utf-8') as wa:
				json.dump(studenttemp, wa, ensure_ascii=False, indent=4)
			return 'Added Successed!'
		elif(course["location"]==location):
			if(self.limitdetecting(coursename)=="Course full"): #這個是我故意用coursename當索引的 如果有衝突到再改
				return "Course full"

			studenttemp["courses"].append(coursename)
			studenttemp["act_students"]+=1
			with open(student_file, 'r', encoding='utf-8') as wa:
				json.dump(studenttemp, wa, ensure_ascii=False, indent=4)
			return 'Added Successed!'
		elif(course["day_of_week"]==day_of_week):
			if(self.limitdetecting(coursename)=="Course full"): #這個是我故意用coursename當索引的 如果有衝突到再改
				return "Course full"

			studenttemp["courses"].append(coursename)
			studenttemp["act_students"]+=1
			with open(student_file, 'r', encoding='utf-8') as wa:
				json.dump(studenttemp, wa, ensure_ascii=False, indent=4)
			return 'Added Successed!'
		else:
			return "Course is not exist"
		
	return 'Added Failed'
def limitdetecting(self,coursename):
		with open (course_file, 'r', encoding='utf-8') as a:
			try:
				coursetemp=json.load(a)
			except json.JSONDecodeError:
				coursetemp=[]
		for course in coursetemp:
			if course["name"] == coursename:
				if course["act_students"] >=course["max_students"]:
					return "Course full"
				else:
					return "Course not full"