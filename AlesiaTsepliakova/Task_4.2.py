#Task 4.2
"""

Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited. To check your implementation you can use strings from here.
"""
a = "Hannah"
def check_palindrome(a:str)-> bool:
	text_list = []
	a = a.lower()
	if isinstance(a, str):
		for i in a:
			text_list.append(i)
		length = len(text_list)	
		for i in range (0,length):
			if text_list[i] == text_list[length-1-i]:
				palindrome = True
			else:
				palindrome = False
				break
	else:
		print("Please write a string!")
	return palindrome 	

print(f"A is a palindrome: {check_palindrome(a)}")

