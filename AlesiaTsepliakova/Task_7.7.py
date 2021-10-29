# Task 7.7
# Implement your custom collection called MyNumberCollection.
# It should be able to contain only numbers. 
# It should NOT inherit any other collections.
# If user tries to add a string or any non numerical object there, exception TypeError should be raised. 
# Method init sholud be able to take either start,end,step arguments, 
# where start - first number of collection, end - last number of collection 
# or some ordered iterable collection (see the example). Implement following functionality:

# appending new element to the end of collection
# concatenating collections together using +
# when element is addressed by index(using []), user should get square of the addressed element.
# when iterated using cycle for, elements should be given normally
# user should be able to print whole collection as if it was list. Example:
# col1 = MyNumberCollection(0, 5, 2)
# print(col1)
# >>> [0, 2, 4, 5]
# col2 = MyNumberCollection((1,2,3,4,5))
# print(col2)
# >>> [1, 2, 3, 4, 5]
# col3 = MyNumberCollection((1,2,3,"4",5))
# >>> TypeError: MyNumberCollection supports only numbers!
# col1.append(7)
# print(col1)
# >>> [0, 2, 4, 5, 7]
# col2.append("string")
# >>> TypeError: 'string' - object is not a number!
# print(col1 + col2)
# >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
# print(col1)
# >>> [0, 2, 4, 5, 7]
# print(col2)
# >>> [1, 2, 3, 4, 5]
# print(col2[4])
# >>> 25
# for item in col1:
#     print(item)
# >>> 0 2 4 5 7

from typing import Iterable


class MyNumberCollection:
    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], Iterable):
            for i in args[0]:
                if not isinstance(i, int):
                    raise TypeError("MyNumberCollection supports only numbers!")
            self.items = list(args[0])
        else:
            start, stop, step = args
            if (isinstance(start, int)
                and isinstance(stop, int)
                and isinstance(step, (int, None))):
                step = step or 1
                self.items = [i for i in range(start, stop, step)]

    def __iter__(self):
        return iter(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} - object is not a number!")
        self.items.append(value)

    def __add__(self, other):
        if not isinstance(other, MyNumberCollection):
            raise TypeError(f"{other} - object is not a MyNumberCollection!")
        result = self.items + other.items
        return MyNumberCollection(result)

    def __getitem__(self, index):
        return self.items[index] ** 2

col1 = MyNumberCollection(0, 5, 2)
print(col1)
col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)
# col3 = MyNumberCollection((1, 2, 3, "4", 5))
col1.append(7)
print(col1)
# col2.append("string")
print(col1 + col2)
print(col1)
print(col2)
print(col2[4])
for i in col1:
    print(i)