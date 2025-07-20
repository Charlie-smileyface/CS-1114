"""
Author: [Cheng Li]
Assignment / Part: HW5 - Q5 (etc.)
Date due: 2023-03-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import arpeggiator
ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

add_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

while add_note != "DONE":
    ARPEGGIATOR.add_note(add_note)
    add_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

print()
print(ARPEGGIATOR)
print()

direction = input("Enter an arpeggiator direction [U/D] ")
while direction != "U" and direction != "D":
    direction = input("Enter an arpeggiator direction [U/D] ")

print()


time_play = float(input("How many times do you want your arpeggiator to play? "))
while time_play <= 0 or time_play % 1 != 0:
    time_play = float(input("How many times do you want your arpeggiator to play? (Must be positive amount) "))
print()

if direction == 'U':
    for i in range(int(time_play)):
        ARPEGGIATOR.play()

else:
    for i in range(int(time_play)):
        ARPEGGIATOR.play(DOWN)

