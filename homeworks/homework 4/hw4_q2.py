"""
Author: [Cheng Li]
Assignment / Part: HW4 - Q2
Date due: 2023-03-02, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

## Q2

g_mochiko = int(input("Enter an amount (g) of mochiko: "))
g_sugar = int(input("Enter an amount (g) of sugar: "))
g_corn = int(input("Enter an amount (g) of cornstarch: "))
g_anko = int(input("Enter an amount (g) of anko: "))

cup_mochiko = g_mochiko/220
cup_sugar = g_sugar/220
cup_corn = g_corn/220
cup_anko = g_anko/220

## cups per piece
peice_mochiko = 3/24
peice_sugar = 1.5/24
peice_corn = 2/24
peice_anko = 1/24

num_peice_mochiko = cup_mochiko // peice_mochiko
num_peice_sugar = cup_sugar // peice_sugar
num_peice_corn = cup_corn // peice_corn
num_peice_anko = cup_anko // peice_anko


if num_peice_mochiko <= num_peice_sugar and num_peice_mochiko <= num_peice_corn and num_peice_mochiko <= num_peice_anko:
    num_peice_mochi = num_peice_mochiko
elif num_peice_sugar <= num_peice_mochiko and num_peice_sugar <= num_peice_corn and num_peice_mochiko <= num_peice_anko:
    num_peice_mochi = num_peice_sugar
elif num_peice_corn <= num_peice_mochiko and num_peic_corn <= num_peice_suagr and num_peice_corn <= num_peice_anko:
    num_peice_mochi = num_peice_corn
else:
    num_peice_mochi = num_peice_anko

batch_mochi = int(num_peice_mochi // 24)

print("With this amount of ingredients, you can make", batch_mochi,"batch(es) of 24 mochi.")
