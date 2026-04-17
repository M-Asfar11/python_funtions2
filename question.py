def get_honor_students(student_list):
    honor_students = []
    for student in student_list:
        try:
            if student["cgpa"] > 3.0:
                honor_students.append({"name":student["name"]})
        except KeyError:
            print("Missing 'cgpa' key for student:", student.get("name", "Unknown"))
    return honor_students

students = [
    {"name": "asfar", "gpa": 3.5,"cgpa": 3.7},
    {"name": "ahmad", "gpa": 3.9,"cgpa": 3.7},
    {"name": "hassan","gpa": 2.9},
    {"name": "musa", "gpa": 3.9,"cgpa": 3.7}
]

result = get_honor_students(students)
print(result)