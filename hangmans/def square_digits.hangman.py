aleatory = "barco"
aleatory = aleatory.upper()
user_letter = str(input("A letter: "))

def find_if_inside(letter):
    ansX = ""
    # for x in str(letter):
    for x in letter:
      if x in aleatory:
        print("inside")
        # ansX += str(int(x)**2)
        # ansX = ansX + str(int(x)**2)
      else:
        print("not letter")
        break
    return str(ansX)

find_if_inside(user_letter.upper())
