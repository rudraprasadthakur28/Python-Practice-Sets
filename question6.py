marks = {
    "Ravi" : 45,
    "Aman" : 75,
    "Priya" : 85,
    "Rahul" : 30
}

for student, mark in marks.items():
    if mark >= 80:
        print(f"Student name is {student} and mark is {mark} Excellent")
    elif mark >= 50:
        print(f"Student name is {student} and mark is {mark} Pass")
    else:
        print(f"Student name is {student} and mark is {mark} Fail")