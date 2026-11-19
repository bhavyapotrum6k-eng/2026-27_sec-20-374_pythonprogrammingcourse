students = [
    {'name': 'Ram', 'marks': 75},
    {'name': 'Sita', 'marks': 90},
    {'name': 'Ravi', 'marks': 60}
]
sorted_students = sorted(students, key=lambda x: x['marks'])
print('Sorted List:', sorted_students)