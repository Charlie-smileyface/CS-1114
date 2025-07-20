"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q6
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q6
day_week = input("Enter the day the call started at: ")
time_start = int(input("Enter the time the call started at (hhmm): "))
length_call = int(input("Enter the duration of the call (in minutes): "))

if day_week == 'Mon' or day_week == 'Tue' or day_week == 'Wed' or day_week == 'Thr':
    if time_start >= 530 and time_start <= 2100:
        cost_per_min = 0.55
    else:
        cost_per_min = 0.35

else:
    cost_per_min = 0.1

total_cost = cost_per_min * length_call

print("This call will cost $" + str(round(total_cost,1)))
