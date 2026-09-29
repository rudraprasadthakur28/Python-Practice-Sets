marks = {
    "Ravi" : 60,
    "Aman" : 85,
    "Priya" : 90,
}

for student, mark in marks.items():
    if mark >= 80:
        print(student, "Excellent")
    elif mark <=79 and mark >= 50:
        print(student, "Pass")