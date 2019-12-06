print("Welcome to the Python Guessing Game! You have 3 tries.")
guess = input("Please enter your answer: ")
answer = "shazbot"
no_of_tries = 2
attempts = 0

while guess != answer and attempts != no_of_tries:
    guess = input("Incorrcet. Please try again: ")
    attempts += 1

if guess == answer:
    print("You win!")
else:
    print("You lose!")