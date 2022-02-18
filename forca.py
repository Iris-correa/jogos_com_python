import random
import time
import game

def gamer():
    
    welcome()
    category_answer = what_your_category()
    
    if category_answer == 1:
        words = if_choice_1()
    elif category_answer == 2:
        words = if_choice_2()
    elif category_answer == 3:
        words = if_choice_3()
    elif category_answer == 4:
        words = if_choice_4()
    elif category_answer == 5:
        if_choice_5() 
    
    secret_word = storage_secret_word(words) 
    
    right_letters = started_right_letters(secret_word)
    print(right_letters)
    
    die = False
    right = False
    wrongs = 0

    while not die and not right:
        
        guess = ask_guess()

        if guess in secret_word:
            right_guess(secret_word,guess,right_letters)
            miss_letters = how_many_letters(right_letters)
            print(right_letters)
            print(f'\nStill need to get it right {miss_letters} letters.\n')
        else:
            dranw_forca(wrongs)
            wrongs += 1
        
        die = wrongs == 6
        right = "_" not in right_letters
        
    if right:
        you_win()
    else:
        you_lost(secret_word)  
         
def welcome():
    file = open("welcome.txt", "r")
    for line in file:
        time.sleep(1)
        print(line)

def what_your_category():
    print("\n What's your category?\n")
    print("(1) Animals  (2) Fruts  (3) Objects  (4) Eletronics (5) Menu principal")
    category_answer = int(input("Category: "))
    return category_answer

def if_choice_1():
    animals_file = open("bd_animals.txt", "r")
    words = []
    for line in animals_file:
        line = line.strip()
        words.append(line)
        
    animals_file.close()  
    return words
            
def if_choice_2():
    fruts_file = open("bd_fruts.txt", "r")
    words = []
    for line in fruts_file:
        line = line.strip()
        words.append(line)
        
    fruts_file.close()
    return words 
            
def if_choice_3():
    objetcs_file = open("bd_objetcs.txt", "r")
    words = []
    for line in objetcs_file:
        line = line.strip()
        words.append(line)
        
    objetcs_file.close() 
    return words
            
def if_choice_4():
    eletric_file = open("bd_eletric.txt", "r")
    words = []
    for line in eletric_file:
        line = line.strip()
        words.append(line)
        
    eletric_file.close() 
    return words

def if_choice_5():
    game.choice_game()

def storage_secret_word(words):
    number = random.randrange(0,len(words))
    secret_word = words[number].upper() 
    return secret_word

def started_right_letters(secret_word):
      right_letters = ["_" for letter in secret_word]
      return right_letters

def ask_guess():
        guess = input("Guess a letter: ")
        guess = guess.strip().upper()
        return guess

def how_many_letters(right_letters):
    miss_letters = str(right_letters.count('_'))
    return miss_letters
    
def dranw_forca(wrongs):
    print("  _______     ")
    print(" |/      |    ")

    if(wrongs == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(wrongs == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrongs == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
    
def you_win():
    print("*** CONGRATSS, YOU WIN! ***")
    print("       ___________       ")
    print("      '._==_==_=_.'      ")
    print("      .-\\:      /-.     ")
    print("     | (|:.     |) |     ")
    print("      '-|:.     |-'      ")
    print("        \\::.   /        ")
    print("         '::. .'         ")
    print("           ) (           ")
    print("         _.' '._         ")
    print("        '-------'        ")

def you_lost(secret_word):
    print("OH NOOO! Your change is OVER! TRY AGAIN!")
    print(f"The right word was {secret_word}")
    print('****** GAME OVER *********')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('****** GAME OVER *********') 

def right_guess(secret_word,guess,right_letters):
    index = 0
    for letter in secret_word:
        if guess == letter:
            right_letters[index] = letter
        index = index + 1
       

if(__name__ == "__main__"):
    gamer()