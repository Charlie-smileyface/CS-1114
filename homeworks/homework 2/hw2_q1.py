"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q1
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import math

# define inputs
frequency_w = float(input("Enter a value for the frequency, w: "))
duration_t = float(input("Enter a value for the duration, T: "))

# calculation
result = 2 * math.sin(frequency_w * duration_t) / frequency_w

# display
print("The amplitude spectrum of this Fourier transform is: ",round(result,3))
