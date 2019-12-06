

print("Welcome to the World's Greatest Calculator!")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
op = (input("Please enter your mathematical operation: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Please choose an appropriate mathematical operation.")

