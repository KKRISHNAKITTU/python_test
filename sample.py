# Simple number checker

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number zero")

print("\nNumbers from 1 to", number)

for i in range(1, number + 1):
    print(i)
