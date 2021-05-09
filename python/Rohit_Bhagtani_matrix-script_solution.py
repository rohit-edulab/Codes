#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
string = ""

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
  for j in range(n):
    string = string + matrix[j][i]
#print(string)

string1 = re.findall("(\w+)",string)
string2 = re.findall("\w\W+$",string)
string3 = re.findall("^\W*",string)
string = ""
#print(string1 , string2)
for i in range(len(string3)):
    string = string + string3[0]
for i in range(len(string1) - 1):
  string = string + string1[i] + " "

for j in range(len(string1)):
  string = string + string1[abs(len(string1) - 1)] 
  break
for i in range(len(string2)):
  string = string + string2[0][1:len(string2[0])]

print(string)
