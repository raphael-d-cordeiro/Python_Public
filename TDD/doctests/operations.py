def multiply_num(x, y):
    """
    Multiply x and y
    >>> multiply_num(2, 10)
    20
    >>> multiply_num(-10, 3)
    -30
    >>> multiply_num('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be an integer or float
    """

    assert isinstance(x, (int, float)), 'x needs to be an integer or float'
    assert isinstance(y, (int, float)), 'y needs to be an integer or float'
    return x * y


def subtraction(x, y):
    """
    Subtraction x and y
    >>> subtraction(10, 5)
    5

    >>> subtraction('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be an integer or float
    """
    assert isinstance(x, (int, float)), 'x needs to be an integer or float'
    assert isinstance(y, (int, float)), 'y needs to be an integer or float'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
