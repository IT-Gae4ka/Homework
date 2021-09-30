# Task 4.2
from collections import Counter
import collections

# Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.

# def most_common_words(filepath, number_of_words=3):
#     pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


# words = "Lorem ipsum suspendisse nostra ullamcorper diam donec etiam nulla sagittis est aliquam, dictum aliquet luctus risus est habitant suspendisse luctus id inceptos lectus, aenean donec maecenas donec aenean fringilla vitae fermentum venenatis enim ultrices per etiam ut aenean odio. Habitasse ad sollicitudin arcu senectus enim etiam platea quisque purus odio sociosqu maecenas habitant,"
number_of_words = 3

filepath = 'D:\Alesia\Python\epam\HOMEWORK\Homework\AlesiaTsepliakova'

 

number_of_words = 3

def most_common_words(filepath,number_of_words):
    with open('lorem_ipsum.txt', 'r') as f:
        file_string_raw=f.read()
        file_string = file_string_raw.lower()
        words = file_string.split()
        wordCount = Counter(words)
        d = collections.OrderedDict(wordCount)
        common_words = []
        for w in sorted(d, key=d.get, reverse=True):
            common_words.append(w)    
        return common_words[0:number_of_words]
        
print(most_common_words(filepath, number_of_words))
