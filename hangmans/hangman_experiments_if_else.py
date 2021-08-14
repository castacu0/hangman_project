# Videogame with Lives, Tries and using 'or'
import random

with open("data_for_hangman.txt","r") as f:
    all_words = f.read()
    words = list(map(str, all_words.split()))
    words = random.choice(words)
    words = words.upper()
    print(words)

def run():
    # aleatory_num = random.randint(1,10)
    aleatory_word = words
    general_saver = ""
    lives = 4
    tries = 1
    user_input = str(input("""Choose one letter"""))

    while user_input != aleatory_word:
        lives-=1 #Every loop it subtracts one life.
        tries+=1 #Every loop it adds one try.
        if user_input < 1 or user_input > 10 or lives == 0: 
            print("--- /// You lost /// ---")
            print("The aleatory number was", aleatory_word)
            break
        elif user_input < aleatory_word:
            print("Look for a 'Higher' number")
        elif user_input > aleatory_word:
            print("Look for a 'Lower' number")
        print("You have", lives, "lives remaining")
        user_input = int(input("Choose other number: ")) 

    if user_input in aleatory_word:
        if user_input in aleatory_word: 
              print("--")
              general_saver = general_saver + user_input
              return general_saver
        elif user_input < aleatory_word:
            print("Look for a 'Higher' number")
        print("Letter here")

    if user_input == aleatory_word:
        print("--> YOU WON <-- With", tries, "tries.")


if __name__ == "__main__":
    run()