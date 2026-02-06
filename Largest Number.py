first = int(input("Enter a number: "))
second = int(input("Enter another number: "))
third = int(input("Enter a third number: "))

if first > second and first > third:
    print(first, "is the greatest number.")
elif second > first and second > third:
    print(second, "is the greatest number")
else:
    print(third, "is the greatest number")