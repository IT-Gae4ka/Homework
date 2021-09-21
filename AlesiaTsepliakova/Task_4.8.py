"""
Task 4.8
Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements. Pairs should be formed as in the example. If there is only one element in the list return None instead. Example:

>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
"""

#lst = [1, 2, 3, 8, 9]
#lst = ['need', 'to', 'sleep', 'more']
lst = [1]



def get_pairs(lst:list)->list:
	pairs_list = []
	long_list = []
	length = len(lst)
	if length > 1:
		for i in range (0, length-1):
			pairs_list.append(lst[i])
			pairs_list.append(lst[i+1])
			pairs_tuple = tuple(pairs_list)
			long_list.append(pairs_tuple)
			pairs_list = []
		return long_list
	else:
		return None
		
print(get_pairs(lst))

