
def fib(idx):
    if idx == 0:
        return 0
    if idx == 1:
        return 1
    return fib(idx-1) + fib(idx-2)


def fib_w_memo(idx, memo=None):
    if memo is None:
        memo = {}  # dictionary from idx => fib(idx), example: memo[5] = 5

    # check if idx is in our dictionary, if so, return its value
    if idx in memo.keys():
        return memo[idx]

    # Compute
    if idx == 0:
        return 0
    if idx == 1:
        return 1

    value = fib_w_memo(idx-1, memo) + fib_w_memo(idx-2, memo)

    # Caching and return the value
    memo[idx] = value
    return value



import time

start = time.time()
for i in range(30):
    val = fib_w_memo(i)
    print(val)

end = time.time()
print('Total time is', end-start)

# 0.590054988861084
# 0.0004990100860595703

