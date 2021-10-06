# Task 4.1
# Implement a Counter class which optionally accepts the start value and the counter stop value. If the start value is not specified the counter should begin with 0. If the stop value is not specified it should be counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."

# Implement to methods: "increment" and "get"

# If you are familiar with Exception rising use it to display the "Maximal value is reached." message.
# Example:

# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43

# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2

# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43
class Counter:
	def __init__(self, start=0, stop=0):
		self.value = start
		self.stop = stop


	def get(self):
		if self.stop and self.value > self.stop:
			raise Exception("Maximal value is reached.")

		print(self.value)
		
	def increment(self):
		self.value += 1

c = Counter(start=42)
c.increment()
c.get()

c = Counter()
c.increment()
c.get()

c.increment()
c.get()

c = Counter(start=42, stop=43)
c.increment()
c.get()

c.increment()
c.get()
