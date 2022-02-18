import random
import game
def gamer():
     
    print("**********************************")
    print("***** Welcome Guessing Game! *****")
    print("**********************************")

    random_number = random.randrange(1,101)
    secret_number = random_number
    trying = 3
    points = 1000

    print("What's your difficult level?")
    print("(1) Easy  (2) Normal  (3) Difficult  (4) Hard")
    answer_level = int(input("Level: "))

    if answer_level == 1:
        trying = 20
    elif answer_level == 2:
        trying = 10
    elif answer_level == 3:
        trying = 5
    elif answer_level == 4:
        trying = 3
    elif answer_level == 5:
        game.choice_game()
        
    for step in range (1, trying + 1):
        print("Try {} of {} ".format(step , trying))
        guess_str = input("Write your number between 1 and 100: ")
        print("Your guess number was: ", guess_str)
        guess = int(guess_str)
        
        if guess < 1 or guess > 100:
            print("WRITE A NUMBER BETWEEN 1 AND 100, PLEASE!")    
            continue
        
        right = secret_number == guess
        wrong_below = secret_number > guess
        wrong_under = secret_number < guess

        if right:
            print("Excenllent! You're RIGHT and you make {} points!)".format(points))  
            break
        else:
            if wrong_below:
                print("Your guess is below the secret number, try again!!")
            elif wrong_under:
                print("Oh no! Try again, your guess is under the secret number :c")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print(f"GAME OVER! The Secret Number was {secret_number}")           

if(__name__ == "__main__"):
    gamer()