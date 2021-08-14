import random

def random_word():
    """
    
    """
    
    with open("data_for_hangman.txt","r", encoding="utf-8") as f:
        all_words = f.read()
        aleatory_word = list(map(str, all_words.split()))
        aleatory_word = str.upper(random.choice(aleatory_word))

    return random_word.choice()