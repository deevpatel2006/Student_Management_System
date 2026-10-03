from student import add_student, display_students, search_student
from attendance import mark_attendance, display_attendance

students = []

add_student(students, "Deev", 101, "IT")
add_student(students, "Rahul", 102, "CSE")

display_students(students)

search_student(students, 101)

attendance = {}

mark_attendance(attendance, 101, "Present")
mark_attendance(attendance, 102, "Absent")

display_attendance(attendance)
print("GitHub integration completed")