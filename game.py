import forca
import guessing
def choice_game():
    print("**********************************")
    print("****** Choice your GAMER! ********")
    print("**********************************")

    print("(1) Forca  (2) Guessing")

    game = int(input("What's your choice: "))
    if game == 1:
        print("Forca GAME!")
        forca.gamer()
    elif game == 2:
        print("Guessing GAME!")
        guessing.gamer()
    else:
        print("Choice a number 1 or 2, please!")

if (__name__ == "__main__"):
    choice_game()