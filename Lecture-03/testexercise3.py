number = int(input("enter the number : "))
hourly = int(input("enter the hourly : "))

pay = (40 * hourly) + ((number - 40 ) * hourly * 1.5)

print("The gross pay is $" , pay)

