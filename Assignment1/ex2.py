from typing import Callable
###
list1=[1, 2, 3]
list2=[3, 4, 5]

# First we parse it to sets to be able to use '&' for intersection and parse it back to lists to conform with the exercise
print(f"{list(set(list1) & set(list2)) = }")


# Because I wanted to exercise currying I made a function that takes an operand and returns a function based on that operand
# including the sought after intersection.

def set_operation(operand) -> Callable:
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

list_intersection = set_operation('intersection')
# example of the list_intersection function
print(f"Common elements of list1 and list2: {list_intersection(list1, list2)} ")
###