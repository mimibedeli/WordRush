import random
import time
from collections import Counter


def game_introduction():
    """
    Primary Author: Michelle Melendez
    Technique Claimed: f-strings containing expressions

    Prints the game introduction and prompts the user to choose a mode.
    Handles initial input and sets up single or multiplayer rounds.
    """
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
    """
    Primary Author: Hung Lai
    Technique Claimed: optional parameters

   Validates a user's guess based on length, duplication, dictionary presence, 
   and allowed letters.

    Args:
        raw_guess (str): The player's guess.
        guessed_words (list): A list of words already guessed.
        valid_words (set): Set of valid words from the dictionary.
        available_letters (list): The letters available for forming words.
        min_length (int, optional): Minimum required length of the guess.

    Returns:
        dict: A dictionary with keys 'valid' (bool), 'message' (str), and 
        optionally 'used_count' (int).

    Side Effects:
        Appends a valid guess to guessed_words.
    """
    
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
    Primary Author: Germid Molina
    Technique Claimed: with statement
    
    Runs one round of the solo or versus-computer game. 
    Applies power-ups, validates guesses, tracks time, and calculates 
    the final score.

    Returns:
        tuple: A tuple containing the list of random letters used and the 
        player's final score (int).

    Side Effects:
        Reads from 'words.txt', prints prompts and messages, interacts with user 
        input.
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
    print("\n Round Over!")

    calculator = ScoreCalculator(list(guessed_words), len(random_letters))
    final_score = calculator.calculate_score()
    if double_points:
        final_score *= 2
    print(f"\nYou found {calculator.word_count()} words!")
    print(f"Your final score: {final_score}")
    print(f"Words you found: {', '.join(guessed_words) if guessed_words else 'None'}")
    
    return random_letters, final_score

def wildcard_powerup(letters):
    """
    Primary Author: Michelle Melendez
    Technique Claimed: conditional expressions

    Lets the player add or remove a letter from their current set.

    Args:
        letters (list): The current list of available letters.

    Returns:
        list: Updated list of letters after the wildcard power-up.

    Side Effects:
        Modifies and prints the letter list based on user input.
    """
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
    """
    Primary Author: Michelle Melendez

    Adds 10 seconds to the round when activated.
    """
    print("[EXTRA TIME ACTIVATED!] 10 extra seconds will be added to your round!")
    return 70

def double_points_powerup():
    """    
    Primary Author: Michelle Melendez

    Doubles the score for the round when activated.
    """
    print("[DOUBLE POINTS ACTIVATED!] Every valid word you make this round will earn double points!")
    return True

class ScoreCalculator:
    """
    Calculates score, bonus time, and word count for a set of valid words.
    
    Primary Author: Dulcinea Metro
    """
    def __init__(self, valid_words, total_letters):
        """
        Initializes ScoreCalculator with list of valid words and
        total number of letters in game.

        Parameters:
            valid_words (list of str): The list of valid words submitted.
            total_letters (int): The total number of letters in the puzzle.

        Primary Author: Dulcinea Metro
        """
        self.valid_words = valid_words
        self.total_letters = total_letters

    def calculate_score(self):
        """
        Calculates the total score based on word lengths. 
        Words with at least 3 letters earn points equal to their length.
        A word that uses all the letters gets 10 bonus points.

        Returns:
            int: The total score.

        Primary Author: Dulcinea Metro

        Techniques Claimed: original algorithm
        """
        score = 0
        for word in self.valid_words:
            if len(word) >= 3:
                score += len(word)
                if len(word) == self.total_letters:
                    score += 10
        return score

    def word_count(self):
        """
        Counts the number of valid words submitted.

        Returns:
            int: The number of valid words.

        Primary Author: Dulcinea Metro
        """
        
        return len(self.valid_words)

    def bonus_time(self):
        """
        Calculates bonus time based on the total number of characters
        across all valid words. One bonus second is given for every 5 characters.

        Returns:
            int: The number of bonus seconds earned.

        Primary Author: Dulcinea Metro

        Techniques Claimed: generator expression
        """
        total_characters = sum(len(word) for word in self.valid_words)
        return total_characters // 5

    def get_results(self):
        """
        Returns a tuple of (score, bonus time, word count) by calling 
        the appropriate methods.

        Returns:
            tuple: (score, bonus_time, word_count)

        Primary Author: Dulcinea Metro
        """
        return (
            self.calculate_score(),
            self.bonus_time(),
            self.word_count()
        )
        
        
def computer_player(valid_words, available_letters):
    """    
    Primary Author: Michelle Melendez
    Technique Claimed: use of a key function with max()

    Chooses the longest valid word the computer can make with the given letters.

    Args:
        valid_words (set): Set of valid dictionary words.
        available_letters (list): Letters the computer is allowed to use.

    Returns:
        str or None: The best word found or None if no valid word exists.
    """
    possible_words = [
        word for word in valid_words
        if not (Counter(word) - Counter(available_letters)) and len(word) >= 3
    ]   
    if possible_words:
        return max(possible_words, key=len)
    return None   


def multiplayer_mode():
    """
    Primary Author: Hung Lai
    Technique Claimed: sequence unpacking

    Runs the full multiplayer game logic across 3 rounds.
    Collects player names, handles turns, tracks scores, and declares a winner.

    Side Effects:
        Prompts user input for number of players and names,
        prints round results and final scores.
    """
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
    """
    Primary Author: Germid Molina
    Technique Claimed: set operations

    Handles one player's full turn during a multiplayer round.
    Applies random power-ups and scores valid guesses.
    
    Args:
        player_name (str): The name of the player taking the turn.
        valid_words (set): Set of valid dictionary words.
        random_letters (list): Letters available for that round.

    Returns:
        int: Score for that player's round.

    Side Effects:
        Interacts with player via input/output, prints score summary.
    """
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
