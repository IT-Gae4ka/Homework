#Task 4.10
"""
Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.

print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


number = 5

def generate_squares(number:int)-> dict:
	
	if isinstance(number, int):
		number_dict = {}
		for i in range (1, number+1):
			j = i**2
			number_dict[i]=j
		return number_dict		
	else:
		print("Please, write integer!")
	
print(generate_squares(number))