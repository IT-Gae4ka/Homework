# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.
from contextlib import suppress
import logging

logging.basicConfig(level=logging.DEBUG)

def suppressing_decorator_fnfe(func):
    def wrapper():
        with suppress(FileNotFoundError):
            func()
    return wrapper

def suppressing_decorator_ve(func):
    def wrapper():
        with suppress(ValueError):
            func()
    return wrapper

@suppressing_decorator_ve
@suppressing_decorator_fnfe
def open_file():
    with open('text.txt', 'w') as f:
        f.write('testing')
        logger = logging.info("This is opening logger")

@suppressing_decorator_ve
@suppressing_decorator_fnfe
def read_file():
    with open('text.txt', 'r') as f:
        print(f.read())
        logger = logging.info('This is reading logger')

open_file()
read_file()
