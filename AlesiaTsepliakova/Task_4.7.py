#Task 4.7
"""
Implement a function foo(List[int]) -> List[int] which, given a list of integers, return a new list such that each element at index i of the new list is the product of all the numbers in the original array except the one at i. Example:

>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
"""

numbers_list = [1, 2, 3, 4, 5]
#numbers_list = [3, 2, 1]
def foo (numbers_list:list)->list:
    product = 1
    j_list = []
    result_list = []
    for i in numbers_list:
        for j in numbers_list:
            if j == i:
                j = 1
                product = j * product
            if j != 1:
                product = j * product
        result_list.append(product)
        product = 1
    return result_list

print(foo(numbers_list))