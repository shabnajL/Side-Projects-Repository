import math
import random

number = random.randint(1, 100)
guess_chance = math.log(100 - 1 +1, 2)
print("You've only",round(guess_chance), "chances to try!")

count_guess = 0
while(count_guess < guess_chance):
    guess = int(input("Guess a number between 1 and 100: "))

    count_guess+=1

    if(guess > number):
        print("Too high! Try Again.")
    elif(guess < number):
        print("Too Low! Try Again.")
    else:
        if(count_guess==1):
            print("GG! You did it in ",count_guess,"try")
        else:
            print("GG! You did it in ",count_guess,"tries")
        break

if(count_guess>guess_chance):
    print("\nBig Oops!\nThe number is: ",number,"\nBetter luck next Time!\n")
