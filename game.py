	import random

def play_game():
    print("\n========== NUMBER GUESSING GAME ==========")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    # Generate random number
    number = random.randint(1, 100)

    # Maximum attempts
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))

            # Check valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Compare guess with generated number
            if guess == number:
                print(f"\n🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")
                
                # Score based on attempts
                score = (max_attempts - attempts + 1) * 10
                print(f"Your score: {score}")
                return True

            elif guess > number:
                print("Too high! Try a smaller number.")

            else:
                print("Too low! Try a larger number.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # If attempts are completed
    print(f"\n❌ Game Over!")
    print(f"The correct number was {number}.")
    print("Your score: 0")
    return False


# Main program
total_score = 0
rounds_won = 0
round_number = 1

while True:
    print(f"\n******** ROUND {round_number} ********")

    won = play_game()

    if won:
        rounds_won += 1

    # Ask whether user wants another round
    choice = input("\nDo you want to play another round? (yes/no): ").lower()

    if choice != "yes":
        break

    round_number += 1

print("\n========== FINAL RESULT ==========")
print(f"Rounds played : {round_number}")
print(f"Rounds won    : {rounds_won}")
print("Thank you for playing!")