# Lambda function
# lambda args: expression
#   - any number of args
#   - only one expression

# Default way to write a function
def my_add(x):
    return x+1
my_add(1)

# 1 argument example:
my_func = lambda x: x + 1
print('Lambda add function', my_func(10))

# multiple arguments example
my_4_add = lambda a, b, c, d: a + b + c + d
res = my_4_add(1, 2, 3, 4)
print('Lambda add function with 4 arguments', res)


# List example: add 1 to each item
# without lambda:
def add_1(x):
    return x + 1

lst = [1, 2, 3, 4]
new_lst = list(map(add_1, lst))
print('New list res', new_lst)

# with lambda function pointer
new_lst = list(map(my_func, lst))
print('New list with lambda res', new_lst)

# Using lambda directly in map function
new_lst = list(map(lambda x: x +1, lst))
print('New list with lambda res', new_lst)

# Lambda power example
new_lst = list(map(lambda x: x**2, lst))
print('New list - power one each element, new_lst', new_lst)
