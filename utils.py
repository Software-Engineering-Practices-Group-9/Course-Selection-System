# 這裡放置載入課程的函式
import json

def load_courses(): 
    course_file = "database/course.json"
    try:
        with open(course_file, 'r', encoding='utf-8') as file:
            courses = json.load(file)
            return courses
    except FileNotFoundError:
        return []

def load_student_courses(id):
    student_file = f"database/student_data/{id}_courses.json"
    try:
        with open(student_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 確保返回的是正確的格式
            return data.get('courses', [])
    except FileNotFoundError:
        return []  # 如果檔案不存在，返回空課程列表
    except json.JSONDecodeError:
        return []  # 如果 JSON 解析錯誤，也返回空課程列表


def save_student_courses(id, student_courses):
    course_file = f"database/student_data/{id}_courses.json"
    with open(course_file, 'w', encoding='utf-8') as file:
        json.dump(student_courses, file, ensure_ascii=False, indent=4)

def save_courses(courses):
    course_file = "database/course.json"
    with open(course_file, 'w', encoding='utf-8') as file:
        json.dump(courses, file, ensure_ascii=False, indent=4)