from typing import Callable

# A)
list1=[1, 2, 3]
list2=[3, 4, 5]
# list1 and list2 references the same object. Therefore list1 and list2 have the same memory location. A change of list1 or list2 leads to a change to the object.
# Command to see the memory location of list1
print(id(list1))
# Command to see the memory location of list2
print(id(list2))

# B)
lst = [1, 2, 3] #Lists are mutable and can perform operations such as insertion and deletion. 
tpl = (1, 2, 3) #Tuples are immutable.Therefore we can't change a tuple after it is created.

# First we parse it to sets to be able to use '&' for intersection and parse it back to a list to conform with the exercise
print(f"{list(set(list1) & set(list2)) = }")


# C)
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