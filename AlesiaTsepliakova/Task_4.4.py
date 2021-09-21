#Task 4.4
"""
Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by indexes specified in indexes. Wrong indexes must be ignored. Examples:

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
"""
s = "pythoniscool,isn'tit?"
list_int = [6, 8, 12, 13, 18]
#s="no luck"
#list_int = [42]


def split_by_index(s:str,indexes:list)->list:
	if isinstance(s,str) and isinstance(indexes,list):
		length = len(s)
		word_list =[]
		word_str = ""
		result_list = []
		counter = 0
		for i in range(0,length): 
			word_list.append(s[i])
			counter = counter+1
			if i+1 in list_int or counter==length:
				word_str ="".join(word_list)
				result_list.append(word_str)
				word_list = []
				word_str = ""
	else:
		print("Please write s as a string, and indexes as a list with integers inside it.")
	return result_list


print(split_by_index(s, list_int))


