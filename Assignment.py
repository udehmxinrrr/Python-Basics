# Write a python program that prompts a user to enter a number and checks whether the number is even or odd

number = int(input("Enter a number: "))
if number

    # Function to check if a number is even or odd
    def check_even_odd(number):
        if number % 2 == 0:
            return f"{number} is Even"
        else:
            return f"{number} is Odd"


    # Taking input from the user
    try:
        user_input = int(input("Enter a number: "))
        print(check_even_odd(user_input))
    except ValueError:
        print("Invalid input! Please enter a whole number.")g
