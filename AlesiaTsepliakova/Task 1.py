
### Task 1.1
#Write a Python program to calculate the length of a string without using the `len` function.

a = "I love Python!"

letters_number = 0
for i in a:
    letters_number = letters_number + 1

print(letters_number)

if letters_number == len(a):
    print("The task is solved!")

