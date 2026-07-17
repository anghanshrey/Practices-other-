students = [
    {"id": 101, "name": "Alice", "score":85},
    {"id": 102, "name": "Bob", "score":78},
    {"id": 103, "name": "Charlie", "score":92},
]

print("="*40)
print("name for each student using loop")
print("="*40)

"""
for student in students:
    print(student["name"])
"""

print("="*40)
print("average score of all students.")
print("="*40)

"""
sum = 0

for student in students:
    sum += student["score"]

print("average Score of all student",sum/len(students))
"""

print("="*40)
print("Add a new student")
print("="*40)

"""
students.append( {"id": 104, "name": "Robinson", "score":88} )

print(students)
"""

print("="*40)
print("Update the score")
print("="*40)

"""
for student in students:
    if student["id"] == 102:
        student["score"] = 88

print(students)
"""

print("="*40)
print("Delete the record 'Charlie'")
print("="*40)

"""
for student in students:
    if student['name'] == 'Charlie':
        students.remove(student)
        break;

print(students)
"""

print("="*40)
print("print names scored more than 80'")
print("="*40)

"""
for student in students:
    if student["score"] > 80:
        print(student['name'])
"""    

print("="*40)
print("sort list in descending'")
print("="*40)

"""
n = len(students)

for i in range(n):
    for j in range(n - i - 1):
        if students[j]["score"] < students[j + 1]["score"]:
            temp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = temp

print("Students after sorting:")
for s in students:
    print(s)
"""

print("="*40)
print("Student highest score'")
print("="*40)

"""
highest = students[0]

for i in students:
    if i["score"] > highest["score"]:
        highest = i

print("highest Scorer :")
print(highest)
"""

print("="*40)
print("Create Report'")
print("="*40)

"""
for s in students:
    if s["score"] > 90:
        grades = "A"
    elif s["score"] > 80 and s["score"] < 89:
        grades = "B"
    else:
        grades = "C"

    print(f"Name: {s['name']} | Score: {s['score']} | Grade: {grades}")
"""
