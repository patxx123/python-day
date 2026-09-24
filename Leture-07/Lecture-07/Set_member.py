# Adding and removing items
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

fruits.discard("grape")
print(fruits)  # Output: {'apple', 'cherry', 'orange'} (no error    raised)

removed_item = fruits.pop()
print(removed_item)
print(fruits)  # Output: {'cherry', 'orange'} (an arbitrary item    removed)

fruits.clear()
print(fruits)  # Output: set() (empty set)