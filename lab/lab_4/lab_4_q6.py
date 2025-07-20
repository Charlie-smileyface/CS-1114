## Q6
import random

print("Welcome to Blackjack")

dealer_card_sum = random.randrange(2,22)

player_card_sum = 0 ## 为了逻辑顺序，尽量在循环开始前给上空值，然后所有的运算都放到循环当中进行

if_continue = " " ## 因为在循环开始是要使用到这个变量的值所以要在循环开始之前 define 一下这个变量，一般给 empty value 即可


while player_card_sum < 21 and if_continue != 'STAND':

    new_card = random.randrange(1,12)
    player_card_sum += new_card
    
    print("Your current card sum is:",player_card_sum)
    if_continue = input("What would you like to do next?: (DEAL, STAND) ")  ## 在构建循环时，当 input variable 是作为是否进入下一轮循环的条件的话，那必须把这个 input 放在循环的最后一行，因为要确保当决定不进入下一轮循环时，这个 input后面的代码不被运行



if dealer_card_sum < player_card_sum < 21:
    print("You won! Your card sum was",player_card_sum ,"and the dealer's was",dealer_card_sum)

elif player_card_sum == dealer_card_sum:
    print("You tie! Your card sum was",player_card_sum ,"and the dealer's was",dealer_card_sum)

else:
    print("You lost! Your card sum was",player_card_sum ,"and the dealer's was",dealer_card_sum)
