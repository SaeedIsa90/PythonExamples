# Definition
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lst)
print(len(lst))

# Indexing - starts from 0
print(lst[0], '----', lst[5])

# Slicing
# from:to
print(lst[2:5])

# from:  ==> to the end
print(lst[4:])

# :to    ==> from the start
print(lst[:6])

# Indexing
# from the end: last element
print(lst[-1])
print(lst[-2])
# Slicing using minus
print(lst[2:-1])

# operator ::
# from:steps
print(lst[::2])

# steps from
print(lst[1::2])

# Reverse using ::
print(lst)
lst2 = lst[::-1]
print(lst2)

# Concatenation
lst2 = [5, 15, 25, 35]
lst3 = lst + lst2
print(lst3)

# Functions
# Clear
print(lst2)
lst2.clear()
print('lst2 after clear:', lst2)

# Copy
print(lst3)
lst4 = lst3.copy()
print(lst4)

# Sum
s = sum(lst)
print(s)

# reverse
lst2 = [5, 15, 25, 35]
lst2.reverse()
print(lst2)

# Comprehension
# lst2 = [1^2 ... 6^2]
lst2 = [i**2 for i in range(1, 7)]
print(lst2)

