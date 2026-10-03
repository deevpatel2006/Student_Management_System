from student import add_student, display_students, search_student

students = []

add_student(students, "Deev", 101, "IT")
add_student(students, "Rahul", 102, "CSE")

display_students(students)

search_student(students, 101)