

def factorial(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + factorial(n-1)


def print_factors(n, pretty=False):
    if n <= 1:
        return
    factors = list()
    for i in range(2, n):
        if n % i == 0:
            factors.append(str(i))
    if len(factors):
        if pretty:
            print("The factors of {} are: {}.".format(str(n), ', '.join(factors)))
        else:
            print("{}: {}".format(str(n), ' '.join(factors)))
    else:
        if pretty:
            print("{} is prime and has no factors.".format(str(n)))
        else:
            print("{}:".format(str(n)))


for x in range(-2, 20):
    x_fact = factorial(x)
    stuff = "{}! is {}".format(x, x_fact)
    print(stuff)
