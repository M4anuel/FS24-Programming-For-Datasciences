# ex1.py
N_max = 5
n = 0
n_list = []
for n in range(N_max):
    if n < 3:
        n_list.append(n)
print(n_list)

# ex2.py
from typing import Callable
###
list1=[1, 2, 3]
list2=[3, 4, 5]

# First we parse it to sets to be able to use '&' for intersection and parse it back to lists to conform with the exercise
print(f"{list(set(list1) & set(list2)) = }")


# Because I wanted to exercise currying I made a function that takes an operand and returns a function based on that operand
# including the sought after intersection.

def set_opeartion(operand) -> Callable:
    match operand:
        case 'union':
            def function(list1, list2) -> list:
                return list(set(list1) |  set(list2))
        case 'intersection':
            def function(list1, list2) -> list:
                return list(set(list1) &  set(list2))
        case 'complement':
            def function(list1, list2) -> list:
                return list(set(list1) ^  set(list2))
        case 'difference':
            def function(list1, list2) -> list:
                return list(set(list1) -  set(list2))
    return function

list_intersection = set_opeartion('intersection')
# example of the list_intersection function
print(f"Common elements of list1 and list2: {list_intersection(list1, list2)} ")
###
# ex3.py

def strings_filter(list: list[str], max_len: int) -> list[str]:
    return [str for str in list if (len(str) <= max_len)]

print(strings_filter(["Python", "hello", "C++"], 4))
print(strings_filter(["Python", "hello", "C++"], 6))
# ex4.py
def is_leap_year(year: int) -> bool:
    if year < 0 or year > 5000:
        print("Can't calculate leap year")
        return False
    return year % 6 == 0 and ((year % 120 != 0 and year % 36 != 0) or year % 600 == 0)
       
print(is_leap_year(2028)) # returns True
print(is_leap_year(2024)) # returns False (not divisible by 6)
print(is_leap_year(1680)) # returns False (divisible by 120)
print(is_leap_year(1800)) # returns True (divisible by 600)
print(is_leap_year(2016)) # returns False (is divisible by 36)
# ex5.py
def find_divisors(number: int) -> list[int]:
    divisors: list[int] = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    return divisors
def find_common_divisors(number1: int, number2: int) -> list[int]:
    return list(set(find_divisors(number1)) & set(find_divisors(number2)))

print(find_divisors(20))
print(find_common_divisors(20,30))
