# Task 4.5
# Implement a decorator remember_result which remembers last result of function it decorates and prints it before next call.

# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result

# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'" 
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'" 
# >>> "Current result = '12'"


last_res = None
def remember_result(func):
    last_res = None
    def wrapper(*args):
        nonlocal last_res
        print(f"Last result = {last_res}")
        last_res = func(*args)      
    return wrapper

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
sum_list("abc", "cde")
#sum_list(3, 4, 5)
