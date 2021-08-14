# -*- coding: utf-8 -*-
import os
import random
from images_for_hangman import IMAGES
from words_for_hangman import WORDS


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    #os.system("cls")
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print(' ---------------------------------- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Choose only one word: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('You lost! The correct word was {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Congrats! You won. The correct word is: {}'.format(word))
            break


if __name__ == '__main__':
    print("LET'S PLAY SOME HANGMAN")
    run()
