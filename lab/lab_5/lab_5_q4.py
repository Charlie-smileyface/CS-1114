## Q4

import random

for row in range(1,11):

    result = ''
    rand_num = random.random()

    if rand_num > 0.5:
        for column in range(1,row+1):
            result += str(row*column) + "\t"
        print(result)

    else:
        for column in range(row,1-1,-1):
            result += str(row*column) + "\t"
        print(result)

    



















































