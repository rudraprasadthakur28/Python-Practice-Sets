marks = {
    "Ravi" : 35,
    "Aman" : 65,
    "Priya" : 85,
    "Rahul" : 45
}

for student, mark in marks.items():
    if mark >= 80:
        print(student, "Excellent")
    elif mark >= 50:
        print(student, "Pass")
    else:
        print(student, "Fail")