"""
Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

characters that appear in all strings

characters that appear in at least one string

characters that appear at least in two strings

characters of alphabet, that were not used in any string

Note: use string.ascii_lowercase for list of alphabet letters

test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}

"""
test_strings = ["hello", "world", "python", ]

def test_1_1(*test_strings):
	test_strings = list(test_strings)
	result = set()
	for word in test_strings:
		letters = list(word)
		for let in letters:
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					pass
				else:
					break 
			else:
				result.add(let)
	return result

def test_1_2(*test_strings):
	test_strings = list(test_strings)
	result = set()
	for word in test_strings:
		letters = list(word)
		for let in letters:
			result.add(let)
	return result

def test_1_3(*test_strings):
	test_strings = list(test_strings)
	result=set()
	for word in test_strings:
		letters = list(word)
		for let in letters:
			count_for_letter = 0
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					count_for_letter+=1
			if count_for_letter>=2:
				result.add(let)
	return result

def test_1_4(*test_strings):
	test_strings = list(test_strings)
	alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	result = set()
	for letter in alphabet:
		for word in test_strings:
			if letter not in word.lower():
				pass
			else:
				break
		else:
			result.add(letter)
	return result

print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))		
