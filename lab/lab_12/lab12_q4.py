def create_grocery_inventory():
    user_input = input("Please enter the item and quantity you own separated by a comma or DONE when complete: ")
    dict = {}
    while user_input != "DONE":
       lst = user_input.split(",")
       item_name = lst[0]
       item_amount = int(lst[1])
       if item_name not in dict:
           dict[item_name] = item_amount
       else:
           dict[item_name] += item_amount

       user_input = input("Please enter the item and quantity you own separated by a comma or DONE when complete: ")
    return dict
       
def create_grocery_shopping_list(fridge_inventory):
    buy_dict = {}
    user_input = input("Please enter the item and quantity you desire separated by a comma or DONE when complete: ")
    while user_input != "DONE":
       lst = user_input.split(",")
       item_name = lst[0]
       item_desire_amount = int(lst[1])
       amount_to_buy = 0

       if item_name not in fridge_inventory:
          buy_dict[item_name] = item_desire_amount
       else:
          if fridge_inventory[item_name] >= item_desire_amount:
             buy_dict[item_name] = 0
          else:
             buy_dict[item_name] = item_desire_amount - fridge_inventory[item_name]
        
       user_input = input("Please enter the item and quantity you desire separated by a comma or DONE when complete: ")
    return buy_dict

def main():
 fridge_inventory = create_grocery_inventory()
 print()
 grocery_list = create_grocery_shopping_list(fridge_inventory)
 print()
 print("Your shopping list, based off of what you have in your fridge, should be: ")
 print(grocery_list)
main()
