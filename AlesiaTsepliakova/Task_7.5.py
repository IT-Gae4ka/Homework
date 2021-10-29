# Task 7.5
# Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors. Custom exceptions must be derived from custom base exception(not Base Exception class).
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

number = int(input("Enter a number: "))

check_number = Check_number(number)
check_number.check_greater_than_2()
check_number.check_even()