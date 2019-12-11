print("Can you divide 3 by?")


def division(user_input):
    try:
        num1 = 3
        num2 = user_input
        answer = num1 / num2
        return print("The answer is " + str(answer))
    except ValueError():
        print("Invalid character - please choose a number")
        division(int(input("Choose another number: ")))
    except ZeroDivisionError:
        print("You cannot divide by zero")
        division(int(input("Choose another number: ")))


division(int(input("What do you want to divide by: ")))
