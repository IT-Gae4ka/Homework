# Task 7.8
# Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through. Example:

# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25
class MySquareIterator:
    def __iter__(self):
        return self

    def __init__(self, lst):
        self.lst = lst
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.lst):

            position = self.lst[self.counter]
            self.counter += 1

            if isinstance(position, int) or isinstance(position, float):
                sqr_position=position**2
                return sqr_position
            else:
                print(f" \'the \'{position}\' is not number\' and does not have square")
                return position
        else:
            raise StopIteration



lst = [1, 2, 3, 4, 5, 9]
itr = MySquareIterator(lst)
for item in itr:
    print(item)

