## Q2
# define inputs
garage = input("Which garage did you parked in? [North/South]")
print("Please enter the hour, followed by minutes, you entered the garage (military time):")
hour_enter = int(input())
min_enter = int(input())

print("Please enter the hour, followed by minutes, you left the garage (military time):")
hour_left = int(input())
min_left = int(input())

total_min = (hour_left - hour_enter)*60 + min_left - min_enter

# if statements : if 后面套 if，是在第一个if运行的条件下，开始进行后面这一整个block的if条件筛选。
if garage == 'North':
    if total_min < 15:
        parking_cost = 0  # 这里不需要每一个if下面都写出来要print的话，可以直接赋值一个 variable, 运行不同的条件会给到 variable 不同的赋值，最后再print出来 
    elif hour_enter > 9 and hour_left < 19:
        parking_cost = 14
    elif total_min < 60:
        parking_cost = 6
    elif total_min < 120:
        parking_cost = 8
    elif total_min < 240:
        parking_cost = 10
    elif total_min < 720:
        parking_cost = 16
    else:
        parking_cost = 'error_1'

elif garage == 'South':
    if total_min < 15:
        parking_cost = 0
    elif hour_enter > 9 and hour_left < 19:
        parking_cost = 16
    elif total_min < 60:
        parking_cost = 8
    elif total_min < 120:
        parking_cost = 10
    elif total_min < 240:
        parking_cost = 12
    elif total_min < 720:
        parking_cost = 18
    else:
        parking_cost = 'error_1'

else:
    parking_cost = "error_2"

# another if statemnet : 在条件中如果还存在执行要print的内容的话，可以给原有变量一个赋值，然后再用另外一个if statement 来承接，if variable = 什么则print什么
if parking_cost == "error_1":
    print("Invalid parking time")
elif parking_cost == "error_2":
    print("invalid garage")
else:
    print("Your total parking cost will be: ",parking_cost)
