# Task 7.11
# Implement a generator which will geterate Fibonacci numbers endlessly. Example:

# gen = endless_fib_generator()
# while True:
#     print(next(gen))
# >>> 1 1 2 3 5 8 13 ...

def endless_fib_generator():
	#create endless Fibonachi generator
	start = 1
	next_num = 1
	while True:
		yield start
		start, next_num = next_num, start+next_num
		
	
gen = endless_fib_generator()
while True:
	print(next(gen))
