import random

x = 1
y = random.randint(1, 20)
a = []
for gen1 in range(y):
    a.append(random.randint(1,100))

w = 1
z = random.randint(1, 20)
b = []
for gen2 in range(z):
    b.append(random.randint(1,100))

c = []

print(f'List 1: {a}')
print('\n')
print(f'List 2: {b}')

for i in a:
    for j in b:
        if i in b:
            if i in c:
                continue
            else:
                c.append(i)

print('\n')
if not c:
    print('Shared Numbers: none')
else:
    print(f'Shared Numbers: {c}')