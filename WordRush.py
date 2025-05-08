import random


def game_introduction():
    print("\nWelcome to WordRush!")
    print("Form as many real words as you can using the given 8 letters.")


def play_game():
    with open("words.txt", 'r') as file:
        valid_words = set(word.strip().lower() for word in file if word.strip())
        
    letters = list("eeeeaaaaiiiooouuulnstrcmphbdgkvywxzjqf")
    
    random_letters = random.sample(letters, 8)
    print("\nUse these letters to form valid words (type 'quit' to exit):")
    print("Your letters: ", " ".join(random_letters))
    print()
    
    power_ups = ["wildcard", "double_points", "extra_time"]
    powerup_names = {
        "wildcard": "Wildcard",
        "extra_time": "Extra Time",
        "double_points": "Double Points"
    }
    
    if random.choice([True, False]):
        selected_powerup = random.choice(power_ups)
        print(f"You've been given: {powerup_names[selected_powerup]}!\n")
        
        if selected_powerup == "wildcard":
            use_powerup = input("Do you want to use the Wildcard Power-Up? (yes/no): "
                        ).strip().lower()
            if use_powerup == "yes":
                random_letters = wildcard_powerup(random_letters)
        
        elif selected_powerup == "extra_time":
            use_powerup = input("Do you want to use the Extra Time Power-Up? (yes/no): "
                        ).strip().lower()
            if use_powerup == "yes":
                extra_time_powerup()
            
        elif selected_powerup == "double_points":
            use_powerup = input("Do you want to use the Double Points Power-Up? (yes/no): "
                        ).strip().lower()
            if use_powerup == "yes":
                double_points_powerup()
                       
    else:
        print("No power-up this round :( \n")

    available_count = {}
    for char in random_letters:
        available_count[char] = available_count.get(char, 0) + 1

    while True:
        guess = input("\nEnter a word: ").strip().lower()
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
            
            
def wildcard_powerup(letters):
    print("[WILDCARD ACTIVATED!] You can add or remove one letter!")
    player_choice = (
        input("\nType 'add' to add a letter or 'remove' to remove one: ")
        .strip().lower()
    )   
    
    if player_choice == "add":
        new_letter = input("Enter the letter you want to add: ").strip().lower()
        letters.append(new_letter)
        print(f"New letter set: {' '.join(letters)}")

    elif player_choice == "remove":
        remove_letter = (
            input("Enter the letter you want to remove: ").strip().lower()
        )
        letters.remove(remove_letter)
        print(f"New letter set: {' '.join(letters)}")

    return letters


def extra_time_powerup():
    print("[EXTRA TIME ACTIVATED!] 10 extra seconds will be added to your round!")
    
    
def double_points_powerup():
    print("[EXTRA TIME ACTIVATED!] Every valid word you make this round will earn double points!")            
            
            
class ScoreCalculator:
    """
    Calculating the score, the bonus time, and the number of words created by
    the player.
    """  
    def __init__(self, valid_words, total_letters):
        self.valid_words = valid_words
        self.total_letters = total_letters
        
    def calculate_score(self):
        score = 0
        
        for word in self.valid_words:
            if len(word) >= 3:
                score += len(word)
                if len(word) == self.total_letters:
                    score += 10 # adding the bonus points if player used all letters
        return score
    
    def word_count(self):
        return len(self.valid_words)
    
    def bonus_time(self):
        total_characters = sum(len(word) for word in self.valid_words)
        return total_characters // 5 
    

if __name__ == "__main__":
    game_introduction()
    play_game()


