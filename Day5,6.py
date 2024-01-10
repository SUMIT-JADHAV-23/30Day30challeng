"""
Task-day 5
Given an integer,n , print its first 10 multiples.
Each multiple n x i (where 1<i<10 ) should be printed on a new line in the form: n x i = result.

"""
# #use for loop
# def multiple(n):
#     for i in range(1, 11):
#         print(f'{n} x {i} = {n*i}')
        
# if __name__ == '__main__':
#     n = int(input().strip())
#     multiple(n)

# #without def
# n = int(input())
# for i in range(1, 11):
#     result = n * i
#     print(f"{n} x {i} = {result}")


# #use while loop
# n = int(input())
# i = 1
# while i < 11:
#     result = n * i
#     print(f"{n} x {i} = {result}")
#     i += 1


# # Taking an integer input from the user
# n = int(input("Enter an integer: "))

# # Using map and lambda to create a list of strings representing the multiplication results
# # Mapping with Lambda Function: The map function is used to apply a lambda function to each element in the range from 1 to 10 (exclusive). 
# # The lambda function takes an index i and creates a string representing the multiplication result of n by i. This results in a list of strings.
# # Converting to List: The list function is used to convert the map result into a list. The list is named multiples.
# multiples = list(map(lambda i: f"{n} x {i} = {n * i}", range(1, 11)))

# # Joining the list of strings with newline characters and printing the result
# print('\n'.join(multiples))



"""
Task - day 6
Given a string, S, of length N  that is indexed from 0 to N-1 , 
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line 
(see the Sample below for more detail).
Note: 0 is considered to be an even index.
Example=s=adbecf
Print abc def
Input Format
The first line contains an integer, T(the number of test cases).
Each line i of the T subsequent lines contain a string,S .

"""
# def even_odd_separation(s):
#     even = []
#     odd = []

#     for i in range(len(s)):
#         if i % 2 == 0:
#             #apped add element
#             even.append(s[i])
#             print(even)
#         else:
#             odd.append(s[i])
#             print(odd)
#     #''.join fun used for joining list of space speareted char
#     return "".join(even), "".join(odd)

# n = int(input())
# for _ in range(n):
#     s = input()
#     res_even, res_odd = even_odd_separation(s)
#     print(res_even,res_odd)



#from slicing
"""
#index slicing
n=int(input())
for _ in range(n):
    s=str(input())
    print(s[::2] ,s[1::2])
"""


# from import itertools

"""
import itertools

n = int(input())
for _ in range(n):
    s = str(input())
    odd = itertools.islice(s, 0, None, 2)
    even = itertools.islice(s, 1, None, 2)
    print(''.join(odd),''.join(even))
"""
