"""
Author: [Cheng Li]
Assignment / Part: HW6
Date due: 2023-03-30, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# part 1
def get_decimal_time(hours,minutes,seconds):
    total_sec = hours*3600 + minutes*60 + seconds

    french_hour = total_sec // (100*100)
    french_min = (total_sec % (100*100)) // 100
    french_sec = (total_sec % (100*100)) % 100

    french_time = str(french_hour) + ":" + str(french_min) + ":" + str(french_sec)

    return french_time

# part 2
def get_decimal_date(month,day,year):
    if month == 1:
        french_month = "Nivôse"
    elif month == 2:
        french_month = "Pluviôse"
    elif month == 3:
        french_month = "Ventôse"
    elif month == 4:
        french_month = "Germinal"
    elif month == 5:
        french_month = "Floréal"
    elif month == 6:
        french_month = "Prairial"
    elif month == 7:
        french_month = "Messidor"
    elif month == 8:
        french_month = "Thermidor"
    elif month == 9:
        french_month = "Fructidor"
    elif month == 10:
        french_month = "Vendémiaire"
    elif month == 11:
        french_month = "Brumaire"
    else:
        french_month = "Frimaire"

    french_year = year - 1792

    if 1<= day <= 10:
        french_week = 1
    elif 11 <= day <= 20:
        french_week = 2
    else:
        french_week = 3

    french_date = str(day) + " " + french_month + " Year " + str(french_year) + ", Décade " + str(french_week)

    return french_date

# part 3
def get_french_datetime(gregorian_datetime):

    hour_end = gregorian_datetime.find(":")
    hours = int(gregorian_datetime[:hour_end])

    min_start = hour_end + 1
    min_end = gregorian_datetime.find(":" , min_start)
    mintues = int(gregorian_datetime[min_start:min_end])

    sec_start = min_end + 1
    sec_end = gregorian_datetime.find(" ")
    seconds = int(gregorian_datetime[sec_start:sec_end])

    mon_start = sec_end + 1
    mon_end = gregorian_datetime.find("/")
    month = int(gregorian_datetime[mon_start:mon_end])

    day_start = mon_end +1
    day_end = gregorian_datetime.find("/",day_start)
    day = int(gregorian_datetime[day_start:day_end])

    year = int(gregorian_datetime[day_end+1:])

    time = get_decimal_time(hours,mintues,seconds)
    date = get_decimal_date(month,day,year)

    datetime = time + "\n" + date

    return datetime


def main():
    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

main()

