# MAP
lst1 = [1, 2, 3, 4, 5, 6]

# + 1
lst2 = []
for i in lst1:
    lst2.append(i + 1)
print(lst2)


# Using map
def add_1(x):
    return x + 1

lst2 = []
for i in lst1:
    lst2.append(add_1(i))
print(lst2)

lst3 = list(map(add_1, lst1))
print(lst3)

# Power example
def power(x):
    return x*x

lst4 = list(map(power, lst1))
print(lst4)

lst = ['Saeed', 'Isa', 'Hello']
def add_space(x):
    return '__   ' + x + '   __'

lst5 = list(map(add_space, lst))
print(lst5)
