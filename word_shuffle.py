import random
from collections import Counter

def load_words(words):
    try:
        with open(words, 'r') as file:
            return set(word.strip().lower() for word in file if word.strip())
    except FileNotFoundError:
        print(f" File '{words.txt}' not found.")
        return set()

def get_random_letters(n=8):
    # Weighted letter list with common vowels/consonants
    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    return random.sample(letters, n)

def is_valid_guess(guess, available_letters, valid_words):
    if guess not in valid_words:
        return False
    guess_counter = Counter(guess)
    letters_counter = Counter(available_letters)
    return all(guess_counter[char] <= letters_counter[char] for char in guess)

def play_game():
    word_list = "words.txt"
    valid_words = load_words(word_list)

    if not valid_words:
        return  # Exit if word list can't be loaded

    letters = get_random_letters()
    print("\nUse these letters to make words! Type 'quit' to stop.")
    print("Your letters:", " ".join(letters))

    score = 0
    used_words = set()

    while True:
        guess = input("Your word: ").lower().strip()

        if guess == "quit":
            break
        if guess in used_words:
            print("You already used that word.")
        elif is_valid_guess(guess, letters, valid_words):
            print(" Great job!")
            score += len(guess)
            used_words.add(guess)
        else:
            print(" Not valid!")

    print("\n Game Over! Your score:", score)

# === Run the game ===
if __name__ == "__main__":
    play_game()
