student = {"name": "Alice", "age": 25, "grade": "A"}
student["age"] = 26 # Update age
student["major"] = "Computer Science" # Add new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26, 'grade': 'A', 'major': 'Computer Science'}

del student["grade"] # Remove key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

removed_major = student.pop("major") # Remove key-value pair and return value
print(removed_major)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 26}