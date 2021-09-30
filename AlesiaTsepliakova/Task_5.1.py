# # Task 4.1
# # Open file data/unsorted_names.txt in data folder.
# Sort the names and write them to a new file called sorted_names.txt. 
# Each name should start with a new line as in the following example:

# # Adele
# # Adrienne
# # ...
# # Willodean
# # Xavier

def sort_words(words):
    words.sort()
    column_temp = []
    for i in words:
        i = i + '\n'
        column_temp.append(i)
        result_column = ''.join(column_temp)
    return result_column


with open('unsorted_names.txt', 'r') as unsorted_names_file:
    words=unsorted_names_file.readlines()
    sorted_words = sort_words(words)
    sorted_names = open('sorted_names.txt','w')
    sorted_names.write(sorted_words)
    sorted_names.close()

sorted_names = open("sorted_names.txt", "r")
print(sorted_names.read())