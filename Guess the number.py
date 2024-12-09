import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Take input from the user
            user_guess = int(input("Enter your guess: "))
            
            # Compare the guess to the random number
            if user_guess < random_number:
                print("Oops too low! Try again.")
            elif user_guess > random_number:
                print("Oops too high! Try again.")
            else:
                print("WOW Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Call the function to start the game
guess_the_number()
