"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q3
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q3
# define inputes
semi_day = int(input("Please enter the number of days Semi has worked: "))
semi_hour = int(input("Please enter the number of hours Semi has worked: "))
semi_min = int(input("Please enter the number of minutes Semi has worked: "))

daniel_day = int(input("Please enter the number of days Daniel has worked: "))
daniel_hour = int(input("Please enter the number of hours Daniel has worked: "))
daniel_min = int(input("Please enter the number of minutes Daniel has worked: "))

# calculations
total_min = (semi_min + daniel_min) + (semi_hour + daniel_hour)*60 + (semi_day + daniel_day)*24*60

total_day = total_min // (24*60)
min_left = total_min % (24*60)
total_hour = min_left // 60
total_min = min_left % 60


print("The total time both of them worked together is: ",total_day,"days,",total_hour,"hours and",total_min,"mintues")
