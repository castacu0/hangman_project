# Hangman Project 🦑


<p align="center"><img src="./images/hangman.PNG" width="400px" /></p>



In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. 

In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. 

The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. 

To assist the player, a visible record of all guessed letters is typically maintained


I worked for a couple of weeks to get it done. I tried my best to follow best practices and   formatting. 


## How to use this game?

The file runs on any Linux, Windows, and MacOs bash and shell

The `core.py` executable expects a dictionary file as argument. Here you can edit the words as pleasure.

```
./hangman/hangman_words.py
```

Hangman will import the dictionary file & select a random word from it. Then it will show you the random word, the ASCII code, & your tries left. 

Then, it will ask you to input a letter.

Example running:

```
*******
Tries: 10
Your letter: a
a is not in the word.

*******
Tries: 9
Your letter: e

*e*****
Tries: 9
Your letter:
```

## ASCII Images and Words

You can find dictionary files samples to edit as pleasusre in the `hangman_words` and `hangman_images` modules.

These dictionaries are basically a list of word separated by new lines (`\n`), or by commas.

Example:

```
keyboard
hospitality
chance
divorce
ensure
embrace
corner
middle
deposit
knock
instrument

'''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''',
'''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========= ''',



> Any comment or feedback is well accepted
