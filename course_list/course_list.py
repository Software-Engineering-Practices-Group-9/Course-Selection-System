from flask import Blueprint, render_template
from account_management.account_management import load_accounts
from utils import load_courses

course_list_bp = Blueprint('course_list', __name__, template_folder='templates')
COURSE_DATABASE_PATH = 'database/course.json'

@course_list_bp.route('/id=<student_id>', methods=['GET'])
def course_list(student_id):
    
    accounts = load_accounts()
    user = next((acc for acc in accounts if acc['id'] == student_id), None)

    courses = load_courses()
    
    return render_template('course_list/course_list.html', user=user, courses=courses)