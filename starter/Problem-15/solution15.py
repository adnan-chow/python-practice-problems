def check_student(marks):
    for mark in marks:
        if mark < 40:
            return "FAILED"
    average = sum(marks) / len(marks)
    return f"Average marks: {average}"

# Test the function
student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

print("Student 1:", check_student(student_1))
print("Student 2:", check_student(student_2))