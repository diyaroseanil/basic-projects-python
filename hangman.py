import random

words = ['cambrian','ordovician','silurian','devonian','carboniferous','permian']
x = random.choice(words)
word_display = ['_' for _ in x]
attempts = 8

print("Welcome to Hangman!")
print(' '.join(word_display))


while attempts>0 and '_' in word_display:
    print("\n"+" ".join(word_display))
    guess = input("Guess a letter:").lower()
    if guess in x:
        for index,letter in enumerate(x):
            if letter == guess:
                word_display[index]=letter
    else:
        print("The letter does not appear in this word.")
        attempts-=1

if '_' not in word_display:
    print(" ".join(word_display))
    print("You passed!")
else:
    print("Failed.")