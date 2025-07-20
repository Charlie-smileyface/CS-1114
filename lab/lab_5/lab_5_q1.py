#Q1

for i in range(4):
    for j in range(4):
        print(i*j , end = ' ')
    print()  ## 为了让他print出来是一个四乘四的矩阵，因为再上一个循环的print里面是写成一行每个之间隔一个空格，
             ## 所以这行print就是再接在上面一行的print后面接一个空格，这个空格是接在上面一行的，而这个print没有限制结尾，所以当再进入下一轮循环时，
             ## 上一面一行 j 的循环print出来的东西另起一行，从而实现4*4矩阵的格式


    
for i in range(5):
    for j in range(i+1,5):
        print(i,j) ## 注意这个print的位置，是在这个J loop的下面，所以当每一个 i 取值跑完整个 j loop之后才会再进入下一个 i 值




for i in range(1,10):
    if i % 2 == 0:
        for j in range(i,10,2):
            print(j, end=' ')
        print()


for i in range(1,10):
    if i % 2 == 0:
        for j in range(0,i,2):
            print(j, end=" ")
        print()
