import random

# Function to select difficulty level
def select_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (5 attempts per word)")
    print("2. Medium (3 attempts per word)")
    print("3. Hard (1 attempt per word)")
    
    while True:
        difficulty = input("Enter difficulty (1/2/3): ").strip()
        if difficulty == '1':
            return 5
        elif difficulty == '2':
            return 3
        elif difficulty == '3':
            return 1
        else:
            print("Invalid choice, please select 1, 2, or 3.")

# Function to start the game
def start_game(attempts):
    words = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "SATURDAY", "SUNDAY", "HELLO", "PYTHON"]
    score = 0

    print("......................Welcome to the Word Scramble Game!......................")
    print(f"You have {attempts} attempts to guess the word correctly.")
    
    while True:
        word = random.choice(words)
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)

        print(f"\nScrambled word: {scrambled}")

        count = 0
        while count < attempts:
            guess = input(f"Attempt {count + 1}/{attempts} - Your guess: ").strip().upper()

            if guess == word:
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect!")
                count += 1

        if count == attempts:
            print(f"Max attempts reached! The word was '{word}'.")

        again = input("\nPlay again? (Y/N): ").strip().upper()
        if again != 'Y':
            print(f"\n.....................Game Over! Your total score: {score}.....................")
            break

# Main function to run the game
def main():
    attempts = select_difficulty()
    print(f"Game starting with {attempts} attempts per word.\n")
    start_game(attempts)

# Start the game
main()
