"""
Task-Day 7
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
Example-A=[1,2,3,4]
Print 4 3 2 1. Each integer is separated by one space.
Input Format
The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers that describe array A's elements.
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
   
    for i in reversed(arr):
        print(i,end=" ")


# #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# txt = "     banana     "
# x = txt.rstrip()
# print("of all fruits", x, "is my favorite")
# #assign the char in rstrip(" ")
# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(",.qsw")
# print(x)

# # The strip() method removes any leading, and trailing whitespaces.
# # Leading means at the beginning of the string, trailing means at the end.
# # You can specify which character(s) to remove, if not, any whitespaces will be removed.
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)

# #remove left side
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.lstrip(",.grt")
# print(x)

# #where * is the unpacking operator that turns a list into positional arguments,
# #print(*[1,2,3]) is the same as print(1,2,3)
# a = [1, 2, 3, 4, 5]
# print(*a, sep = ' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))


"""

Task-Day-8
Given N names and phone numbers, assemble a phone book that maps friends names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
Input Format
The first line contains an integer,N , denoting the number of entries in the phone book.
Each of the N subsequent lines describes an entry in the form of 2 space-separated values on a single line. 
The first value is a friend's name, and the second value is an 8-digit phone number.
After the N lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.
Note: Names consist of lowercase English alphabetic letters and are first names only.
Output Format
On a new line for each query, print Not found if the name has no corresponding entry in the phone book;
otherwise, print the full name and phonenumber in the format name=phoneNumber.

"""




# #for same line keys values input
# n=int(input())
# dict1={}
# for i in range(n):
#     key,values=input().split()
#     dict1[key]=values
# print(dict1)


# for separate line keys and values input
# N=int(input())
# d={}
# for i in range(N):
#     tmp=input()
#     d[tmp]=input()
# print (d)


n=int(input())
dict1={}
for i in range(n):
    key,values=input().split()
    dict1[key]=values
    # print(dict1)
for keys,values in dict1.items():
    query=input()
    if query==key:
        print(key,values)
    else:
        print("Not found")    

"""
n = int(input())
dict1 = {}
# Input key-value pairs
for i in range(n):
    key, values = input().split()
    dict1[key] = values
# Input queries
for j in range(n):
    query = input()
    # Check if the query key is present in the dictionary
    if query in dict1:
        print(query,"=",dict1[query])
    else:
        print("Not Found")



import sys 
# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()
# print(lines)
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
"""


