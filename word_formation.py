import collections

def word_file():
    with open('words.txt', 'r') as file:
        words = set(word.strip().lower() for word in file)
    return words

def finding_words(letters, word_set):
    letters_counter = collections.Counter(letters.lower())
    valid_words = []

    for word in word_set:
        word_counter = collections.Counter(word)
        if all(word_counter[c] <= letters_counter[c] for c in word_counter):
            valid_words.append(word)

    return valid_words

if __name__ == "__main__":
    word_set = word_file()

    name = input("Enter your name: ")
    letters = input("Enter 8 letters: ").strip().lower()

    if len(letters) != 8 or not letters.isalpha():
        print("Please enter exactly 8 alphabetic characters.")
    else:
        matches = finding_words(letters, word_set)
        print(f"\nHi {name}, here are the words you can form from '{letters}':")
        for word in sorted(matches, reverse=True, key=lambda x: (len(x), x)):
            print(word)
