import random 
import string

def password_generator():
    """
    It returns one or several passwords
    based on the numbers the user inputs
    when asked to do so
    """
    charactersY = string.ascii_letters + string.digits + string.punctuation

    while 1:
        lengthX = int(input("\nWhat length do you want your password to be? "))
        total_of_passwordsX = int(input("How many passwords you need? "))
        print("\n")

        for x in range(0, total_of_passwordsX): 
            password = "" 
            for i in range(0, lengthX): 
                password_charactersX = random.choice(charactersY)
                password = password + password_charactersX
            print("Here is your password: " + password)
        print("\n")
        break

def run():
    password_gen = password_generator()


if __name__ == '__main__':
    run() 