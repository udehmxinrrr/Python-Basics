# Create a simple calculator program with the +,-,/and * operators.

num1 = int(input("Enter a number: "))
op = input("Enter a operator: ")
num2 = int(input("Enter a second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print(num1 / num2)
