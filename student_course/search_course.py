import re
def merge_sessions(sessions):
    if not sessions:
        return []
    sessions = sorted(map(int, sessions))  # 確保節次為數字並排序
    merged = []
    start = prev = sessions[0]
    for session in sessions[1:]:
        if session == prev + 1:  # 若當前節次與前一節次連續
            prev = session
        else:
            merged.append(f"{start}-{prev}" if start != prev else str(start))
            start = prev = session
    merged.append(f"{start}-{prev}" if start != prev else str(start))  # 處理最後一組
    return merged

def format_schedule(day_of_week, location):
    locations = re.split(r'[ /]+', location.strip())
    formatted_schedule = []
    location_index = 0  # 教室索引，用於對應 day_of_week


    for day, sessions in day_of_week.items():
        if sessions:  # 如果該天有課
            # 確保不超出 location 列表範圍
            current_location = locations[location_index] if location_index < len(locations) else locations[-1]
            session_ranges = merge_sessions(sessions)
            formatted_schedule.append(f"({day}) {' '.join([f'{r} {current_location}' for r in session_ranges])}")
            location_index += 1  # 更新索引，指向下一個教室

    return formatted_schedule


def filter_courses(courses, course_id=None, course_name=None, instructor=None, location=None, day_of_week=None, time_slot=None):
    if not any([course_id, course_name, instructor, location, day_of_week, time_slot]):
        return courses  # 如果沒有任何查詢條件，返回所有課程

    filtered_courses = []
    for course in courses:
        if course_id and course_id not in course['course_id']:
            continue
        if course_name and course_name not in course['name']:
            continue
        if instructor and instructor not in course['instructor']:
            continue
        if location and location not in course['location']:
            continue
        if day_of_week and day_of_week not in course['day_of_week']:
            continue

        filtered_courses.append(course)

    return filtered_courses
