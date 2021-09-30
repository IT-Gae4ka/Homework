# Task 4.4
# Look through file modules/legb.py.

# Find a way to call inner_function without moving it from inside of enclosed_function.
# 2.1) Modify ONE LINE in inner_function to make it print variable 'a' from global scope.

# 2.2) Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.


# файл modules / legb.py.

# Найдите способ вызвать inner_function, не перемещая его изнутри enclosed_function.
# 2.1) Измените ОДНУ СТРОКУ в inner_function, чтобы она печатала переменную 'a' из глобальной области видимости.

# 2.2) Измените ОДНУ СТРОКУ в inner_function, чтобы она печатала переменную 'a', включающую функцию формы.


a = "I am global variable!"


def enclosing_funcion_global():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function

f_global = enclosing_funcion_global()
f_global()



def enclosing_funcion_nonlocal():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function

f_nonlocal = enclosing_funcion_nonlocal()
f_nonlocal()