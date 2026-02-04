age = 19 #This is an Integer
weight = 50.76 #This is called a float
greeting = "Hello" #This is a string
isMammal= True #This is Boolean

#Data Structures - Here, there are multiple elements in one variable
fruits =["apple", "banana", "cherry"] #This is a List - it is ordered and changeable, carries different data types
cars = ("Mercedez", "Jaguar", "Mazda" "Mitsubishi") #This is a Tuple - Elements are ordered, but are irreplaceable
countries = {"Tanzania","India","United Kingdom","Italy"} #This is a set - Elements are unordered, and unchangeable
student = {
    "First Name": "Udeh",
    "Course": "MIT",
    "Age": 19,
    "Nationality": "Kenyan",
} #This is a Dictionary - It stores key value pairs
courses = ["MIT","Data Science", "Cyber Security"] #This is an Array - It carries similar data types, e.g: strings only, numbers only, etc

print("Student is", age, "years old")
print(weight)
print("is animal a mammal?:", isMammal)
print(fruits)
print(countries)

#Type Casting - This is converting on datatype to another
print(float(age))
print(int(weight))