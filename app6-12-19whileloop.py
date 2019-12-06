
i = 1
print("Current value of \"i\" is " + str(i))

num1 = float(input("Please enter a number to add to \"i\": "))

while i <= 10:
    print(i)
    i += num1

print("Loop finished. \"i\" now exceeds 10 (result: " + str(i) + ")")