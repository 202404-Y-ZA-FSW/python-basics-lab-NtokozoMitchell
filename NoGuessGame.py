import random

def Guess_Number():
    used_numbers = set()  # Keep track of used numbers
    target_number = random.randint(1, 100)
    while target_number in used_numbers:  # Ensure a new number
        target_number = random.randint(1, 100)
    used_numbers.add(target_number)

    attempts = 0
    guessed_correctly = False

    print("Hi User, Welcome to the number Guessing Game !🤪")
    print("I have selected a number between 1 and 100. Can you guess what it is?🤔")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < target_number:
                print("Too Low! Please try again." )
            elif user_guess > target_number:
                print("Too High! Please try again.")
            else:
                guessed_correctly = True
                print(
                    f"Congratulations! You have guessed the correct number {target_number} in {attempts} attempts."
                )

        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 100.")

    
    play_again = input("Thank you for playing, Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        return  # Exit the function if the user doesn't want to play again

    # If playing again, clear used numbers for a fresh game
    else:
        used_numbers.clear()
        Guess_Number()  # Start a new game

# Start the game
Guess_Number()
