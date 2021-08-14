import os
import random

with open("data_for_hangman.txt","r") as f:
    all_words = f.read()
    words = list(map(str, all_words.split()))
    words = random.choice(words)
    words = words.upper()
    print(words)

def cleaner():
    os.system("cls")

aleatory_word = words
user_input = ""
lives = 7
tries = 0

length = len(aleatory_word)
print(length)
underscore = "_ " * length
print(f"---> {underscore}")

#str.replace("_", new)
def saver():
    if user_input in aleatory_word:
        return aleatory_word.replace("_ ", user_input)
    else:
        print("continue")


user_input = str(input("Guess the word: "))
user_input = user_input.upper()

def run():
    global user_input
    global aleatory_word
    global lives
    global tries
    if user_input in aleatory_word:
        print("Running")
        # aleatory_word.replace("_ ", user_input)
        lives -= 1
        if lives > 0:
            tries += 1
            # user_input = input("Guess the word: ")
            saver()
            # if user_input in aleatory_word:
                #I have to show every letter
            # cleaner()
                # if :
                #     print("You have", lives, "lives remaining") # or life
                
        elif lives == 1:
            print("You have", lives, "life remaining") # or life

        elif lives <= 0:
            print(f"You lost, the word was: '{aleatory_word}'")
            # break
    else:
        print("This letter is not in the word.")


    if user_input == aleatory_word:
        if tries == 1:
            print(f"Congrats, you won with {tries} try") # or try
        else:
            print(f"Congrats, you won with {tries} tries!") # or try

if __name__ == "__main__":
    run() 



#Translate

#Change data__hangman

#len()
#only one letter as input not more