# Task 7.2
# Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.
from contextlib import contextmanager

modes = ['r', 'w', 'a', 'r+']

@contextmanager
def open_file(filename, mode):

    try:
        file = open(filename, mode)
        yield file
    except ValueError as value_e:
        print(f"Please  the right mode in your input!\n Your error is: {value_e}")            
    except FileNotFoundError as not_found_e:
        print(f"Please write the name of the file in your input!\n Your error is: {not_found_e}")
    finally:
        file.close()

    


with open_file('text', "w") as file:
    file.write("hello")

with open_file("text.txt", "r") as file:
    print(file.read())
    