"""
## Problem 1
#(1) Binary to decimal (01011010)
decimal = 1*2**6 + 1*2**4 + 1*2**3 + 1*2**1 = 90

#(2) Decimal to binary (153)
binary = 10011001

#(3) Binary to Hexadecimal (10100111)
hexadecimal = a7

#(4) Hexadecimal to binary (0*DFA)
binary = D*16**2 + F*16**1 + A*16**0 = 13*16**2 + 15*16 + 10*1 = 3578

#(5)Decimal to Octal(base 8) (229)
octal = 345

## Problem 2
A=True
B=False
C=False
#(1) (A and B or C) or (C and A)
(T and F or F) or (F and T) = (F or F) or F = False

#(2) not(C and A) and (4*5>=20)
not(F and T) and T = not F and T = T and T = True

#(3) (3+3==5) or (C or B and A) or (3*3==9)
F or (F and T) or T = F or F or T = True

#(4) (not("")) or (A and 0) or (A or B),       ("")和 0 都代表 False.
(not("")) or (A and 0) or (A or B) = not(F) or F or T = T or F or T = True
"""

## Problem 3
import random

random_number = random.randint(0,100) ##先引入 random，然后根据上下线构建一个随机数变量，random.randint( )生成的数是上下限都包括在内的

even_check = random_number % 2 == 0 ## 判断生成的随机数是不是偶数，且需要返回的答案为Boolean，可以通过mod除2，看看结果是否为零且加入运算符号==0，来让结果呈现为Boolean。
greater_than_50_check = random_number > 50  ## 同样需要呈现boolean，所以还是通过运算符号来实现

print(str(random_number) + " is even: " + str(even_check))
print(str(random_number) + " is greater than 50: " +str(greater_than_50_check))


## Problem 4
import random

decimal_integer = int(input("Enter a decimal integer less than 100: "))

num_L = decimal_integer // 50  # 算出转化后结果里面有几个L就要看，这个随机数整除50，得几就说明有几个L
num_X = (decimal_integer % 50) // 10 # 而后面X的个数就是随机数整除50的余数再去整除10，看能整除几倍的十就是有几个X
num_V = (decimal_integer % 50 % 10) // 5  
num_I = (decimal_integer % 50 % 10 % 5) // 1  

print(str(decimal_integer) + " is convert to: " + "L"*num_L + "X"*num_X + "V"*num_V  + "I"*num_I)


## Problem 5
import random
import math

height_wall = float(input("Enter the height of the wall: "))
distance_wall_ladder = float(input("Enter the distance between the wall and the ladder: "))

min_ladder_height = math.sqrt(height_wall**2 + distance_wall_ladder**2)

# 这里有两个条件要被同时满足，一个是满足40%的概率在那里有ladder，并且这个ladder的长度 > reach roof 的min height，这两个条件variables的值一定是T/F.
check_avaiable = random.randint(1,100) < 40  # 满足40%的概率就是从0-100中生成一个随机数，而这个随机数 < 40 or > 60
check_height = random.randint(1,100) > min_ladder_height 

check_reach_the_roof = check_avaiable and check_height # 这里用 and 来使两个条件联立,两个条件同时满足是才会return True.

print("From a distance of " + str(distance_wall_ladder) + " meters and a wall height of " + str(height_wall) + " meters, can we reach the roof?: " + str(check_reach_the_roof))


## Problem 6
import math

pi = math.pi
e = math.e

x=0.0
fx = 1/math.sqrt(2*pi)*math.pow(e,-1/2*x**2)  ## 这里要用到数学表达式，指数，在开头先define 出来想用的数学常数，后面运算会变简单
print("The value of the pdf at x= 0.0 is: " + str(fx))

x=1.0
fx = 1/math.sqrt(2*pi)*math.pow(e,-1/2*x**2)
print("The value of the pdf at x=1.0 is: " + str(fx))

x=-1.0
fx = 1/math.sqrt(2*pi)*math.pow(e,-1/2*x**2)
print("The value of the pdf at x=-1.0 is: " + str(fx))


## flip coin
import random

random_number = random.random( ) ## random.dandom( ) 是生成一个在0-1之间的随机数，不包括1
result = round(random_number)  # round 是自带的功能，不需要引入 math modoule,可以直接使用，作用就是讲float四舍五入
print(random_number)
print(result)

# 这里 head 和 tail 这两个便量都是Boolean了，结果取决于后面的条件，结果为T/F
head = result == 1
tail = not(result == 1) # 这里也可以是 tail = result != 1

print("This flip result in a head: " + str(head))
print("This flip result in a tail: " + str(tail))
































