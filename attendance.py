def mark_attendance(attendance, roll_no, status):
    attendance[roll_no] = status


def display_attendance(attendance):
    print("Attendance Details")

    for roll_no, status in attendance.items():
        print("Roll No:", roll_no, "Status:", status)