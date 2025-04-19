from collections import Counter

def check_and_store_guess(raw_guess, used_words, valid_words, available_letters, min_length=3):
    """
    The program will check if a guess is valid based on the length, 
    repeated, in the word list, and 
    whether it's long enough, not repeated, in the word list, 
    and only uses specific letters. If valid, stores the guess.
    """
    
    guess = raw_guess.strip().lower()

    if len(guess) < min_length:
        return {
            "valid": False,
            "message": f"The word must be at least {min_length} letters."
        }

    if guess in used_words:
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

    used_words.add(guess)

    return {
        "valid": True,
        "message": "Great guess!",
        "used_count": len(used_words)
    }
