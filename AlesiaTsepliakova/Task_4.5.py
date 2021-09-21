#Task 4.5
"""
Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits. Example:

>>> split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
"""

num = 87178291199


def get_digits(num:int) -> tuple:
	if isinstance(num,int):
		num_string = str(num)
		print(f"num_string:{num_string}")
		num_list = []
		for i in num_string:
			num_list.append(i)
		num_tuple=tuple(num_list)
	else:
		print("Please, write integer")	
	return num_tuple

print(get_digits(num))