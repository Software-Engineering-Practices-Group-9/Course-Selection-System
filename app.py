from flask import Flask, render_template, request, redirect, url_for, session
from login import login_bp  # 匯入你在 login.py 中定義的 Blueprint
import json
import os

app = Flask(__name__)

# JSON 檔案路徑
DATA_FILE = 'courses.json'

# 註冊 Blueprint
app.register_blueprint(login_bp, url_prefix='/login')  # 根據需要設置 url_prefix

# 讀取課程資料
def load_courses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 儲存課程資料
def save_courses(courses):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)

@app.route('/teacher')
def home():
    courses = load_courses()
    return render_template('home.html', courses=courses)

@app.route('/teacher/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        # 載入現有課程
        courses = load_courses()  # 確保先載入已儲存的課程列表
        
        course_name = request.form['course_name']
        compulsory = request.form['compulsory']
        max_students = int(request.form['max_students'])
        act_students = 0
        credits = int(request.form['credits'])
        location = request.form['location']
        description = request.form['description']

        # Initialize an empty dictionary for day_of_week
        day_of_week = {
            "星期一": [],
            "星期二": [],
            "星期三": [],
            "星期四": [],
            "星期五": []
        }

        # Populate day_of_week based on the form input
        for day in day_of_week.keys():
            periods = request.form.getlist(f'day_of_week[{day}]')
            day_of_week[day] = periods

        # Debug: Check the structure of day_of_week before saving
        print(f"Day of Week Structure: {day_of_week}")

        # Generate a course ID (e.g., auto-increment from 0001)
        if not courses:
            course_id = "0001"  # 若無課程則從 0001 開始
        else:
            max_id = max(int(course['course_id']) for course in courses)
            course_id = f"{max_id + 1:04d}"

        # Add the new course data to the courses list
        courses.append({
            "course_id": course_id,
            "course_name": course_name,
            "compulsory": compulsory,
            "act_students": act_students,
            "max_students": max_students,
            "credits": credits,
            "location": location,
            "description": description,
            "day_of_week": day_of_week,  # Store as a dictionary
            "instructor": "預設老師"  # Example instructor, can be dynamic
        })

        # Save all courses to the JSON file
        save_courses(courses)

        return redirect(url_for('home'))
    
    return render_template('add_course.html')


if __name__ == '__main__':
    app.run(debug=True)
