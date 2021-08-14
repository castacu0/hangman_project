import os


# Have to use the random module or loop with Open
# Add comprehensions list/dic
# I have to convert the given letter to capital
# If I don't get 1 one, erase me one life 
# If the user gives me a number, I have to cut the game or put a try/except
#     "C:\Users\Cesar Castanon\courses\python_course\basic_python_pl\random_videogame.py"
# Have to handle errors
# I have to connect to other file

# >>> use enumerate
# >>> get method from dicts
# os.system("cls") on Win or os.system("clear") on Linux
# Read the docmentation

with open("data_for_hangman.txt","r") as f:
    for line in f:
        stripped_line = line.strip() #remove smthing
        print(stripped_line) 


    while user_word != aleatory_word:

    if user_word == aleatory_word:
        return f"Congrats, you won with {tries} tries!"

def cleaner():
    os.system("cls")

cleaner()

def mom():
    print(f"mom")

def run():
    mom()
    print(f"run")

if __name__ == "__main__":
    run() 