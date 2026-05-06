from typing import List, Tuple, Union

n : int = 5 # When you type n. it will give all int functions

name : str = "Patu" # When you type name. it will give all string functions

def sum(a: int, b: int) -> int:
    return a+b

sum(4,7)

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
Scores: dict[str, int] = {"Alice": 90, "Bob":95}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 #Also valid