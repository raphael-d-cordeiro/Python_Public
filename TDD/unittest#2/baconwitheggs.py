"""
Steps
1 - Receive one number integer
2 - Know if the number is multiple by 3 and 5:
    return Bacon with eggs
3 - know if the number is multiple by 3 only:
    return Bacon
4 - know if the number is multiple by 5 only:
    return Eggs
5 - Know if the number is not multiple by 3 and 5:
    return Hungry
"""


def bacon_with_eggs(i):
    assert isinstance(i, (int,)), 'i <- is not integer'

    if (i % 3 == 0) and (i % 5 == 0):
        return 'Bacon with eggs'
