num = input('Enter a number: ')
check = input('Enter a divisor: ')

if int(num)%4 == 0 and int(num) > 4:
    print(f'{num} is a multiple of 4.\n')
elif int(num)%2 == 0:
    print(f'{num} is an even number.\n')
else:
    print(f'{num} is an odd number. \n')

if int(num)%int(check) == 0:
    print(f'{check} divides evenly into {num}.\n')
else:
    print(f'{check} does not evenly divide into {num}.\n')