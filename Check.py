number = int(input("Enter the number: "))

print("Multiplication Table of", number)
for i in range(1, 11):
    print(number, "X", i, "=", number * i)

input("Multiplication printed")

