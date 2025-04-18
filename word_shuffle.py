import random

def play_word_game(n=8):
    """
    Loads a word list from 'words.txt', generates a random letter set, 
    shows the letters to the player, takes one word guess, and checks if 
    it's valid.

    Args:
        n (int): Number of random letters to generate (default is 8).

    Returns:
        dict: A dictionary with the player's guess, the letters shown, and 
        whether the guess was valid.
    """
    try:
        with open("words.txt", 'r') as file:
            valid_words = set(word.strip().lower() for word in file if 
                              word.strip())
    except FileNotFoundError:
        print("File 'words.txt' not found.")
        return {'valid_guess': False, 'random_letters': [], 'guess': None}

    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    random_letters = random.sample(letters, n)

    print("Your letters are:", " ".join(random_letters))
    guess = input("Enter your word guess: ").lower().strip()

    guess_count = {}
    for char in guess:
        guess_count[char] = guess_count.get(char, 0) + 1

    available_count = {}
    for char in random_letters:
        available_count[char] = available_count.get(char, 0) + 1

    if guess not in valid_words:
        return {'valid_guess': False, 'random_letters': random_letters, 
                'guess': guess}

    for letter in guess_count:
        if guess_count[letter] > available_count.get(letter, 0):
            return {'valid_guess': False, 'random_letters': random_letters, 
                    'guess': guess}

    return {'valid_guess': True, 'random_letters': random_letters, 
            'guess': guess}


if __name__ == "__main__":
    result = play_word_game()
    print(result)