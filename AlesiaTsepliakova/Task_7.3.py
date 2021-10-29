# Task 7.3
# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
from contextlib import contextmanager
from timeit import timeit
import time

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

    
with open_file('excecution_time_logger.txt', 'w') as f:
    execution_time = str(timeit(stmt="open_file('excecution_time_logger.txt', 'w')", setup='from __main__ import open_file', number = 1))
    f.write(f'Execution time of the code is: {execution_time}')
  

with open_file('excecution_time_logger.txt', 'r') as f:
    print(f.read())


    