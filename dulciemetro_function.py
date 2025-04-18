def calculate_score(valid_words, total_letters):
    """
    Calculate total score based on valid words and rules.

    Parameters:
    - valid_words: list of strings (valid player-submitted words)
    - total_letters: int (# of letters available in round)

    Returns:
    - int: total score
    """
    score = 0

    for word in valid_words:
        if len(word) >= 3:
            score += len(word)
            if len(word) == total_letters:
                score += 10  # bonus points for using all letters

    return score


# Test
test_valid_words = ["pact", "tropical", "plot", "trial"]
test_total_letters = 8

total_score = calculate_score(test_valid_words, test_total_letters)

print(f"Total Score: {total_score}")
