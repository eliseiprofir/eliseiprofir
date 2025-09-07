import random

# List of words to guess
words: list[str] = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Random choose a word from the list
chosen_word: str = random.sample(words)
word_display: list[str] = ['_' for _ in chosen_word]  # Create a list of underscores
attempts: int = 8  # Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess: str = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word!")
        attempts -= 1

if '_' not in word_display:
    print("You guessed the word:")
    print(chosen_word)
    print("You survived!")
else:
    print("You ran out of attempts. The word was:", chosen_word)
    print("You died!")
