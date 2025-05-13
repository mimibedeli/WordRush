import random
import time
import threading
from collections import Counter

round_time = 60
my_timer = round_time
time_up = False

def game_introduction():
    print("\nWelcome to WordRush!")
    print("Form as many real words as you can using the given 8 letters.")

    
    print("\nChoose your game mode:")
    print("1 - Solo")
    print("2 - Versus Computer")
    print("3 - Multiplayer")
    
    mode = input("\nEnter 1, 2, or 3: ").strip()
    total_rounds = 3
    player_total_score = 0
    computer_total_score = 0
    
    if mode in ["1", "2"]:
        player_name = input("\nEnter your name: ").strip()
        
    if mode == "1":
        for round_num in range(1, total_rounds + 1):
            print(f"\n--- Round {round_num} ---")
            print(f"\n{player_name.upper()}'S TURN")
            _, player_score = play_game()
            player_total_score += player_score
        
        print("\n--- Game Over ---")
        print(f"\n{player_name}'s Total Score: {player_total_score}")    
        print()    
    elif mode == "2":
        for round_num in range(1, total_rounds + 1):
            print(f"\n--- Round {round_num} ---")
        
            print(f"\n{player_name.upper()}'S TURN")
            random_letters, player_score = play_game()
            player_total_score += player_score
            
            print("\n[COMPUTER'S TURN]")
            with open("words.txt", 'r') as file:
                valid_words = set(word.strip().lower() for word in file if word.strip())
            computer_word = computer_player(valid_words, random_letters)
            print(f"Computer's letters: {' '.join(random_letters)}")
            
            if computer_word:
                computer_score = len(computer_word)
                print(f"Computer guessed: {computer_word} ({computer_score} points)")
            else:
                computer_score = 0
                print("Computer couldn’t find a valid word.")     
            computer_total_score += computer_score
            
        print("\n--- Game Over ---")
        print(f"{player_name}'s Total Score: {player_total_score}")
        print(f"Computer's Total Score: {computer_total_score}")
        if player_total_score > computer_total_score:
            print(f"{player_name} wins!")
        elif player_total_score < computer_total_score:
            print("Computer wins!\n")
        else:
            print("It's a tie!")
        print()

    elif mode == "3":
        multiplayer_mode()

    else:
        print("Invalid input. Starting solo mode by default.")
    

def check_and_store_guess(raw_guess, guessed_words, valid_words, available_letters, min_length=3):
    try:
        guess = raw_guess.strip().lower()

        if len(guess) < min_length:
            return {
                "valid": False,
                "message": f"The word must be at least {min_length} letters."
            }

        if guess in guessed_words:
            return {
                "valid": False,
                "message": "The word has already been used."
            }

        if guess not in valid_words:
            return {
                "valid": False,
                "message": "The word isn't in the list."
            }

        if Counter(guess) - Counter(available_letters):
            return {
                "valid": False,
                "message": "The word uses invalid letters."
            }

        guessed_words.append(guess)
        return {
            "valid": True,
            "message": "Great guess!",
            "used_count": len(guessed_words)
        }

    except Exception as e:
        return {
            "valid": False, 
            "message": f"An unexpected error occurred: {str(e)}"
        }

def play_game():
    """
    Starts an interactive word game session using randomly selected letters.

    Args:
        None

    Side Effects:
        - Reads from 'words.txt' to load valid words.
        - Prints output to the console.
        - Prompts user for input via the console.
        - Tracks elapsed time to enforce a timed round.
        - Calls other functions to apply optional power-ups.
        - Displays the final score and word count at the end of the game.
          Arguments:
        None

    Returns:
        None

    """
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

    double_points = False
    round_time = 60
    if random.choice([True, False]):
        selected_powerup = random.choice(power_ups)
        print(f"You've been given: {powerup_names[selected_powerup]}!\n")

        if selected_powerup == "wildcard":
            while True:
                use_powerup = input("Do you want to use the Wildcard Power-Up? (yes/no): "
                               ).strip().lower()
                if use_powerup in ["yes", "no"]:
                    break
                else:
                    print("Invalid Input. Please type 'yes' or 'no'. ")
            if use_powerup == "yes":
                random_letters = wildcard_powerup(random_letters)

        elif selected_powerup == "extra_time":
            while True: 
                use_powerup = input("Do you want to use the Extra Time Power-Up? (yes/no): "
                                ).strip().lower()
                if use_powerup in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
            if use_powerup == "yes":
                round_time = extra_time_powerup()

        elif selected_powerup == "double_points":
            while True:
                use_powerup = input("Do you want to use the Double Points Power-Up? (yes/no): "
                               ).strip().lower()
                if use_powerup in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'. ")
            if use_powerup == "yes":
                double_points = double_points_powerup()
    else:
        print("No power-up this round :( \n")

    guessed_words = []
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = int(round_time - elapsed_time)
        
        if remaining_time <= 0:
            print("\nTime's up! The round has ended.")
            break
        
        print(f"\n Time left: {remaining_time} seconds.")
        
        guess = input("\nEnter a word: ").strip().lower()
        if guess == 'quit':
            break

        result = check_and_store_guess(  
            raw_guess=guess,
            guessed_words=guessed_words,
            valid_words=valid_words,
            available_letters=random_letters
        )

        print(result["message"])

    calculator = ScoreCalculator(list(guessed_words), len(random_letters))
    final_score = calculator.calculate_score()
    if double_points:
        final_score *= 2
    print(f"\nYou found {calculator.word_count()} words!")
    print(f"Your final score: {final_score}")
    print(f"Words you found: {', '.join(guessed_words) if guessed_words else 'None'}")
    
    return random_letters, final_score

