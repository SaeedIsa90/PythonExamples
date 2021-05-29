
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


res = factorial(5)
print('Factorial results is: ', res)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


res = fib(7)
print('Fib result: ', res)
