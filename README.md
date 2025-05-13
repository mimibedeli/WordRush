# WordRush
WordRush is a fast-paced, interactive terminal based word game where players form real words using a random selection of 8 letters. The game features built-in power-ups, score tracking, and time-based challenges to make gameplay engaging and competitive.

# How to Play
1. When you start the game, you’ll receive 8 random letters.

2. You have 60 seconds to enter as many valid English words as possible using the provided letters.

3. Optional power-ups may appear randomly at the start of the round:

- Wildcard – Add or remove a letter from your set.

- Extra Time – Increases the round duration to 70 seconds.

- Double Points – Doubles your final score.

- Type quit anytime to end the game early.

# Requirements
- Python 3.x

- The words.txt file in the same directory containing a list of valid English words (one word per line).

# File Structure
WordRush.py: Main game script.

words.txt: (Required) Text file with valid words, used to check user guesses.

# Features
- Real-time input with a countdown timer

- Input validation (duplicates, non-dictionary words, illegal letter use)

- Randomly assigned power-ups for strategic gameplay

- Automatic scoring and summary display

- Score bonuses for longer words
# How to Run
python WordRush.py
or
python3 WordRush.py on Mac
