## Q5
price = 5

# 分三大项检验，在大项中再用 if 语句检验小项
is_rarity = input("Welcome to the Pokémon card price calculator! Is your card of a special rarity? (Y/N): ")

# if statement 1 检验第一大项，根据检验结果我们的目标变量值在进行筛选过后发生变化(条件发生）或者不变（条件不发生）
if is_rarity == 'Y':
    is_uncommon = input("Is your card uncommon? (Y/N); ")
    if is_uncommon == 'Y':
        price += 5 ## += 代表 price = price + 5, 这个运算符号同样也可以应用与（-, *, /)
    else:
        is_rare = input("Is your card rare? (Y/N): ")
        if is_rare == 'Y':
            price += 15


# if statement 2 检验第二大项  第二个大项有三个小项要进行选择，但是这里不能用 elif 因为中间要加 input, 所以只在else: 后面加，然后再多套一层 if statement,相当于在一个一个的验证小项的input
is_holo = input("Is your card holographic? (Y/N): ")
if is_holo == 'Y':
    is_reverse = input("Is your card reverse holos? (Y/N): ")
    if is_reverse == 'Y':
        price += 10
    else:
        is_holos = input("Is your card holos? (Y/N): ")
        if is_holos == 'Y':
            price += 15
        else:
            is_full_holos = input("Is your card full holos? (Y/N): ")
            if is_full_holos == 'Y':
                price += 20

# if statement 3
is_special = input("Is your card of a special Pokémon? (Y/N): ")
if is_special == 'Y':
    is_starter = input("Is your card starter? (Y/N): ")
    if is_starter == 'Y':
        price += 5
    else:
        is_legend = input("Is your card of a legendary? (Y/N): ")
        if is_legend == 'Y':
            price += 30

# dispaly
print("Your card has a final resale price of: ",price,"$")
