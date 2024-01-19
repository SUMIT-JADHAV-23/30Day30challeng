"""Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example

In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format

There are 6 lines of input, where each line contains  6 space-separated integers that describe the 2D Array A.

Output Format

Print the maximum hourglass sum in A.

"""
def top(arr):
    for i in range(len(arr)-2):
            for j in range(len(arr[1])-2):
                top_sum = arr[i][j] , arr[i][j+1] , arr[i][j+2]

                print(top_sum)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    top(arr)
    

# middle = arr[i+1][j+1]
# bottom_sum = arr[i+2][j] , arr[i+2][j+1] ,arr[i+2][j+2]




# import math
# import os
# import random
# import re
# import sys

# def max_sum(arr):
#     # keeping in mind the constraint of `-9 <= arr[i][j] <= 9`
#     # minimum possible value we can have is -63 (if all value in the hourglass turns out to be -9)
#     highest = -63
#     for i in range(len(arr)-2):
#         for j in range(len(arr[1])-2):
#             top_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
#             middle = arr[i+1][j+1]
#             bottom_sum = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
#             hourglass_sum = top_sum + middle + bottom_sum
            
#             if hourglass_sum > highest:
#                 highest = hourglass_sum
#     print(highest)

# if __name__ == '__main__':

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
        
#     max_sum(arr)