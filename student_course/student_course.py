from flask import Blueprint, render_template, request
from account_management.account_management import load_accounts
from student_course.search_course import filter_courses, format_schedule
import json

student_course_bp = Blueprint('student_course', __name__, template_folder='templates')

def load_courses(): 
    course_file = "database/course.json"
    try:
        with open(course_file, 'r', encoding='utf-8') as file:
            courses = json.load(file)
            # 為所有課程添加格式化的上課時間
            for course in courses:
                course['formatted_schedule'] = format_schedule(course['day_of_week'], course['location'])
            return courses
    except FileNotFoundError:
        return []

def load_student_courses(id):
    course_file = f"database/{id}_courses.json"
    try:
        with open(course_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 如果檔案不存在，返回空課程列表
    

# -------------------------------- 處理課程各功能 --------------------------------

@student_course_bp.route('/id=<id>')
def student_page(id):
    accounts = load_accounts()
    student = next((acc for acc in accounts if acc['id'] == id), None)

    student_courses = load_student_courses(id)

    # 載入所有課程資料
    courses = load_courses()

    # 取得查詢條件
    course_id = request.args.get('course_id')
    course_name = request.args.get('course_name')
    instructor = request.args.get('instructor')
    location = request.args.get('location')
    day_of_week = request.args.get('day_of_week')
    time_slot = request.args.get('time_slot')

    # 使用篩選函式過濾課程
    filtered_courses = filter_courses(
        courses,
        course_id=course_id,
        course_name=course_name,
        instructor=instructor,
        location=location,
        day_of_week=day_of_week,
        time_slot=time_slot
    )

    return render_template('student_course/student.html', student=student, student_courses=student_courses, courses=filtered_courses)