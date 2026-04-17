def findStudent(student_list):
    name = input("Enter student name: ")
    
    for std in student_list:
        if std.get("name") == name:
            print("Found:", std)
            break
    else:
        print("Not found")


student = [
    {"name": "asfar", "gpa": 3.5,"cgpa": 3.7},
    {"name": "ahmad", "gpa": 3.9,"cgpa": 3.7},
    {"name": "hassan","gpa": 2.9},
    {"name": "musa", "gpa": 3.9,"cgpa": 3.7}
]

findStudent(student)