def wildcard_powerup(letters):
    print("[WILDCARD ACTIVATED!] You can add or remove one letter!")
    
    while True:
        player_choice = input("\nType 'add' to add a letter or 'remove' to remove one: ").strip().lower()
        if player_choice in ["add", "remove"]:
            break
        else:
            print("Invalid input. Please type 'add' or 'remove'.")

    if player_choice == "add":
        new_letter = input("Enter the letter you want to add: ").strip().lower()
        letters.append(new_letter)
        print(f"New letter set: {' '.join(letters)}")

    elif player_choice == "remove":
        remove_letter = input(
            "Enter the letter you want to remove: ").strip().lower()
        if remove_letter in letters:
            letters.remove(remove_letter)
            print(f"New letter set: {' '.join(letters)}")
        else:
            print("That letter isn't in the set!")

    return letters

def extra_time_powerup():
    print("[EXTRA TIME ACTIVATED!] 10 extra seconds will be added to your round!")
    return 70

def double_points_powerup():
    print("[DOUBLE POINTS ACTIVATED!] Every valid word you make this round will earn double points!")
    return True

class ScoreCalculator:
    """
    Calculates score, bonus time, and word count.
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
                    score += 10
        return score

    def word_count(self):
        return len(self.valid_words)

    def bonus_time(self):
        total_characters = sum(len(word) for word in self.valid_words)
        return total_characters // 5

    def get_results(self):
        return (
            self.calculate_score(),
            self.bonus_time(),
            self.word_count()
        )
        
        
def computer_player(valid_words, available_letters):
    possible_words = [
        word for word in valid_words
        if not (Counter(word) - Counter(available_letters)) and len(word) >= 3
    ]   
    if possible_words:
        return max(possible_words, key=len)
    return None   


def multiplayer_mode():
    print("\nMultiplayer Mode: Enter number of players (2–4)")
    while True:
        try:
            num_players = int(input("How many players? (2-4): ").strip())
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    print()
    
    player_names = []
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ").strip()
        player_names.append(name)
    
    total_rounds = 3
    scores = {name: 0 for name in player_names}

    for round_num in range(1, total_rounds + 1):
        print(f"\n--- Round {round_num} ---")

        with open("words.txt", 'r') as file:
            valid_words = set(word.strip().lower() for word in file if word.strip())
        letters = list("eeeeaaaaiiiooouuulnstrcmphbdgkvywxzjqf")
        random_letters = random.sample(letters, 8)

        for player in player_names:
            print(f"\n{player.upper()}'S TURN") 
            print(f"\nYour letters: {' '.join(random_letters)}")
            round_score = multiplayer_turn(player, valid_words, random_letters)
            scores[player] += round_score
            
    print("\n--- Game Over ---")
    for player in player_names:
        print(f"{player}'s Total Score: {scores[player]}")
    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    if len(winners) == 1:
        print(f"\n{winners[0]} wins!")
    else:
        print("\nIt's a tie between: " + ", ".join(winners))
    print()
  
    
def multiplayer_turn(player_name, valid_words, random_letters):
    power_ups = ["wildcard", "double_points", "extra_time"]
    powerup_names = {
        "wildcard": "Wildcard",
        "extra_time": "Extra Time",
        "double_points": "Double Points"
    }

    double_points = False
    round_time = 60
    if random.choice([True, False]):
        selected_powerup = random.choice(power_ups)
        print(f"You've been given: {powerup_names[selected_powerup]}!\n")

        if selected_powerup == "wildcard":
            use_powerup = input("Do you want to use the Wildcard Power-Up? (yes/no): ").strip().lower()
            if use_powerup == "yes":
                random_letters = wildcard_powerup(random_letters)

        elif selected_powerup == "extra_time":
            use_powerup = input("Do you want to use the Extra Time Power-Up? (yes/no): ").strip().lower()
            if use_powerup == "yes":
                round_time = extra_time_powerup()

        elif selected_powerup == "double_points":
            use_powerup = input("Do you want to use the Double Points Power-Up? (yes/no): ").strip().lower()
            if use_powerup == "yes":
                double_points = double_points_powerup()
    else:
        print("No power-up this round :( \n")

    guessed_words = []
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = int(round_time - elapsed_time)

        if remaining_time <= 0:
            print(f"\nTime's up! {player_name}'s round has ended.")
            break

        print(f"\n Time left: {remaining_time} seconds.")
        guess = input("\nEnter a word: ").strip().lower()
        if guess == 'quit':
            break

        result = check_and_store_guess(guess, guessed_words, valid_words, random_letters)
        print(result["message"])

    score = ScoreCalculator(guessed_words, len(random_letters)).calculate_score()
    if double_points:
        score *= 2

    print(f"\n{player_name} found {len(guessed_words)} words!")
    print(f"{player_name} score this round: {score}")
    print(f"Words you found: {', '.join(guessed_words) if guessed_words else 'None'}")
    return score
         

if __name__ == "__main__":
    game_introduction()
