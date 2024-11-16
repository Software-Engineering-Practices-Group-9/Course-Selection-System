from flask import Blueprint, render_template
from account_management.account_management import load_accounts

student_list_bp = Blueprint('student_list', __name__, template_folder='templates')

@student_list_bp.route('/student_list')
def student_list():
    accounts = load_accounts()
    student = [acc for acc in accounts if acc['role'] == '學生']
    return render_template('student_list/student_list.html', students=student)