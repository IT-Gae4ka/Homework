"""
### Task 1.5
Write a Python program to print all unique values of all dictionaries in a list.
Examples:
```
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
```
"""
#1.Loops variant of solving:

"""
dicts_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
value_list = []
unique_values = set()

for i in dicts_list:
    temp_value = i.values()
    value_list.extend(temp_value) 
    unique_values = set(value_list)

print(f"Value_list: {unique_values}")

"""
#2.Classes variant of solving:

"""
dicts_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

class UniqueValues():
    value_list = []
    unique_values = set()

    def __init__(self, dicts_list):
        self.dicts_list = dicts_list

    def get_unique_values(self):
        for i in self.dicts_list:
            self.temp_value = i.values()
            self.value_list.extend(self.temp_value) 
            self.unique_values = set(self.value_list)
        return self.unique_values

unique_values = UniqueValues(dicts_list)
unique_values.get_unique_values()
print(unique_values.get_unique_values())
"""