student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

print(student.keys())
print(student.values())
print(student.items())
print(student.get('name')) 
print(student.get('grade', ' Not found'))  # Using default value if key doesn't exist

major = student.pop('major')  # Remove key-value pair and return value
print(major)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 26}

last_item = student.popitem()  # Remove and return an arbitrary key-value pair
print(last_item)  # Output: ('age', 26) (or another key-value pair)
print(student)  # Output: {'name': 'Alice'} (remaining items in the dictionary

student.clear()  # Remove all items from the dictionary
print(student)  # Output: {} (empty dictionary)