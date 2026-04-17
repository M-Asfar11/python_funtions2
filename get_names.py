student = [
    {"name": "asfar", "gpa": 3.5,"cgpa": 3.7},
    {"name": "ahmad", "gpa": 3.9,"cgpa": 3.7},
    {"name": "hassan","gpa": 2.9},
    {"name": "musa", "gpa": 3.9,"cgpa": 3.7}
]

# getting the names from the dict
def get_names(student_list):
    for student in student_list:
        print(student["name"])
        
get_names(student)
