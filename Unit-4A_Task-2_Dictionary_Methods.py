student = {'name': 'Ram', 'age': 20, 'course': 'BCA'}

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))
print("Get age:", student.get('age'))

student.update({'age': 21, 'city': 'Nuzvid'})
print("After update:", student)

student.pop('course')
print("After pop:", student)