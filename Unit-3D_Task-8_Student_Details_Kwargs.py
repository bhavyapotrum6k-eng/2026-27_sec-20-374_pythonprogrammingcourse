def student_details(name, **marks):
    print("Student Name:", name)
    for subject, mark in marks.items():
        print(subject, ":", mark)

student_details(name="Krishna", Telugu=85, English=90, Maths=95)