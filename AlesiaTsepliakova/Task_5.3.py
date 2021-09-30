# Task 5.3
# File data/students.csv stores information about students in CSV format. This file contains the student’s names, age and average mark.

# 1. Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5):
#     pass

# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# 2. Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age. Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27


import csv

def get_top_performers(filepath:str, number_of_top_students=5):
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        students = [x for x in csv_reader]
        students_by_performance = sorted(students[1:], key=lambda x: float(x[2]), reverse=True)
        
        top_performers = []
        for x in students_by_performance[0:number_of_top_students]:
            top_performers.append(x[0])
    
    return top_performers


def get_students_sorted_by_age(filepath:str):
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        students = [x for x in csv_reader]
        students_by_age = sorted(students[1:], key=lambda x: int(x[1]), reverse=True)
    return students_by_age

def write_sorted_students(sorted_students:list):
    with open('new.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)

        for student in sorted_students:
            writer.writerow(student)

    

students_by_age = get_students_sorted_by_age('students.csv')
students_by_performance = get_top_performers('students.csv')
print(students_by_performance)
write_sorted_students(students_by_age)


