from flask import Blueprint, render_template, request, redirect, url_for, session
from account_management.account_management import load_accounts
from utils import save_courses, load_courses

create_course_bp = Blueprint('create_course', __name__, template_folder='templates')

@create_course_bp.route('/create_course/id=<id>')
def home(id):
    courses = load_courses()

    accounts = load_accounts()
    professor = next((acc for acc in accounts if acc['id'] == id), None)

    # Store the professor's ID in the session for later use
    session['professor_id'] = id

    # 分頁設定：每頁顯示 10 條課程
    page = request.args.get('page', 1, type=int)  # 默認頁面是 1
    per_page = 10  # 每頁顯示的課程數量

    # 使用 Flask-Paginate 模組的 pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_courses = courses[start:end]

    total_pages = (len(courses) // per_page) + (1 if len(courses) % per_page > 0 else 0)

    return render_template('create_course/home.html', courses=paginated_courses, professor=professor, page=page, total_pages=total_pages)

@create_course_bp.route('/create_course/add_course', methods=['GET', 'POST'])
def add_course():
    accounts = load_accounts()

    if request.method == 'POST':
        # 載入現有課程
        courses = load_courses()  # 確保先載入已儲存的課程列表

        # 獲取手動輸入的課程代碼
        course_id = request.form['course_id']
        
        # 檢查課程代碼是否已存在
        if any(course['course_id'] == course_id for course in courses):
            # 如果需要，這裡可以加入錯誤處理，例如回傳錯誤訊息
            return "課程代碼已存在，請使用其他代碼", 400
        
        course_name = request.form['course_name']
        compulsory = request.form['compulsory']
        max_students = int(request.form['max_students'])
        act_students = 0
        credits = int(request.form['credits'])
        location = request.form['location']
        description = request.form['description']

        # Initialize an empty dictionary for day_of_week
        day_of_week = {
            "一": [],
            "二": [],
            "三": [],
            "四": [],
            "五": []
        }

        # Populate day_of_week based on the form input
        for day in day_of_week.keys():
            periods = request.form.getlist(f'day_of_week[{day}]')
            day_of_week[day] = periods

        # Debug: Check the structure of day_of_week before saving
        print(f"Day of Week Structure: {day_of_week}")

        # Get the professor ID from the session
        professor_id = session.get('professor_id')

        # Find the professor's name based on the ID
        professor = next((acc for acc in accounts if acc['id'] == professor_id), None)
        instructor_name = professor['name'] if professor else 'Unknown'

        # Add the new course data to the courses list
        courses.append({
            "course_id": course_id,
            "course_name": course_name,
            "instructor": instructor_name,  # Set the professor's name
            "compulsory": compulsory,
            "credits": credits,
            "act_students": act_students,
            "max_students": max_students,
            "day_of_week": day_of_week,  # Store as a dictionary
            "location": location,
            "description": description,
        })

        # Save all courses to the JSON file
        save_courses(courses)

        return redirect(url_for('create_course.home', id=professor_id))

    return render_template('create_course/add_course.html')
