"""
he absolute difference between two integers, A and B, is written as |A-B|.
The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in elements.

Task
Complete the Difference class by writing the following:
A class constructor that takes an array of integers as a parameter and saves it to the element instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in elements and stores it in the minimum instance variable.

Input Format
You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in 2 lines of input. 
The first line contains N, the size of the elements array. The second line has N space-separated integers that describe the element array.

Output Format
You are not responsible for printing any output; the Solution class will print the value of the minimum difference instance variable.
"""
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)