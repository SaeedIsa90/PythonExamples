import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

print('\n---------- Dimensions ----------')
# Dimensions
# 0-D array
a = np.array(120)
print('0 d array:', a)

# 1-D array
one_d = np.array([3, 1, 7, 5])
print('1 d array:', one_d)

# 2-D array
two_d = np.array([[1, 3, 2], [5, 6, 4]])
print('2 d array:\n', two_d)

# 3-D array
three_d = np.array([[[1, 2], [2, 3]], [[3, 5], [6, 7]]])
print('3 d array:\n', three_d)

# N-D array
# ...

print('\n---------- Array attributes ----------')
print('Array dimensions:', two_d.ndim)
print('Array shape:', two_d.shape)

print('\n---------- Accessing/Indexing ----------')
print('first item in one d array:', one_d[0])
print('first item in two d array:', two_d[0, 0])
print('first item in three d array:', three_d[0, 0, 0])

print('\n---------- Iterating ----------')
# 1-d array iterating
for x in one_d:
    print(x)

# 2-d array iterating
print('Iterating over 2 d array')
for x in two_d:
    for y in x:
        print(y)

# 3-d array iterating
print('Iterating over 3 d array')
for x in three_d:
    for y in x:
        for f in y:
            print(f)

print('Iterating over all items in array using nditer:')
for x in np.nditer(two_d):
    print(x)

print('\n---------- Search ----------')
# where function
print(np.where(two_d == 4))  # will find all indices match the condition
print(np.where(two_d % 2 == 0))  # will find all indices match the condition (all even numbers)

print('\n---------- Sort ----------')
print('Sorting array:\n', np.sort(one_d))
print('Sorting each row in array: \n', np.sort(two_d))

print('\n---------- Random numbers ----------')
print('Random integer:', np.random.randint(100))
print('Random integer between 2 numbers:', np.random.randint(10, 80))
print('Random float ben 0-1:', np.random.rand())

print('\n---------- Array generation ----------')
print('Generating integer matrix 2x3 with random integer numbers:\n', np.random.randint(10, 90, size=(2, 3)))
print('Generating float matrix 2x3 with random numbers 0-1:\n', np.random.rand(2, 3))
print('Generating zeros matrix 2x3:\n', np.zeros((2, 3), int))
print('Generating ones matrix 2x3:\n', np.ones((2, 3), int))

print('\n---------- Transpose ----------')
two_d_t = two_d.T
print('original 2 d:\n', two_d, two_d.shape)
print('Transposed 2 d:\n', two_d_t, two_d_t.shape)

print('\n---------- copy ----------')
two_d_c = two_d.copy()
two_d_c[0, 1] = 1000192
print('Original 2d:\n', two_d)
print('copied 2d:\n', two_d_c)

print('---------- Mathematical operations ----------')
a = np.array([1, 2])
b = np.array([3, 4])
print('Result of a + b: ', np.add(a, b))
print('Result of a - b: ', np.subtract(a, b))
print('Result of a * b: ', np.multiply(a, b))
print('Result of a / b: ', np.divide(a, b))
print('Result of a ^ b: ', np.power(a, b))
print('Result of a ^ 2: ', np.power(a, 2))


print('\n---------- Trigonometric operations ----------')
a = np.array([0, 1])
print(np.sin(a))
print(np.cos(a))

print('\n---------- Statistical functions ----------')
a = two_d
print('Min item in array:', np.amin(a))
print('Max item in array:', np.amax(a))
print('Median of array:', np.median(a))
print('standard deviation of array:', np.std(a))
print('Average of array:', np.average(a))
print('Mean of array:', np.mean(a))
print('Variance of array:', np.var(a))

print('\n---------- Algebra functions ----------')
a = np.array([2, 4])
b = np.array([3, 5])
print('1-d Matrices multiplication:\n', np.matmul(a, b))

a = np.array([[2, 4], [1, 3]])
b = np.array([[3, 5], [4, 6]])
print('2-d Matrices multiplication:\n', np.matmul(a, b))

print('\n---------- Algebra functions ----------')
a = np.array([1, 2, 3, 5, 6, 1, 2, 3, 4, 1, 1, 2, 6])
print('Histogram of array', np.histogram(a))
