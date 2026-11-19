student = {'name': 'Ram', 'age': 20, 'course': 'BCA'}

print("Dictionary:", student)
print("Name:", student['name'])
print("Age:", student.get('age'))

student['age'] = 21
student['city'] = 'Nuzvid'

print("Updated Dictionary:", student)