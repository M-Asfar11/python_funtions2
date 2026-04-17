student = [
    {"name": "asfar", "gpa": 3.5,"cgpa": 3.7},
    {"name": "ahmad", "gpa": 3.9,"cgpa": 3.7},
    {"name": "hassan","gpa": 2.9},
    {"name": "musa", "gpa": 3.9,"cgpa": 3.7}
]

def count_student(student_list):
    return len(student_list)
    
print("total students:", count_student(student))