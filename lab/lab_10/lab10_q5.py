def organize_into_profits_losses(lst):
    output_lst = []
    inside_lst = []
    inside_sum = 0
    for element in lst:
        if (element >= 0 and inside_sum >=0) or (element < 0 and inside_sum < 0):
            inside_lst.append(element)
            inside_sum += element
        else:
            output_lst.append(inside_lst) # 每当正负发生变化时，把之前的 inside lst append 到 output当中

            inside_lst =[]
            inside_lst.append(element)
            inside_sum = element
    
    output_lst.append(inside_lst) # 把最后一组的inside lst append 进去
    return output_lst

def spending_statistics(lst_lsts):
    profit_count = 0
    loss_count = 0
    balance = 0

    for element in lst_lsts:
        acc = 0
        for num in element:
            acc += num
        balance += acc    
        if acc >= 0:
            profit_count += 1
        else:
            loss_count += 1
    print(f"You have had {profit_count} periods of subsequent profit.")
    print(f"You have had {loss_count} periods of subsequent losses.")
    print(f"Total balance: {balance}")
    if balance > 0:
        print("You're doing great! Keep it up!")
    else:
        print("You are loosing money!")

def main():
    weeks_lst = [1, 4, -2, 3, -3, -5, 3]
    organized_weeks_lst = organize_into_profits_losses(weeks_lst)
    print("Here are your spending habits over the last few weeks:", organized_weeks_lst)
    spending_statistics(organized_weeks_lst)
main()