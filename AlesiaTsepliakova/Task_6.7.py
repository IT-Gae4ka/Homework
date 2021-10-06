# Task 4.7
# Implement a class Money to represent value and currency. You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction). Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }
# Example:

# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# >>543.21 EUR

# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# >>123.45 BYN
# Have a look at @functools.total_ordering

from functools import total_ordering


class Money():

    exchange_rate_byn = {
    "EUR": 2.90,
    "BYN": 1,
    "JPY": 0.022,
    "USD": 2.5}

    def __init__(self, amount, abbreviation="USD"):
        self.amount = amount
        self.abbreviation = abbreviation
     
    def convert_into_byn(self):
        self.converted_into_byn = self.amount*self.exchange_rate_byn[self.abbreviation]
        return self.converted_into_byn

    def __add__(self, other):
        if isinstance(other,(int, float)):
            return self.convert_into_byn() + other
        if isinstance(other,(Money)):
            return self.convert_into_byn() + other.convert_into_byn()

    def __radd__(self, other):
        return self + other        
    
    def __sub__(self, other):
        if isinstance(other,(int, float)):
            return self.convert_into_byn() - other
        if isinstance(other,(Money)):
            return self.convert_into_byn() - other.convert_into_byn()

    def __rsub__(self, other):
            return self - other

    def __mul__(self, other):
        if isinstance(other,(int, float)):
            return self.convert_into_byn() * other
        if isinstance(other,(Money)):
            return self.convert_into_byn() * other.convert_into_byn()
    
    def __truediv__(self, other):
        if isinstance(other,(int, float)):
            return self.convert_into_byn() / other
        if isinstance(other,(Money)):
            return self.convert_into_byn() / other.convert_into_byn()
        raise NotImplemented

    def __rtruediv__(self, other):
        return self / other
    
    def __eq__(self, other):
        return isinstance(self, Money) and isinstance(other, Money) \
        and self.convert_into_byn() == other.convert_into_byn()

    def __lt__(self, other):
        return self.convert_into_byn()<other.convert_into_byn()

    def __le__(self,other):
        return self.convert_into_byn()<=other.convert_into_byn()


x = Money(10, "BYN")
y = Money(11) # defined default value in “USD”
z = Money(12.34, "EUR")
xx = Money(10, "BYN")

print (x+y-z)
print(x+2)
print(x+y+z)
print(z*x/y)
print (y+z/2)
print (y>z)
print (y<z)
print (y!=z)
print (z==y)
lst=[x,y,z]
print(sum (lst))

