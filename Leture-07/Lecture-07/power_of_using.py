def remove_dulicates(lst):
    return list(set(lst))

numbers = [1, 2, 3, 1, 2, 4, 5, 6, 5, 4, 3]
print(remove_dulicates(numbers))  # Output: [1, 2, 3, 4, 5, 6] (order may vary)