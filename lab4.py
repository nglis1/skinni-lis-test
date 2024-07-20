num = int(input('Enter a random number: '))

x = list(range(1, num+1))
div = []

for i in x:
    if num%i == 0:
        div.append(i)

print(div)