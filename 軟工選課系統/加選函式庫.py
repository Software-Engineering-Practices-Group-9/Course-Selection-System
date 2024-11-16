import sys
import time
from flask import Flask, render_template, redirect, url_for,request,session
import json 
app = Flask(__name__)
app.secret_key = 'test'
courseinfo = "courseinfomation.json"
coursetemp = []

students=[]
class Courseadding():
	def AddCourse(self,coursename,StudentID):
		with open (courseinfo, 'r', encoding='utf-8') as a:
			try:
				coursetemp=json.load(a)
			except json.JSONDecodeError:
				coursetemp=[]
		for studentinsert in coursetemp:
			if(studentinsert["Coursename"]==coursename ):
				if(self.limitdetecting(coursename)=="Course full"):
					return "Course full"
				if "Addedstudents" not in studentinsert:
					studentinsert["Addedstudents"]=[]
				studentinsert["Addedstudents"].append(StudentID)
				with open(courseinfo, 'w', encoding='utf-8') as wa:
					json.dump(coursetemp, wa, ensure_ascii=False, indent=4)
				return 'Added Successed!'
			else:
				return "Course is not exist"
		return 'Added Failed'
	def limitdetecting(self,coursename):
		with open(courseinfo, 'r', encoding='utf-8') as a:
			try:
				coursetemp=json.load(a)
			except json.JSONDecodeError:
				coursetemp=[]
		for course in coursetemp:
			if course["Coursename"] == coursename:
				currentstudents= len(course["Addedstudents"])
				if currentstudents >=course["maxiumlimits"]:
					return "Course full"
				else:
					return "Course not full"
	def showcourseinfo(self,coursename):
		with open(courseinfo, 'r', encoding='utf-8') as a:
			try:
				coursetemp=json.load(a)
			except json.JSONDecodeError:
				coursetemp=[]
		for course in coursetemp:
			if course['Coursename'] == coursename:
				print("課程名稱: " + coursetemp['Coursename'])
				print("學分: " + coursetemp['Coursecredits'])
				print("節數: " + coursetemp['Coursetime'])
				print("人數上限: " + coursetemp['maxiumlimits'])
				print("授課教授: " + coursetemp['Professor'])
	def course_exisitence_check(self,coursename):
		with open(courseinfo, 'r', encoding='utf-8') as a:
			try:
				coursetemp = json.load(a)
			except json.JSONDecodeError:
				coursetemp=[]
		for course in coursetemp:
			if course['Coursename']==coursename:
				return "Course exists"
		return "Course is not exist"
	
#################################################################################################
#################################################################################################
#################################################################################################

	@app.route('/')
	def redirect_to_course_page():
		return redirect(url_for('ID_input'))
	@app.route('/IDInput', methods=['GET', 'POST'])
	def ID_input():
		if request.method == 'POST':
			studentid = request.form.get('studentid')
			if not studentid:
				return "Student ID is required", 400
			session['studentid'] = studentid
			return redirect(url_for('search_course'))
		else:
			return render_template('IDInput.html')
	@app.route('/CourseSearchPage', methods=['GET', 'POST'])
	def search_course():
		try:
			studentid = session.get('studentid')
			if request.method == 'POST':
				if 'add_course' in request.form:
					coursename = request.form['coursename']		
					course_adding = Courseadding()
					result = course_adding.AddCourse(coursename, studentid)

					with open(courseinfo, 'r', encoding='utf-8') as f:
						try:
							coursetemp = json.load(f)
						except json.JSONDecodeError:
							coursetemp = []
					
					keyword = request.form['keyword']
					search_results = [course for course in coursetemp if keyword in course['Coursename']]
					return render_template(
					'CourseSearchPage.html',
					results=search_results,
					keyword=keyword,
					add_result=result,
					studentid=studentid
					)
				else:
					keyword = request.form['coursename']

					with open(courseinfo, 'r', encoding='utf-8') as f:
						try:
							coursetemp = json.load(f)
						except json.JSONDecodeError:
							coursetemp = []
							
					result = [course for course in coursetemp if keyword in course['Coursename']]
					return render_template('CourseSearchPage.html', results=result, keyword=keyword, studentid=studentid)
			else:
				return render_template('CourseSearchPage.html', results=None, studentid=studentid)
		except Exception as e:
			return f"An error occurred: {str(e)}", 500
				
def main():
	#coursename = input('請輸入課程名稱: ')
	#if(Courseadding.course_exisitence_check(coursename) == "Course exists"):
	#	course_exisitence=1
	app.run(debug=True)
	

if __name__ == '__main__':
	main()
