import random

def play_word_game(word_file, guess, n=8):
    """
    Loads words from a file, generates random letters, and checks if a guess is valid.

    Args:
        word_file (str): Path to the file containing valid words.
        guess (str): The user's word guess.
        n (int): Number of random letters to generate (default is 8).

    Returns:
        dict: Game results including random letters and guess validity.
    """
    # Load valid words from file
    try:
        with open(word_file, 'r') as file:
            valid_words = set(word.strip().lower() for word in file if word.strip())
    except FileNotFoundError:
        print(f"File '{word_file}' not found.")
        return {'valid_guess': False, 'random_letters': [], 'guess': guess}

    # Generate random letters
    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    random_letters = random.sample(letters, n)

    # Count letters in guess
    guess = guess.lower()
    guess_count = {}
    for char in guess:
        guess_count[char] = guess_count.get(char, 0) + 1

    # Count letters in available pool
    available_count = {}
    for char in random_letters:
        available_count[char] = available_count.get(char, 0) + 1

    # Check if guess is valid
    if guess not in valid_words:
        return {'valid_guess': False, 'random_letters': random_letters, 'guess': guess}

    for letter in guess_count:
        if guess_count[letter] > available_count.get(letter, 0):
            return {'valid_guess': False, 'random_letters': random_letters, 'guess': guess}

    return {'valid_guess': True, 'random_letters': random_letters, 'guess': guess}
