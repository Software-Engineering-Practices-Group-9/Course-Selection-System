from flask import Blueprint, render_template, request, session, jsonify, json
from account_management.account_management import load_accounts
from utils import load_courses

course_list_bp = Blueprint("course_list", __name__, template_folder="templates")
COURSE_DATABASE_PATH = "database/course.json"


@course_list_bp.route("/id=<id>", methods=["GET"])
def course_list(id):
    accounts = load_accounts()
    user = next((acc for acc in accounts if acc["id"] == id), None)

    courses = load_courses()

    # Store the professor's ID in the session for later use
    session["professor_id"] = id

    # 分頁設定：每頁顯示 10 條課程
    page = request.args.get("page", 1, type=int)  # 默認頁面是 1
    per_page = 10  # 每頁顯示的課程數量

    # 使用 Flask-Paginate 模組的 pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_courses = courses[start:end]

    total_pages = (len(courses) // per_page) + (1 if len(courses) % per_page > 0 else 0)

    return render_template(
        "course_list/course_list.html",
        user=user,
        courses=paginated_courses,
        page=page,
        total_pages=total_pages,
    )


@course_list_bp.route("/cancel_course/course_id=<course_id>", methods=["POST"])
def cancel_course(course_id):
    # 加載現有的課程資料
    courses = load_courses()

    # 找到要移除的課程
    course_to_remove = None
    for course in courses:
        if course.get("course_id") == course_id:  # 使用 .get() 防止 keyError
            course_to_remove = course
            break

    if course_to_remove:
        # 如果找到該課程，將其移除
        courses.remove(course_to_remove)

        # 寫回到 JSON 文件
        try:
            with open("database/course.json", "w", encoding="utf-8") as file:
                json.dump(courses, file, ensure_ascii=False, indent=4)

            return jsonify({"message": "退選成功！", "status": "success"}), 200
        except Exception as e:
            return jsonify(
                {"message": f"寫入文件失敗: {str(e)}", "status": "error"}
            ), 500
    else:
        # 如果沒有找到該課程
        return jsonify({"message": "退選失敗！課程代碼無效。", "status": "error"}), 400
