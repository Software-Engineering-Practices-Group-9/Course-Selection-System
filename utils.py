# 這裡放置載入和刪除課程的函式
import json
from collections import OrderedDict
import os # 使用該模組固定json字典順序

def load_courses(): 
    course_file = "database/course.json"
    try:
        with open(course_file, 'r', encoding='utf-8') as file:
            courses = json.load(file, object_pairs_hook=OrderedDict)
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


# cancel_course 使用
def remove_course_from_all_students(course_id):
    # 取得學生課程資料檔案
    student_files = [f for f in os.listdir("database/student_data/") if f.endswith('_courses.json')]
    
    for student_file in student_files:
        student_course_file = os.path.join("database/student_data/", student_file)
        
        try:
            # 讀取學生的課程資料
            with open(student_course_file, 'r', encoding='utf-8') as file:
                student_data = json.load(file)
            
            # 刪除該課程
            updated_courses = [
                course for course in student_data.get('courses', []) if course.get('course_id') != course_id
            ]
            
            # 儲存更新後的課程資料
            with open(student_course_file, 'w', encoding='utf-8') as file:
                json.dump({'courses': updated_courses}, file, ensure_ascii=False, indent=4)
        
        except Exception as e:
            print(f"無法處理學生檔案 {student_file}: {str(e)}")