import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a)
print(b)

def unique(temp):
    list_set = set(temp)
    unique_list = (list(list_set))
    return unique_list

c = unique(a)
d = unique(b)
for i in c:
    for j in d:
        if i == j:
            print(i)

e = random.sample(range(10, 30), 5)
f = random.sample(range(10, 30), 10)
print(e)
print(f)
g = unique(e)
h = unique(f)
for i in g:
    for j in h:
        if i == j:
            print(i)