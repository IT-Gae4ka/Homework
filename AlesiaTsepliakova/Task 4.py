
### Task 1.4
#Write a Python program to sort a dictionary by key.
#1. Loops variant of solving:
"""
unsorted_dict = {4:"Mars",5:"Jupiter",1:"Mercury",2:"Venus",6:"Saturn",7:"Uranus",3:"Earth",9:"Pluto",8:"Neptune"}
sorted_dict = {}
key_list = list(unsorted_dict.keys())
check = True
print(f"Unsorted key_list: {key_list}")

if check == True:
    for i in range(0,len(key_list)):
        for j in range(0,len(key_list)):
            if key_list[i]< key_list[j]:
                a=key_list[j]
                key_list[j]=key_list[i]
                key_list[i]=a
                check = True
            if key_list[i]>=key_list[j]:
                check = True
print(f"Sorted key_list: {key_list}")

for i in key_list:
    sorted_dict[i]=unsorted_dict[i]

print(f"Sorted_dict: {sorted_dict}")

"""

#2 Classes variant of solving:
"""
unsorted_dict = {4:"Mars",5:"Jupiter",1:"Mercury",2:"Venus",6:"Saturn",7:"Uranus",3:"Earth",9:"Pluto",8:"Neptune"}

class SortedDict():
    sorted_dict = {}
    key_list = list(unsorted_dict.keys())
    check = True

    def __init__(self, unsorted_dict):
        self.unsorted_dict = unsorted_dict

    def sort_key_list(self):
        if self.check == True:
            for i in range(0,len(self.key_list)):
                for j in range(0,len(self.key_list)):
                    if self.key_list[i]< self.key_list[j]:
                        self.a=self.key_list[j]
                        self.key_list[j]=self.key_list[i]
                        self.key_list[i]=self.a
                        self.check = True
                    if self.key_list[i] >= self.key_list[j]:
                        self.check = True
            self.sorted_key_list = self.key_list
        return self.sorted_key_list 

    def create_sorted_dict(self):
        self.sorted_key_list = self.sort_key_list()
        for i in self.sorted_key_list:
            self.sorted_dict[i]=self.unsorted_dict[i]
        return self.sorted_dict

sorted_dict = SortedDict(unsorted_dict)
print(sorted_dict.create_sorted_dict())
"""