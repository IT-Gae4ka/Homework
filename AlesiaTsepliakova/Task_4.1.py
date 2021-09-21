#Task 4.1
#Implement a function which receives a string and replaces all " symbols with ' and vise versa.

a = "I 'love' autumn!"

def change_quotes(a:str):
	text = "str"
	text_list = []
	if isinstance(a,str):
		for i in a:
			if i == '"':
				i = "'"
			if i == "'":
				i = '"'
			text_list.append(i)
		text="".join(text_list)
	else:
		print("Please input a string.")	
	return text


print(change_quotes(a))