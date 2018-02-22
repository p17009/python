num1 = int(input("input 5 numbers: ")
import random


gridSize = 5
minNum = 1
maxNum = 80
cards = 40

for h in range(cards):
    card = []
    randRange = range(minNum, maxNum)
    card = random.sample(randRange, gridSize * gridSize)
    for i in range(gridSize):
        string = ""
        for j in range(gridSize):
            string +=  str(card[i + j * gridSize]) + " "
        print string  

    print "\n"
	
