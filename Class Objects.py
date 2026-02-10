#A class is the blueprint of an object in OOP
#An object is an instance of a class

#Name, Age , Gender and Course are attributes/characteristics of the class
class Student:
    name = "Joy"
    age = 21
    gender = "Female"
    course = "MIT"

#The following are Behaviors/Functions
    def study(self):
        print("Student is Studying")

student1 = Student() #This is how an object is created;by creating a variable and assign the object to it.
student1.study()
print(student1.name)

student2 = Student()