from flask import Flask
from account_management.account_management import account_mgmt_bp
from login_system.login import login_bp
from student_course.student_course import student_course_bp
from student_course.student_list import student_list_bp
from course_list.course_list import course_list_bp
from course_list.create_course import create_course_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'efb658580b34b7c6a6e15208b8ba545d'

app.register_blueprint(account_mgmt_bp, url_prefix='/account')
app.register_blueprint(login_bp)
<<<<<<< HEAD
app.register_blueprint(student_course_bp, url_prefix='/student_course')
app.register_blueprint(student_list_bp, url_prefix='/student_list')
app.register_blueprint(course_list_bp, url_prefix='/course_list')
app.register_blueprint(create_course_bp, url_prefix='/create_course')
=======
app.register_blueprint(create_course_bp, url_prefix='/create_course')
app.register_blueprint(course_list_bp, url_prefix='/course_list')
app.register_blueprint(student_list_bp, url_prefix='/student_list')
app.register_blueprint(student_course_bp, url_prefix='/student_course')
>>>>>>> feature/drop-course

if __name__ == "__main__":
    app.run(debug=True)