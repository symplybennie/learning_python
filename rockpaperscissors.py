import random
"""randomChoice = ""
choiceNumber = random.randrange(0, 3) # to get a 0, 1, or 2
if choiceNumber == 0:

 randomChoice = 'rock'
elif choiceNumber == 1:
 randomChoice == 'paper'
else: # not zero and not one, must be 2
 randomChoice == 'scissors'"""

randomAnswer = random.randrange(0, 8) # pick a random number between 0 and 7
if randomAnswer == 0:
 print('It is certain.')
elif randomAnswer == 1:
 print('Absolutely!')
elif randomAnswer == 2:
 print('You may rely on it.')
elif randomAnswer == 3:
 print('Answer is foggy, ask again later.')
elif randomAnswer == 4:
 print('Concentrate and ask again.')
elif randomAnswer == 5:
 print('Unsure at this point, try again.')
elif randomAnswer == 6:
 print('No way, dude!')
else: # must be 7
 print ('No, no, no, no, no.')