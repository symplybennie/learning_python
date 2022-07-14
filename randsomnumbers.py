
from random import random


nFlips = 0      #count the number of flips
nHeads = 0      #count the number of heads
nTails = 0      #count the number of tails
maxFlips = int(input("ENter maximum nuber of flips: "))

while nFlips < maxFlips:
    zeroOne = random.randrange(0, 2)
    if zeroOne == 0:
        nHeads = nHeads + 1
    else:
        nTails = nTails + 1
nFlips += 1
print("Number of nFlips are: ", nFlips, "Number of Head and Tail Tosses are: ", nHeads, nTails)