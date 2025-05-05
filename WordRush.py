import random

def play_game():
    try:
        with open("words.txt", 'r') as file:
            valid_words = set(word.strip().lower() for word in file if word.strip())
    except FileNotFoundError:
        print("File 'words.txt' not found.")
        return

    letters = list("eeeeaaaaiiiooouuulnstrcmphbdg")
    random_letters = random.sample(letters, 8)
    print("Use these letters to form valid words (type 'quit' to exit):")
    print("Your letters:", " ".join(random_letters))

    available_count = {}
    for char in random_letters:
        available_count[char] = available_count.get(char, 0) + 1

    while True:
        guess = input("Enter a word: ").strip().lower()
        if guess == 'quit':
            break

        if guess not in valid_words:
            print("Not a valid word.")
            continue

        guess_count = {}
        for char in guess:
            guess_count[char] = guess_count.get(char, 0) + 1

        valid = True
        for letter in guess_count:
            if guess_count[letter] > available_count.get(letter, 0):
                valid = False
                break

        if valid:
            print(" Valid guess!")
        else:
            print("Invalid use of letters.")

if __name__ == "__main__":
    play_game()
