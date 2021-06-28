"""
https://docs.python.org/3/library/typing.html
pip install mypy
pip install flake8
"""

from typing import Iterable, List, NewType, Sequence, Union
from typing import Tuple, Dict, Any, Callable

# Primitives
num: int = 10
num_float: float = 10.5
boolean: bool = False
string: str = 'Raphael Cordeiro'

# Sequences
seq_list: List[int] = [1, 2, 3]
seq_list_str_int: List[Union[int, str]] = [1, 2, 3, 'Raphael']
seq_tuple: Tuple[int, int, int, str] = (1, 2, 3, 'Raphael')
seq_tuple2: Tuple = (1, 2, 3, 'Raphael')

# Dictionaries and sets
# Alias typehint
MyDict = Dict[str, Union[str, Any]]

dict_person: Dict[str, Union[str, int]] = {
    'name': 'Raphael',
    'lastname': 'Cordeiro',
    'age': 31
}
dict_person2: MyDict = {
    'name': 'Raphael',
    'lastname': 'Cordeiro',
    'age': 31
}

# New Type
UserId = NewType('UserId', int)
user_id = UserId(1)


# Functions and Class
def return_function(function: Callable[[int, int], int]) -> Callable:
    return function


def sum_func(x: int, y: int) -> int:
    return x + y


print(return_function(sum_func)(10, 20))


class Person:
    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age

    def say_something(self) -> None:
        print(f'{self.name} {self.lastname} is talking to...')


def iterate(sequence: Sequence[int]):
    return [x * 2 for x in sequence]


def iterate2(sequence: Iterable[int]):
    return [x * 2 for x in sequence]


print(iterate([1, 2, 3]))
