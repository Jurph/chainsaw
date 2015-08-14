

def factorial(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + factorial(n-1)


for x in range(-2, 5):
    x_fact = factorial(x)
    stuff = "{}! is {}".format(x, x_fact)
    print(stuff)



