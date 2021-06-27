def multiply_num(x, y):

    assert isinstance(x, (int, float)), 'x needs to be an integer or float'
    assert isinstance(y, (int, float)), 'y needs to be an integer or float'
    return x * y


def subtraction_num(x, y):

    assert isinstance(x, (int, float)), 'x needs to be an integer or float'
    assert isinstance(y, (int, float)), 'y needs to be an integer or float'
    return x - y


if __name__ == '__main__':
    print(multiply_num(2, 3))
