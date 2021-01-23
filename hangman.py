import random
from words import words

def get_word():
     return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False

    print(f'The word contains {len(word)} letters.')
    print(len(word) * '-')
    while guessed == False and tries > 0:
        print(f'You have {str(tries)} tries')
        guess = input('Please enter one letter or the entire word: ').lower()

        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter.')
            elif guess in letters_guessed:
                print('You have already guessed this letter.')
            elif guess not in word:
                print('This letter is not in the word.')
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print('Well done. That letter is on this word.')
                letters_guessed.append(guess)
            else:
                print(' ')
                

        elif len(guess) == len(word):
            if guess == word:
                print("That's right!!")
                guessed = True
                if input("Do you want to try again? (y/n) ") == 'y':
                    play_game()
                else:
                    print("Okay, see you soon!")
                    pass
            else:
                print("That's not the word! Try again")
                tries -= 1
            
        else:
            print('The length of your guess is not the same as the word')


        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else: 
                    status += '-'
            print(status)

        if status == word:
            print('Well done! That was the word!')
            guessed = True
        elif tries == 0:
            print('There are no more tries! Try again!')
            print(f'The word was ==> {word} <==')
            if input("Do you want to try again? (y/n) ") == 'y':
                play_game()
            else:
                print("Okay, see you soon!")
                break
            



play_game()


if input("Do you want to try again? (y/n) ") == 'y':
    play_game()
else:
    print("Okay, see you soon!")
    pass