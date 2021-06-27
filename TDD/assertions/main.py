# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/unittest.html

from calculator import sum_num

if __name__ == '__main__':
    try:
        print(sum_num('10', 11))
    except AssertionError as e:
        print(f'Invalid Operation: {e}')

print(sum_num(50, 50))
