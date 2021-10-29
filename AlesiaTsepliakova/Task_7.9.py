# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration. If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
# Note: Do not use function range() at all Example:

# er1 = EvenRange(7,11)
# next(er1)
# >>> 8
# next(er1)
# >>> 10
# next(er1)
# >>> "Out of numbers!"
# next(er1)
# >>> "Out of numbers!"
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)
# >>> 4 6 8 10 12 "Out of numbers!"



class EvenRange():

    is_by_loop = False

    def __init__(self, start, end):
        if isinstance(start, int) and isinstance(end, int):
            #checks input for INTEGER
            self.item = start if start%2==0 else start+1
            self.end = end
        else:
            print("Start or End is not INTEGER")
            self.item=0
            self.end=0


    def __iter__(self):
        """
        is called in the loop 'for in'
        """
        self.is_by_loop = True
        return self



    def __next__(self):
        if self.item < self.end:
            result = self.item
            self.item += 2
            return result 
        if self.is_by_loop:
            print("Out of number!")
            raise StopIteration
        else:
            return "Out of number!"


# er1 = EvenRange(5, 9)
# print(next(er1))
# print(next(er1))
# print(next(er1))
# print(next(er1))

er2 = EvenRange(-3, 10)
for item in er2:
    print(item)



