import random
import hangman_words
import hangman_art

print(hangman_art.logo)
print("Welcome to Hangman!")
chosen_word = random.choice(hangman_words.word_list)

display = []

for letters in chosen_word:
    display.append('_')

print(f"{' '.join(display)}")
print(hangman_art.stages[-1])
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You have already guessed {guess}.')

    for pos in range(len(chosen_word)):
        if guess == chosen_word[pos]:
            display[pos] = guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f'You guessed {guess}, which is not in the word. Life -1!')
        lives -= 1
        print(f'You have {lives} more lives.')
        print(hangman_art.stages[lives])

    # Join all the elements in the list and turn it into a String.

    if '_' not in display:
        print('You Win!')
        end_of_game = True
    elif lives == 0:
        print(f'You Lose! Word was {chosen_word}')
        end_of_game = True

