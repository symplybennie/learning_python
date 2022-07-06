"""
The goal of the program is to calculate the sum of the numbers from 1 through the target 
number
"""


def sumNum():
    num = int(input("Enter your num: "))
    sum = 0
    count = 1
    #if count != num:
    while count <= num:
        sum = sum + count
        count += 1
    #else:
        print("Your Total Sum is: ", sum)

            
sumNum()