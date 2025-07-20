"""
Author: [Cheng Li]
Assignment / Part: HW1 - Q2
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Q2
# Define inputs
year_input = int(input("Please enter a year greater than 2023: "))

# define variables
current_population = 330109174
birth_sec = 1/7
death_sec = 1/15
immigrant_sec = 1/42
emigration_sec = 1/(1.25*60)

sec_year = 60*60*24*365

birth_year = birth_sec*sec_year
death_year = death_sec*sec_year
immigrant_year = immigrant_sec*sec_year
emigration_year = emigration_sec*sec_year

#calculations
change_population_year = birth_year - death_year + immigrant_year - emigration_year
diff_year = year_input - 2023

estimated_population = int(current_population + change_population_year*diff_year)

#dispaly
print("The population in year " + str(year_input) + " will be: " + str(estimated_population))
