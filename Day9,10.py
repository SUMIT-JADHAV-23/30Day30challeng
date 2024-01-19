"""#recursion-the process of defining a function or calculating a number by the repeated application of an algrithm
#factorial of number - factorial is a function that multiplies a number by every number below it till 1

def factorial(n):
    # Write your code here
    #base case
    if n<1:
        return 1
    #recursion case-keep go
    else:
        #3*factorial(2)---(3-1)
        #3*2*factorial(1)---(2-1)
        #3*2*1*factorial(0)---(1-1)
        #3*2*1*0 #base case
        return n*factorial(n-1)


if __name__ == '__main__':
    n = int(input().strip())
    result = factorial(n)
    print(result)




#The summation of an explicit sequence is denoted as a succession of additions.
#Sum = 1+2+3+4+……………+ 97 + 98 + 99 + 100=5050
def summation(n):
    # Write your code here
    #base case
    #factorial(0)=0
    if n<0:
        return 0
    #recursion case-keep go
    else:
        #3+factorial(2)---(3-1)
        #3+2+factorial(1)---(2-1)
        #3+2+1+factorial(0)---(1-1)
        #3+2+1+0 #base case
        return n+summation(n-1)


if __name__ == '__main__':
    n = int(input().strip())
    result = summation(n)
    print(result)


#Exponentiation in math is defined as the operation used to represent repeated multiplication.
#For example, if 10 is multiplied three times, then it can be written as "10 raised to 3" which means 10*3. 
#Here, 10 is the base, and 3 is the exponent.
def exponentiation(n,p):
    # Write your code here
    #base case
    if p <= 0:
        return 1
    #recursion case-keep go
    else:
        #3*exponentiation(3,p-1))
        #3*3*exponentiation(3,p-1)
        #3*3*3*exponentiation(3,p-1)
        #3*3*3*1 #base case
        return n*exponentiation(n,p-1)


if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())
    result = exponentiation(n,p)
    print(result)

"""


#Day10

#find binaray and consucative number


n = int(input("Enter a decimal number: ").strip())
binary_list = []

while n > 0:
    remainder = n % 2
    binary_list.insert(0, remainder)  # Insert the remainder at the front of the list
    print(binary_list)
    n = n // 2  # This is integer division. It returns the quotient as an integer, discarding any decimal part.
    print(n)
print(binary_list)



#max consucative one's

n = int(input().strip())
n_bin=bin(n)
bin_str=(n_bin.removeprefix('0b'))
count_1=0
max_one=0
for i in bin_str :
    if i == "1" :
        count_1 += 1
        # print(count_1)
        max_one = max(max_one, count_1)
        # print(max_one)
    else:
        count_1=0

print(max_one)


