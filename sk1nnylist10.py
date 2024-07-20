a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

b = [i for i in a if i < 5]
print(b)

num = input('Enter a number: ')
for i in a:
    if i < int(num):
        print(i)