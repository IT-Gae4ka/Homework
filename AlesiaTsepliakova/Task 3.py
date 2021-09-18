"""
### Task 1.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:
```
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
```
"""
"""
list = ['red', 'white', 'black', 'red', 'green', 'black']
print(set(list))
"""


"""
### Task 1.3
Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
```
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
"""
"""
# 1. Loops variant of solving:

number = int(input("Please, write a number!"))
divisors_list=[]

for i in range(1,number):
    remainder = number % i
    if remainder == 0:
        divisors_list.append(i)
    else:
        pass
print(f"The number: {number} can be divided without remainder by: \n {divisors_list}")

"""
# 2. Class variant of solving:

"""
number = int(input("Please, write a number!"))

class Divisor():
    divisors_list = []

    def __init__(self, number):
        self.number = number

    def create_divisors_list(self):
        for i in range(1,self.number):
            self.remainder = self.number % i
            if self.remainder == 0:
                self.divisors_list.append(i)
            else:
                pass
        return self.divisors_list
            
divisor = Divisor(number)
divisors_list = divisor.create_divisors_list()
print(f"The number: {number} can be divided without remainder by: \n {divisors_list}")

"""