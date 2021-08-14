#! .env/bin/python
# Adrian Andres AROESTI 2019

# requierements.txt
# requests
# unidecode

import random
import requests
import unidecode

IMAGES = ['''You know what is here''']


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print('------------------------------------------------------------------------')
    print(IMAGES[tries])
    print('')
    print(hidden_word)


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Choose a letter: '))

        letter_indexes = []
        for idx in range(len(word)):
            # In Spanish there are words with accents, such as "computación", we compare without these.
            if unidecode.unidecode(word[idx]) == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('You lose! the correct word was {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Congratulations! You win, the correct word is: {}'.format(word))
            break


if __name__ == '__main__':
    # Select the language
    print('1 = Inglés')
    print('2 = Español')
    idioma = int(input('Choose a language of the source words (1 o 2): '))

    if idioma == 1:
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    elif idioma == 2:
        word_site = "https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/palabras_todas.txt"
    else:
        print("This language not exists")
        exit()

    # Getting the selected contend
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    # Words must be in UTF-8
    WORDS = list(map(lambda palabra: palabra.decode('utf-8'), WORDS))

    print('------------------------------------------------------------------------')
    print('|                W E L C O M E   T O   P Y H A N G M A N               |')
    run()
