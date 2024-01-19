#Using the super() method we can invoke the parent class constructor from a child class
"""Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string,F name .
A string, L name.
An integer, ID.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg_score = sum(self.scores)/len(self.scores)
        grade = ''
        if avg_score >= 90:
            grade = 'O'
        elif avg_score >= 80:
            grade = 'E'
        elif avg_score >= 70:
            grade = 'A'
        elif avg_score >= 55:
            grade = 'P'
        elif avg_score >= 40:
            grade = 'D'
        elif avg_score < 40:
            grade = 'T'
        return grade

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


"""
def __init__(self, firstName, lastName, idNumber, scores):
    self.scores = scores
    super().__init__(firstName, lastName, idNumber)
#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here


def calculate(self):
    a = sum(self.scores) / len(self.scores)
    if 90 <= a <= 100:
        Grade = 'O'
    elif 80 <= a <90:
        Grade = 'E'
    elif 70 <= a < 80:
        Grade = 'A'
    elif 55 <= a < 70:
        Grade = 'P'
    elif 40 <= a < 55:
        Grade = 'D'
    else:
        Grade = 'T'
    return Grade"""