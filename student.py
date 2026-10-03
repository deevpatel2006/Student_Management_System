def add_student(students, name, roll_no, department):
    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department
    }

    students.append(student)


def display_students(students):
    print("===== Student Management System =====")
    print("Student Details")        

    for student in students:
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Department:", student["department"])
        print()