n = 1026

def fib(n):
    i = 0
    nextterm = 1
    present = 1
    previous = 0

    while i < n:
        nextterm = present + previous
        present = previous
        previous = nextterm
        i = i + 1
    return nextterm

result = fib(n)
print(result & (2 ** 64 - 1))