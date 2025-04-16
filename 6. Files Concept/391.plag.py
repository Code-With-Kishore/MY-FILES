# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:03:13 2024

@author: Admin
"""

file = open('task.txt', 'r')
b = file.read()
c = b.split()
main = set(c)

stopword = open('project.txt', 'r')
e = stopword.read()
f = e.split()
stopwords = set(f)

n = int(input('Enter no.of.files:'))
files = []
for i in range(n):
    file = input('Enter files:')
    files.append(file)

diff = main.difference(stopwords)
ln = len(diff)

print("Original_filename:", file, "\t| Total_words:", ln)
print("_" * 125)
print("S.No\t|\tFile_Name\t\t|\tTotal_Words\t|\tUnique_Words\t|\tDuplicate_Words\t|\tUniqueWords_%")
print("_" * 125)

x = 0
for j in files:
    f1 = open(j)
    g = f1.read()
    h = g.split()
    k = set(h)
    d1=main.difference(k)
    d2=k.difference(main)
    total_words = len(h)
    unique_words = len(d2)
    duplicate_words = len(diff.intersection(d1))
    percent = unique_words / total_words * 100 

    x += 1
    print(x, "\t|\t", j, "\t\t|\t", total_words, "\t\t|\t", unique_words, "\t\t|\t", duplicate_words, "\t\t|\t", percent)
print("_" * 125)
