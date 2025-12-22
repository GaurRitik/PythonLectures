info =[
    ("Alice","Maths"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Maths"),
    ("Bob","Maths"),
    ("Alice","English"),
    ("Charlie","English"),
    ("Alice","Maths"),
]

student_unique_courses = []
english_students = []
student_courses = {}
for tup in info:
    if tup[1] not in student_unique_courses:
        student_unique_courses.append(tup[1])
    if tup[1] == "English":
        english_students.append(tup[0])
    if tup[0] not in student_courses:
        student_courses[tup[0]] = {tup[1],}
    else:
        student_courses[tup[0]] |= {tup[1],}

print("Student Courses Dictionary:", student_courses)
print("Students enrolled in English:", english_students)
print("Courses offered:", student_unique_courses)