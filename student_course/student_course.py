from flask import Blueprint, render_template, request
from account_management.account_management import load_accounts
import json

student_course_bp = Blueprint('student_course', __name__, template_folder='templates')

def merge_sessions(sessions):
    if not sessions:
        return []
    sessions = sorted(map(int, sessions))  # 確保節次為數字並排序
    merged = []
    start = prev = sessions[0]
    for session in sessions[1:]:
        if session == prev + 1:  # 若當前節次與前一節次連續
            prev = session
        else:
            merged.append(f"{start}-{prev}" if start != prev else str(start))
            start = prev = session
    merged.append(f"{start}-{prev}" if start != prev else str(start))  # 處理最後一組
    return merged

def format_schedule(day_of_week, location):
    locations = location.split(' / ')  # 將教室分成列表
    formatted_schedule = []
    location_index = 0  # 教室索引，用於對應 day_of_week


    for day, sessions in day_of_week.items():
        if sessions:  # 如果該天有課
            # 確保不超出 location 列表範圍
            current_location = locations[location_index] if location_index < len(locations) else locations[-1]
            session_ranges = merge_sessions(sessions)
            formatted_schedule.append(f"({day}) {' '.join([f'{r} {current_location}' for r in session_ranges])}")
            location_index += 1  # 更新索引，指向下一個教室

    return formatted_schedule


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

def load_student_courses(student_id):
    course_file = f"database/{student_id}_courses.json"
    try:
        with open(course_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 如果檔案不存在，返回空課程列表
    

def filter_courses(courses, course_id=None, course_name=None, instructor=None, location=None, day_of_week=None, time_slot=None):
    if not any([course_id, course_name, instructor, location, day_of_week, time_slot]):
        return courses  # 如果沒有任何查詢條件，返回所有課程

    filtered_courses = []
    for course in courses:
        if course_id and course_id not in course['course_id']:
            continue
        if course_name and course_name not in course['name']:
            continue
        if instructor and instructor not in course['instructor']:
            continue
        if location and location not in course['location']:
            continue
        if day_of_week and day_of_week not in course['day_of_week']:
            continue
        if time_slot and not any(time_slot in slot for slots in course['day_of_week'].values() for slot in slots):
            continue

        filtered_courses.append(course)

    return filtered_courses



# -------------------------------- 處理課程各功能 --------------------------------

@student_course_bp.route('/id=<student_id>')
def student_page(student_id):
    accounts = load_accounts()
    student = next((acc for acc in accounts if acc['id'] == student_id), None)

    student_courses = load_student_courses(student_id)

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