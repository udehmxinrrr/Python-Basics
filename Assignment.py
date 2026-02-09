# Write a python program that prompts a user to enter a number and checks whether the number is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
if number == 0:
    print("Number is Neutral")
