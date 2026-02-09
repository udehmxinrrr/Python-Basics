#A function is the same as a method. it is a block of code that performs a specific task

#Standard Library Functions
y = max( 54,23,45,65,83,100,645,364,936,464)
print("The maximum number is", y)
print()
x = min(645,674,683,841,864,883,330,674,543,836)
print("The minimum number is", x)

#User-Defined Functions
def name():
    print("Udeh")
name() #This is calling a function

print()

def add():
    print(10+20)
add()

print()

def sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1+num2)
sum()

print()

def dog():
    name = ("Ttio")
    breed = ("Spitz")
    age = ("3")
    print(name,breed,age)
dog()

print()

def dog(name,breed,age): #A Variable is referred called a parameter when it is typed between the defined function's parentheses
    print(name, breed, age)
dog("Bosco","Spitz","3") #Arguments are values that are passed when calling the defined function
dog("Pato","Labrador","5") #Arguments are values that are passed when calling the defined function
dog("Aleko","Pitbull","4") #Arguments are values that are passed when calling the defined function
print()

#Write a program displaying details of five employees at a company, using a user-defined functions,parameters and functions
def Employee(employee, position, age, gender):
    print(employee,position,age,gender)
Employee("Andre Johnson","Senior VP",35,"M")
Employee("Charlie Maina","Junior VP",29,"M")
Employee("Ashley Mwakio","Senior Account",31,"F")
Employee("Riri Henshaw","Risk Analyst",31,"F")
Employee("Brenda Biggs","Manager",33,"F")

