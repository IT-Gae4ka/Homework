# Task 7.10
# Implement a generator which will generate odd numbers endlessly. Example:

# gen = endless_generator()
# while True:
#     print(next(gen))
# >>> 1 3 5 7 ... 128736187263 128736187265 ...


def endless_odd_generator():
	odd = 1
	while True:
		yield odd
		odd += 2


gen = endless_odd_generator()
while True:
	print(next(gen))