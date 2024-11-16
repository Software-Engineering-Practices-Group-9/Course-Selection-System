from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
import json
import os

account_mgmt_bp = Blueprint('account_management', __name__, template_folder='templates')
DATABASE_PATH = 'database/accounts.json'

def load_accounts():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_accounts(accounts):
    with open(DATABASE_PATH, 'w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=4, ensure_ascii=False)


def create_student_courses_file(id):
    # 確保資料夾存在
    folder_path = 'database/student_data'
    os.makedirs(folder_path, exist_ok=True)
    
    # 學生課程檔案路徑
    file_path = os.path.join(folder_path, f"{id}_courses.json")
    
    # 預設的課程資料結構
    default_courses = {
        "id": id,
        "courses": []
    }
    
    # 保存 JSON 檔案
    with open(file_path, 'w') as f:
        json.dump(default_courses, f, indent=4)

# ----------------------------------------------------------------------------------------

@account_mgmt_bp.route('/')
def index():
    accounts = load_accounts()
    return render_template('account_management/account_management.html', accounts=accounts)

@account_mgmt_bp.route('/register', methods=['POST'])
def register():
    data = request.form
    role = data.get('role')
    id = data.get('id')

    new_account = {
        "id": id,
        "name": data.get('name'),
        "role": role,
        "password": data.get('password')
    }
    if role in ['學生', '系辦助教', '教授', '教務處人員']:  # 如果是學生或教職員，可以設置系級
        new_account["department"] = data.get('department')

    accounts = load_accounts()
    accounts.append(new_account)
    save_accounts(accounts)

    if role == '學生':
        create_student_courses_file(id)
    
    return redirect(url_for('account_management.index'))

@account_mgmt_bp.route('/delete/<account_id>', methods=['POST'])
def delete(account_id):
    accounts = load_accounts()
    accounts = [acc for acc in accounts if acc['id'] != account_id]
    save_accounts(accounts)
    return redirect(url_for('account_management.index'))



@account_mgmt_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    accounts = load_accounts()
    filtered_accounts = [acc for acc in accounts if query.lower() in acc['id'].lower()]
    return render_template('account_management/account_management.html', accounts=filtered_accounts)
