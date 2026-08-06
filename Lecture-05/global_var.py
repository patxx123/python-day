counter = 0

def increment():
    global counter
    counter += 6
increment()
increment()

print(counter)