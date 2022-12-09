def max_number(x, y):
    if x > y:
        print(x)
        return x
    else:
        print(y)
        return y


max_number(17, 25)


def min_number(x, y):
    if x < y:
        print(x)
        return x
    else:
        print(y)
        return y


min_number(13, 33)


def module_x(x):
    if x < 0:
        print(x*(-1))
        return x
    else:
        print(x)
        return x


module_x(-3)


def sum_x_y(x, y):
    print(x+y)


sum_x_y(2, 4)


def number_is_positive(x):
    if x < 0:
        print('The number is not positive')
    elif x == 0:
        print('The number is zero')
    else:
        print('The number is positive')


number_is_positive(7)
