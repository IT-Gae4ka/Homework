#Task 4.3
#Implement a function which works the same as str.split method (without using str.split itself, ofcourse).


a = "I want to be a programmer!"
b = " "
maxsplit = 2   
def split_string(a:str, b:str, maxsplit:int)->list:
    if isinstance(a,str):
        if isinstance(maxsplit,int):
            text_list = []  
            word_list = []
            result_list =[]
            word_str = " "
            length = len(a)
            counter = -1
            count_b = 0
            for i in a:
                counter = counter+1
                if i != b:
                    word_list.append(i)
                if i == b or counter == length:
                    if count_b < maxsplit:    
                        word_str ="".join(word_list)
                        text_list.append(word_str)
                        result_list.append(word_str)
                        word_str = " "
                        word_list = []
                        count_b = count_b+1
                    else:
                        word_list.append(i)
            word_str ="".join(word_list)
            result_list.append(word_str)
        else:
            print("Please, write an integer!")
    else:
            print("Please, write a string!")
    return result_list

print(split_string(a,b,maxsplit))




