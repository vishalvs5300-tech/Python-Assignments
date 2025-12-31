# Task 1: Create a Dictionary of Student Marks

student_marks = {"Alice":85, "Carol":90, "Rohan":79, "Rahul":91,}
name = input("Enter the student's name: ").capitalize()

# If-else condition:
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")

else:
    print("Student not found.")
