"""from ast import Num
from turtle import right
"""

def guessNum():
    num = ""
    guessLimit = 4
    rightNum = 20
    guessCount = 0
    
    while num != rightNum:
        num = int(input("Take a guess: "))
        guessCount += 1
        #print(num)
        if guessCount == guessLimit:
            print("Your LOSE!!")
            break
        else:
            if num == 1 or num <= 16:
                print("Your guess is low")
            elif num == 17 or num <= 19:
                print("Your guess is high")
            else:
                print("Your guess is right")
        
            
        
guessNum()