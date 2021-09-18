### Task 1.6
"""
Write a Python program to convert a given tuple of positive integers into an integer. 
Examples:
```
Input: (1, 2, 3, 4)
Output: 1234
```
"""
#1.Loop variant of solving:

"""
given_tuple = (1,2,3,4)
values_list = []

for i in given_tuple:
    string_values = str(i)
    values_list.extend(string_values)
print(values_list)

print(''.join(values_list))
"""

#2.Classes variant of solving:
"""
given_tuple = (1,2,3,4)

class StringJoining():
    values_list = []
    
    def __init__(self,given_tuple):
        self.given_tuple = given_tuple

    def join_strings(self):
        for i in self.given_tuple:
            self.string_values = str(i)
            self.values_list.extend(self.string_values)
            self.joined_strings = ''.join(self.values_list)
        return self.joined_strings

joined_strings = StringJoining(given_tuple)
print(joined_strings.join_strings())
"""

### Task 1.6
"""
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
```
Input:
a = 2
b = 4
c = 3
d = 7

Output:
    3   4   5   6   7   
2   6   8   10  12  14  
3   9   12  15  18  21  
4   12  16  20  24  28
```
"""

#1. Loops variant of solving:

"""
a = 2
b = 4
c = 3
d = 7

temp_row = []
row =[]

print ("  ",' '.join([str(i) for i in range(c,d+1)]))
for i in range (a,b+1):
    for j in range(c, d+1): 
        temp = i*j
        temp_row.append(temp)
    print (i,' '.join([str(k) for k in temp_row]))
    temp_row = []
    
"""

#2.Functions variant of solving:
"""
a = 2
b = 4
c = 3   
d = 7


def multiplicate(a:int, b:int, c:int, d:int):
    if isinstance (a, int) and isinstance (b, int) and isinstance (c, int) and isinstance (d, int):
        if a<=b and c<= d:
            temp_row = []
            row =[]

            print ("  ",' '.join([str(i) for i in range(c,d+1)]))
            for i in range (a,b+1):
                for j in range(c, d+1): 
                    temp = i*j
                    temp_row.append(temp)
                print (i,' '.join([str(k) for k in temp_row]))
                temp_row = []
        else:
            print('Please enter values, where a>b and c>d')
    else:
        print('Please enter an integer')

painting = multiplicate(a,b,c,d)

"""

    