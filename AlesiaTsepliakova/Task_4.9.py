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
	list_in = []
	for word in test_strings:
		letters = list(word)
		for let in letters:
			counter = 0
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					counter = counter+1
					if counter == len(test_strings):
						list_in.append(let)
				else:
					break
	return (set(list_in))

def test_1_2(*test_strings):
	test_strings = list(test_strings)
	result = set()
	list_in = []
	for word in test_strings:
		letters = list(word)
		for let in letters:
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					list_in.append(let)
				else:
					pass				

	return set(list_in)

def test_1_3(*test_strings):
	test_strings = list(test_strings)
	result = set()
	list_in = []
	for word in test_strings:
		letters = list(word)
		for let in letters:
			counter = 0
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					counter = counter+1
					if counter >= 2:
						list_in.append(let)
				else:
					pass
	return (set(list_in))


def test_1_4(*test_strings):
	test_strings = list(test_strings)
	result = set()
	list_in = []
	alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	for word in test_strings:
		letters = list(word)
		for let in letters:
			for i in range(len(test_strings)):
				if let in test_strings[i]:
					list_in.append(let)
				else:
					pass
	result = set(alphabet).difference(set(list_in))
	return result

print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))		
