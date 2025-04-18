def wordrush_wildcard_check():
    """
    WordRush with wildcard power-up.
    Uses words from words.txt, allows player to add/remove a letter, 
    and checks if their guessed word is valid.
    """
    
    with open("words.txt", "r") as file:
        all_words = [word.strip().lower() for word in file if word.strip()]


    letters = ['A', 'T', 'E', 'R', 'N', 'M']
    print("Welcome to WordRush!")
    print("Here are your letters:", " ".join(letters))

    use_powerup = input(
        "You've been given the wildcard power-up!"
        " Would you like to use it? (yes/no): " 
       ).lower()
    if use_powerup == "yes":
            choice = input("Would you like to add or remove a letter?"
                           "(add/remove): "
                           ).lower()
    if choice == "add":
        letter = input("Enter the letter you want to add (A-Z): "
                       ).strip().upper()
        if letter not in letters:
            letters.append(letter)
            print(f"'{letter}' was added.")
    elif choice == "remove":
        letter = input("Enter the letter you want to remove: ").strip().upper()
        if letter in letters:
            letters.remove(letter)
            print(f"'{letter}' was removed.")


    print("Your final letter set:", " ".join(letters))

    valid_words = []
    for word in all_words:
        upper_word = word.upper()
        if all(char in letters for char in upper_word):
            valid_words.append(word)

    guess = input("Enter a word using your letters: ").lower().strip()

    if guess in valid_words:
        print("Valid word!")
    else:
        print("Not valid.")


if __name__ == "__main__":
    wordrush_wildcard_check()