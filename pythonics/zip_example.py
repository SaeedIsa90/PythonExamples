# ZIP
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [6, 5, 4, 3, 2, 1]

# build lst3: lst3[i] = lst1[i] + lst2[i]
# Old way
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print(lst3)

# Using ZIP
lst3 = []
for i, j in zip(lst1, lst2):
    lst3.append(i + j)
print(lst3)

# Not the same length
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [6, 5, 4, 3]

lst3 = []
for i, j in zip(lst1, lst2):
    print(i, j)
    lst3.append(i + j)
print(lst3)

# Multiple lists
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [6, 5, 4, 3, 2, 1]
lst3 = [3, 5, 3, 5, 3]
lst4 = []
for i, j, k in zip(lst1, lst2, lst3):
    print(i, j, k)
    lst4.append(i + j + k)
print(lst4)

# Dict example
dict1 = {"Name": "Saeed", "Family": "Isa", "Youtube": "Yes"}
dict2 = {"Name": "Salam", "Family": "Isa"}
for i, j in zip(dict1.items(), dict2.items()):
    print(i, '----', j)

# Subscribe and share :)
