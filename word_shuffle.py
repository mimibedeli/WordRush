import random

def load_words(words):
    try:
        with open(words, 'r') as file:
            return set(word.strip().lower() for word in file if word.strip())
    except FileNotFoundError:
        print(f" File '{words}' not found.")
        return set()

def get_random_letters(n=8):

    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    return random.sample(letters, n)

def count_letters(word):
    """Returns a dictionary with counts of each letter in the word."""
    letter_count = {}
    for char in word:
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def is_valid_guess(guess, available_letters, valid_words):
    if guess not in valid_words:
        return False

    guess_count = count_letters(guess)
    available_count = count_letters(available_letters)

    for letter in guess_count:
        if guess_count[letter] > available_count.get(letter, 0):
            return False
    return True

def play_game():
    word_list = "words.txt"
    valid_words = load_words(word_list)

    if not valid_words:
        return  

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


if __name__ == "__main__":
    play_game()
