import random
print("HELLO WELCOME")
print("-"*100)

wordDit = ["Always deliver quality","Always be yourself","Audit your metrics","Build redundancy procedures","Clear the air","Dare to suck","Focus vs. scattered","Friends are treasures","Knowledge is power","Love endures delay"]
Rword = random.choice(wordDit)

for x in Rword:
    print("_",end=" ")

def printHang(wrong):
    
    if(wrong== 0):
        print("\n+---+")
        print("    | ")
        print("    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("o   | ")
        print("    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("o   | ")
        print("    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print("o   | ")
        print("|    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print("o   | ")
        print("/|    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print("o   | ")
        print("/|\    | ")
        print("    | ")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print("o   | ")
        print("/|\    | ")
        print(" |  | ")
        print("/\ ===")


def printword(guessedLetters):
    counter = 0 
    rightletters = 0
    for char in Rword:
        if(char in guessedLetters):
            print(Rword[counter],end=" ")
            rightletters+=1
        else:
            print(" ",end=" ")
        counter+=1
    return rightletters
def printlines():
    print("\r")
    for char in Rword:
        print("\u203E",end=" ")

length_word_guess = len(Rword)
amount_of_FAILURES = 0
current_guess_index = 0
current_letters_guess = []
current_letters_right = 0 

while(amount_of_FAILURES !=6 and current_letters_right != length_word_guess):
    print("\nLetters guessed right so far")
    for letter in current_letters_guess:
        print(letter, end=" ")
    letterGuessed = input ("\nplease Guess a letter")
    if(Rword[current_guess_index] == letterGuessed):
        printHang(amount_of_FAILURES)
        current_guess_index+=1
        current_letters_guess.append(letterGuessed)
        current_letters_right = printword(current_letters_guess)
        printlines()
    else:
        amount_of_FAILURES+=1
        current_letters_guess.append(letterGuessed)
        printHang(amount_of_FAILURES)
        current_letters_right = printword(current_letters_guess)
        printlines()

print("GAME OVER")