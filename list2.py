"""#looping through a list
shoppingList = ['pepper', 'ginger', 'tomatoes', 'onions', 'tissue', 'beverage']
nitems = len(shoppingList)
index = 0

while index < nitems:
    print(shoppingList[index])
    index = index + 1"""

#using for loop in lists
"""shoppingList = ['pepper', 'ginger', 'tomatoes', 'onions', 'tissue', 'beverage']

for item in shoppingList:
    print('i want to buy' + item)"""
#Write a program that starts with a list of numbers
#use a for loop to add all the numbers in the list. Print the total.
"""
numList = [23, 13, 26, 28, 10]
total = 0

for num in numList:
    total = total + num
    print('the total is ', total)"""

"""for num in range(10):
    print(num)"""

#program that allows the user to enter an integer and add the numbers up

from turtle import clear


userNum = int(input('Enter an integer: '))
sum = 0

for i in range(0, userNum):
    sum = sum + i
print(sum)