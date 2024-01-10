"""Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. 
The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; 
if a negative argument is passed as initialAge, the constructor should set age to  0and print Age is not valid, setting age to 0.
In addition, you must write the following instance methods:
1.yearPasses() should increase the age instance variable by 1.
2.amIOld() should perform the following conditional actions:
If age < 13, print You are young..
If age => 13 and age < 18, print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you,
but you’ll be writing everything in the future. The code that creates each instance of your Person class is in the main method.
Don’t worry if you don’t understand it all quite yet!
Note: Do not remove or alter the stub code in the editor.
Input Format
Input is handled for you by the stub code in the editor.
The first line contains an integer, T (the number of test cases), and 
the T subsequent lines each contain an integer denoting the age of a Person instance.
Constraints
1 <= T <= 4
-5 <= age <= 30
Output Format
Complete the method definitions provided in the editor so they meet the specifications outlined above;
the code to test your work is already in the editor.
If your methods are implemented correctly, each test case will print 2 or 3 lines 
(depending on whether or not a valid initialAge was passed to the constructor)."""

#day 4


"""for j in range(0, 3): - This is an inner loop that iterates three times. 
It represents the passage of three years for the current person.
p.yearPasses() - Inside the loop, the yearPasses method of the Person class is called.
This method likely increments the age of the person by one year and may perform any other necessary updates.
After this loop, the person's age has been increased by three years
This line calls the amIOld method of the Person class, which prints a message about the person's age category based on the updated age
This line prints an empty line to separate the output for different test cases.
It adds a visual break between the output for one person and the next when multiple test cases are being processed.

The statement for _ in range(3): is used to simulate the passage of three years for the person.
The specific number 3 is arbitrary and depends on the requirements of the problem or the desired simulation.
In this case, the task does not specify a particular number of years to simulate, so the choice of 3 is somewhat arbitrary.
It's common in such programming exercises to choose a small number to keep the simulation manageable and
to showcase the behavior of the class without making the output too lengthy.
You could choose a different number if you want to simulate a different number of years passing. 
For example, you could use for _ in range(5): if you want to simulate five years passing. 
The choice of the number in the range depends on the context and requirements of the problem you are solving"""


class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge            
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console+
        if ( self.age < 13 ):
            print("You are young.")
        elif ( self.age >= 13 and self.age < 18 ):
            print("You are a teenager.")
        else:
            print("You are old.")     
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age +=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

# Test Case 0: initialAge = -1
# Because initialAge < 0, our code must set age to 0 and print the “Age is not valid…” message followed by the young message. 
# Three years pass and age = 3, so we print the young message again.

# Test Case 1: initialAge = 10
# Because initialAge < 13, our code should print that the person is young. 
# Three years pass and age = 13, so we print that the person is now a teenager.

# Test Case 2: initialAge = 16
# Because 13 <= initialAge < 18, our code should print that the person is a teenager. 
# Three years pass and age = 19, so we print that the person is old.

# Test Case 3: initialAge = 18
# Because initialAge => 18, our code should print that the person is old. 
# Three years pass and the person is still old at age = 21, so we print the old message again.