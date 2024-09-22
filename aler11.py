import random

list=['rock','scissors','paper']

cpuScore = 0

userScore=0

pps=True

while pps==True:

    guess = input('Lets play game,Enter rock or paper or scissors  :')

    cpu=random.choice(list)

    

    if guess==cpu :
        
        result = ('Draw')

        

    elif guess=='rock':

        
        
        if cpu=='paper' :

            result=('lose')

        if cpu == 'scissors':

            result=('win')

    elif guess == 'paper':

        

        if cpu == 'scissors' :

            result=('lose')

        if cpu == 'rock' :

            result=('win')   

    elif guess == 'scissors' :

        
         
        if cpu == 'rock' :
             
                result=('lose')

        if cpu == 'paper' :

            result=('win')   

    else :

        result=('wrong answer')  

    

    if result != 'wrong answer' :
         print (cpu)

    print (result)


    if result=='Draw' :

        cpuScore+=0

        userScore+=0

    elif result=='win' :

        cpuScore+=0

        userScore+=1

    else :

        cpuScore +=1

        userScore +=0

    print(cpuScore)

    print(userScore)







