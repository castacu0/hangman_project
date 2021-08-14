import os
import sys
import random

def aleatory_word():
    with open("data_for_hangman.txt","r", encoding="utf-8") as f:
        all_words = f.read()
        aleatory_word = list(map(str, all_words.split()))
        aleatory_word = str.upper(random.choice(aleatory_word))

length = len(aleatory_word)
print("Length: {}".format(length))

underscore = "— " * length
print(f" ---> {underscore}")

def user_input():
    var_userinput = str(input("Give only one letter: "))
    var_userinput = var_userinput.upper()
    try:
        if len(var_userinput) == 1:
            print("OK len")
            
    except:
        print("Oops", sys.exc_info()[0], "occurred")


# def clean():
#     os.system("cls")
#     print("Cleaner in use")
#     user_input()
#     print("Reprompting")


def run():
    user_input()
        
    for i in aleatory_word:
        if "var_user_input" in aleatory_word:
            print("Running 1")
            return user_input()
            print("Running 2")

        elif "user_input" not in aleatory_word:
            print("This letter is not in the word.")
            return user_input()


if __name__ == "__main__":
    run()