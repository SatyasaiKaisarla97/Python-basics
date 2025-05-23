student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}
name =  str(input("please enter the student name: "))
if name in student_marks:
    print(f"The student {name} has scored {student_marks[name]} marks")
else:
    print(f"The student {name} is not in the list")