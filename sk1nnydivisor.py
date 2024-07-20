import math
num = input('Enter a number: ')
for i in range((int(num)//2)+1):
    if i != 0:
        if int(num)%i == 0:
            print(i)
print(num)