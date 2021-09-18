
"""
### Task 1.2
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
Examples:
```
Input: 'Oh, it is python' 
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
```
"""
##1.Loops variant of solving:
"""
text ='Oh, it is python'
lower_case_text = text.lower()

empty_set = set()
counting_letters = {}


for i in lower_case_text:
    empty_set.add(i)
    letters_set = empty_set

for i in lower_case_text:
    counting_letters[i] = 0

for i in lower_case_text:
    if i in letters_set:
        counting_letters[i] = counting_letters[i]+1
        
print(f"In the text:'{text}' there are:{counting_letters}")
"""
#2.Functions variant of solving:
"""

text ='Oh, it is python'

def create_letters_set(text):
    lower_case_text = text.lower()
    empty_set = set()
    
    for i in lower_case_text:
        empty_set.add(i)
        letters_set = empty_set
    return letters_set

def count_letters_in_text(text):
        counting_letters = {}
        lower_case_text = text.lower()
        for i in lower_case_text:
            counting_letters[i] = 0
        
        letters_set = create_letters_set(text)
        for i in lower_case_text:
            if i in letters_set:
                counting_letters[i] = counting_letters[i]+1
        return counting_letters

counting_letters = count_letters_in_text(text)

print(f"In the text:'{text}' there are:{counting_letters}")
"""

#3. Class variant of solving:
"""

text ='Oh, it is python'

class LetterCounter():
    empty_set = set()
    counting_letters = {}

    def __init__(self, text):
        self.lower_case_text = text.lower()

    def create_letters_set(self):
        for i in self.lower_case_text:
            self.empty_set.add(i)
        letters_set = self.empty_set
        return letters_set

    def count_letters_in_text(self):
        for i in self.lower_case_text:
            self.counting_letters[i] = 0
        
        letters_set = self.create_letters_set()
        for i in self.lower_case_text:
            if i in letters_set:
                self.counting_letters[i] = self.counting_letters[i]+1
        return self.counting_letters

count = LetterCounter(text)
counting_letters = count.count_letters_in_text()
print(f"In the text:'{text}' \nthere are:\n{counting_letters}")
"""