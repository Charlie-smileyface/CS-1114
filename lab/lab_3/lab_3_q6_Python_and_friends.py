## Q6
# define inputs 
venomous = input("Is the snake venomous? [Yes/No] ")
small = input("Is the snake small? [Yes/No]" )
aggressive = input("Is the snake aggressive? [Yes/No] " )

snake = ' '
fun_fact = " "

# if statemnets ,这里有三个 input 互相组合一共有八种结果，可以通过 if else, 在一个段落中完成所有三个条件的筛选并返回结果，在最后在把根据条件赋值的 vaiables 值 print 出来 
if venomous == 'No':
    if small == 'No':
        if aggressive == 'No':
            snake = 'Python Python'
            fun_fact = "One of the largest and most famous snakes. However, they are pretty slow, and are commonly used to introduce people to learning about snakes"
            
        else:
            if aggressive == 'Yes':
                snake = 'Assembly Anaconda'
                fun_fact = "Many people hate learning about these snakes."

    else:
        if small == 'Yse':
            if aggressive == 'No':
                snake = 'Java Kingsnake'
                fun_fact = "Very befitting of their name, they are objectively the most sophisticated snake species."

            else:
                if aggressive == 'Yes':
                    snake = 'Java Treesnake'
                    fun_fact = "They are cpmpetely different from the Java Kingsnake."

else:
    if venomous == 'Yes':
        if small == 'No':
            if aggressive == 'No':
                snake = 'C Sprent'
                fun_fact = "Can be found in the sea."

            else:
                if aggressive == 'Yes':
                    snake = 'C++ Cobra'
                    fun_fact = "Evolved from the C Serpants many years ago."

        else:
            if small == 'Yes':
                if aggressive == 'No':
                    snake = 'Verilog Viper'
                    fun_fact = "Many people first see these snakes around arcitectures."

                else:
                    if aggressive == 'Yes':
                        snake = 'Matlab Mamba'
                        fun_fact = "Commonly used to introduce mecheies to working with snakes."

# dispaly
print("That is a ",snake,". ",fun_fact)
