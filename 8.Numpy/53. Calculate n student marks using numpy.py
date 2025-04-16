# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:46:14 2025

@author: Admin
"""

import numpy as np

r=5
c=5

marks = np.random.randint(50, 100, (r,c))

total_marks = np.sum(marks, axis=1)  

average_marks = np.mean(marks, axis=1)

percentage = (total_marks / (500)) * 100  

highest_marks = np.max(marks, axis=1)

lowest_marks = np.min(marks, axis=1)

grades = np.where(
    percentage >= 90, 'A+',
    np.where(percentage >= 80, 'A',
    np.where(percentage >= 70, 'B',
    np.where(percentage >= 60, 'C',
    np.where(percentage >= 50, 'D', 'F')))))

print("Student Marks:\n", marks)
print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Grades:", grades)

subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)
subject_average = np.mean(marks, axis=0)

print("\nSubject-wise Highest Marks:", subject_highest)
print("Subject-wise Lowest Marks:", subject_lowest)
print("Subject-wise Average Marks:", subject_average)
