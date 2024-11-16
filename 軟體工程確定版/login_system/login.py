from flask import Blueprint, render_template, request, redirect, url_for
import json

login_bp = Blueprint('login', __name__, template_folder='templates')
DATABASE_PATH = 'database/accounts.json'

def load_accounts():
    with open(DATABASE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)
    
@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']
        accounts = load_accounts()

        # 比對 id 和 password
        for account in accounts:
            if account['id'] == user_id and account['password'] == password:
                if account['role'] == '學生':
                    return redirect(url_for('student_course.student_page', student_id=user_id))
                elif account['role'] == '系辦助教':
                    return redirect(url_for('student_list.student_list', student_id=user_id))
                # elif account['role'] == '教授':  # 教授
                #     return redirect(url_for('course_list.course_list', student_id=user_id))
                elif account['role'] == '教務處人員':
                    return redirect(url_for('course_list.course_list', student_id=user_id))
        return render_template('login_system/login.html', error="帳號或密碼錯誤")
    return render_template('login_system/login.html')