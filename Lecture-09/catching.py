try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"the result is {result}")
print("End of program")