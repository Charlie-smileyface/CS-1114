"""
Author: [Cheng Li]
Assignment / Part: HW3 - Q5
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q5
import random

if_play = input("Would you like to play 'Twenty-One'? [y/n] ")

while if_play != 'y' and if_play != 'n':
    if_play = input("Invalid input! Would you like to play 'Twenty-One'? [y/n] ")


if if_play == 'n':
    print("Thank you for playing!")

else:
    card1 = random.randrange(1,12)
    card2 = random.randrange(1,12)
    print("Your cards are worth " + str(card1) + " and " + str(card2) + ".")

    third_card = input("Would you like another card? [y/n] ")

    while third_card != 'y' and third_card != 'n':
        third_card = input("Invalid input! Would you like another card? [y/n] ")

    if third_card == 'y':
        card3 = random.randrange(1,12)
        total_score = card1 + card2 + card3
        print("Your score is " + str(total_score) + "!")

    else:
        total_score = card1 + card2
        print("Your score is " + str(total_score) + "!")


    opponent_score = random.randrange(0,101)
    
    while opponent_score < 3 or opponent_score > 33:
        opponent_score = random.randrange(0,101)

    print("Your opponent's score is " + str(opponent_score) + "!")

    if total_score == 21 and opponent_score != 21:
        print("You win! Your score was " + str(total_score) + ".")

    elif opponent_score == 21 and total_score != 21:
        print("Your opponent wins! Their score was " + str(opponent_score) + ".")

    elif total_score < 21 and opponent_score > 21:
        print("You win! Your score was " + str(total_score) + ".")

    elif opponent_score < 21 and total_score > 21:
        print("Your opponent wins! Their score was " + str(opponent_score) + ".")

    elif (total_score < 21 and opponent_score < 21) and (total_score > opponent_score):
        print("You win! Your score was " + str(total_score) + ".")

    elif (total_score < 21 and opponent_score < 21) and (total_score < opponent_score):
        print("Your opponent wins! Their score was " + str(opponent_score) + ".")

    else:
        print("It's a draw!")

    
