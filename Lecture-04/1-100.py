column = int(input('Enter number colum '))
for i in range(1,101):
    print(f"{i:3}", end=" ")
    if i % column == 0:
        print()