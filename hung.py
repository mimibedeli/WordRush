import random

def get_shuffled_word_from_file(filename):
    """Reads 8-letter words from a file, picks one randomly, and returns it with its shuffled version."""
    try:
        with open(filename, 'r') as file:
            words = [word.strip().lower() for word in file if len(word.strip()) == 8]

        target_word = random.choice(words)
        letters = list(target_word)
        random.shuffle(letters)
        shuffled_word = ''.join(letters)

        return target_word, shuffled_word

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None

if __name__ == "__main__":
    while True:
        target_word, shuffled = get_shuffled_word_from_file('words.txt')

        print("Use the letters below to unscramble the eight-letter word:")
        print(f"Shuffled letters: {shuffled.lower()}")

        guess = input("Your guess: ").strip().lower()

        if guess == target_word:
            print("Correct! You guessed the word!")
        else:
            print(f"Incorrect. The correct word was: {target_word}")

        play_again = input("If you would like to play again, answer 'yes': ").strip().lower()
        if play_again not in ('yes'):
            print("Thanks for playing!")
            break
