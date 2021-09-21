#Task 4.6
"""
Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string. The word can contain any symbols except whitespaces ( , \n, \t and so on). If there are multiple longest words in the string with a same length return the word that occures first. Example:
#NB! In ASCII, whitespace characters are space (' '), tab ('\t'), carriage return ('\r'), newline ('\n'), vertical tab ('\v') and formfeed ('\f').
>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
"""
s = "Python is simple and effective!"
#s = "Any pythonista like namespaces a lot."

whitespace_list = [' ', '\t', '\r', '\n', '\v','\f']

def get_longest_word(s:str) -> str:
	if isinstance(s,str):
		longest_word = ""
		word_list = []
		word = ""
		counter = 0
		for i in s:
			counter = counter+1
			if i not in whitespace_list:
				word_list.append(i)
			if i in whitespace_list or counter == len(s):
				word = "".join(word_list)
				if len(longest_word)<len(word):
					longest_word=word
					word = ""
					word_list = []
				if len(longest_word) >= len(word):
					word = ""
					word_list = []
	else:
		print("Please, write a string")
	return longest_word


print(get_longest_word(s))
