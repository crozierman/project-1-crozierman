# Author:  Mike Crozier
# GitHub username: Crozierman
# Date: 01/08/2024
# Description: A program that recieves lists of student names and grades and returns the mean, median, and mode of
# students in that list
import statistics

class Student:
    # represents students each with a name and a grade
    def __init__(self, name, grade ):
        # creates a new student with a name and a grade
        self._name = name
        # assigns object "name" to self._name input
        self._grade = grade
        # assigns object "grade" to self._grade input

    def get_grade (self):
        # creates method get_grade with input self
        return self._grade
        # returns just grade portion of self

def basic_stats (student_list_in):
    # creates method with list input
    grade = [Student._grade for Student in student_list_in]
    # assigns object grade to grades only from list student passed through Student class
    mean = statistics.mean(grade)
    # Uses statistics module to fine mean of grades
    median = statistics.median(grade)
    # Uses statistics module to find median of grades
    mode = statistics.mode(grade)
    # Uses statistics modules to find mode of grades
    tuple = (mean), (median), (mode)
    # Creates object "tuple" to recieve mean, median, mode
    return tuple
    # Return tuple


# s1 = Student("Kyoungmin", 73)
# s2 = Student("Mercedes", 74)
# s3 = Student("Avanika", 78)
# s4 = Student("Marta", 74)
# s5 = Student("Sam", 86)
# s6 = Student("Charles", 99)
#
# student_list = [s1, s2, s3, s4, s5, s6]
# print(basic_stats(student_list))  # should print a tuple of three values
