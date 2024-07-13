from datetime import datetime
current_year = datetime.now().year

first = input('Enter your First Name: ')
last = input('Enter your Last Name: ')
age = input('Enter your age: ')

year100 = current_year + (100 - int(age))

copyNum = input('Enter a number : ')
for i in range(int(copyNum)):
    print(f"You will turn 100 years old in the year {year100}.\n")