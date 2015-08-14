bar = 4


def set_bar():
    # Comment 1
    bar = "dog"


def test():
    # Comment 2
    set_bar()
    print('bar is {}'.format(bar))


# Comment 3
test()

print('bar is {}'.format(bar))
