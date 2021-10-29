# Task 7.6
# Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close. 
# Use function from Task 5.5 for validating input, 
# handle all exceptions and print user friendly output.
from itertools import permutations

class Check_number():
    def __init__(self, number):
        self.number = number
    
    def check_greater_than_2(self):
        if self.number > 2:
            print (f"Number {self.number} is greater than 2")
        else:
            raise Exception (f"Number {self.number} is less than 2")

    def check_even(self):
        if self.number % 2 == 0:
            print(f"Number {self.number} is even number")
        else:
            raise Exception (f"Number {self.number} is odd number")

    def eratosthenes(self):
        self.primes = list (range(2, self.number+1))
        for i in self.primes:
            j=2
            while i*j<= self.primes[-1]:
                if i*j in self.primes:
                    self.primes.remove(i*j)
                j=j+1
        return self.primes

    def odd_primes(self):
        self.oddprimes = self.eratosthenes()
        self.oddprimes.remove(2)
        return self.oddprimes

    def goldbach(self):
        x, y = 0, 0
        result = 0
        if self.number % 2 == 0:
            self.prime = self.odd_primes()
            while result != self.number:
                for i in range(len(self.prime)):
                    if result == self.number: break  # this line first
                    x = self.prime[i]   # this line after
                    for j in range(len(self.prime)):
                        y = self.prime[j]
                        result = x + y
                        if result == self.number: break 
        return x, y 

number = int(input("Enter a number: "))

check_number = Check_number(number)
check_number.check_greater_than_2()
check_number.check_even()
print(check_number.goldbach())


