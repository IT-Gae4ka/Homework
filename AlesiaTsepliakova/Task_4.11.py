"""
Task 4.11
Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary. Dict values ​​should be summarized in case of identical keys

def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
>>> {'a': 300, 'b': 200, 'c': 300}


print(combine_dicts(dict_1, dict_2, dict_3)
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*args):
    dicts_list = list(args)
    dict_sum = {}
    for dict_1 in dicts_list:
        for key in dict_1:
            if key in dict_sum:
                dict_sum[key]=dict_sum[key]+dict_1[key]
            else:
                dict_sum.update({key:dict_1[key]})
    return dict_sum
    
  
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
