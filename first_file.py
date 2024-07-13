first = input('Enter your First Name:')
last = input('Enter your Last Name:')
age = input('Enter your age:')
age = int(age)

newAge = (100 - age) + 2024
print(first + ' ' + last + ' ' + 'will turn 100 years old in ' + str(newAge))