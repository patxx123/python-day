keep_going = 'Y'
while keep_going.upper() == 'Y':
    sales =float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the comission rate: '))
    commission = sales * comm_rate
    print(f'The comission is ${commission:.2f}')
    keep_going = input('Do you want to calculate another' + \
                       ' commission (Y/N): ')