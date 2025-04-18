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
<<<<<<< HEAD
    
    try:
        with open(word_file, 'r') as file:
            valid_words = set(word.strip().lower() for word in file 
                              if word.strip())
=======
    try:
        with open("words.txt" , 'r') as file:
            valid_words = set(word.strip().lower() for word in file if 
                              word.strip())
>>>>>>> 1446c1c (updating shuffle function)
    except FileNotFoundError:
        print(f"File 'words.txt' not found.")
        return {'valid_guess': False, 'random_letters': [], 'guess': guess}

<<<<<<< HEAD
    
    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    random_letters = random.sample(letters, n)

    
=======
    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    random_letters = random.sample(letters, n)

    print("Your letters are:", " ".join(random_letters))
    guess = input("Enter your word guess: ").lower().strip()

>>>>>>> 1446c1c (updating shuffle function)
    guess = guess.lower()
    guess_count = {}
    for char in guess:
        guess_count[char] = guess_count.get(char, 0) + 1

<<<<<<< HEAD
=======
>>>>>>> 1446c1c (updating shuffle function)
    available_count = {}
    for char in random_letters:
        available_count[char] = available_count.get(char, 0) + 1

<<<<<<< HEAD
    
    if guess not in valid_words:
        return {'valid_guess': False, 'random_letters': random_letters,
                 'guess': guess}

    for letter in guess_count:
        if guess_count[letter] > available_count.get(letter, 0):
            return {'valid_guess': False, 'random_letters': random_letters,
                     'guess': guess}
=======
    if guess not in valid_words:
        return {'valid_guess': False, 'random_letters': random_letters, 
                'guess': guess}

    for letter in guess_count:
        if guess_count[letter] > available_count.get(letter, 0):
            return {'valid_guess': False, 'random_letters': random_letters, 
                    'guess': guess}
>>>>>>> 1446c1c (updating shuffle function)

    return {'valid_guess': True, 'random_letters': random_letters, 'guess': 
        guess}

if __name__ == "__main__":
    result = play_word_game()
    print(result)