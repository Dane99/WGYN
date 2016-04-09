from __future__ import division
from itertools import product
from decimal import Decimal
from datetime import datetime
import random
import time
import sys


numbers = ['5' , '2' , '7', '9']
cleanNumbers = numbers[:]
operators = ['+', '-', '/', '*']
possibleChars = operators + numbers
lengthOfPossibleChars = len(possibleChars)
counter = 0
start_time = time.time()

numbersLeftAndSolutions = range(1,101)
length = 11

solCounter = 0

numOfCycles = 100000000 # Changes the amount of time that it takes to compute results. Smaller value = less coverage

random.seed(datetime.now())
def randomDNA(length):
	DNA = []
	for x in range(length):
		if(x == 0):
			DNA.append(random.choice(numbers + ['(']))
		elif(DNA[x-1] in cleanNumbers):
			DNA.append(random.choice(numbers + operators + [')']))
		elif(DNA[x-1] in operators):
			DNA.append(random.choice(numbers + ['(']))
		elif(DNA[x-1] == '('):
			DNA.append(random.choice(numbers))
		elif(DNA[x-1] == ')'):
			DNA.append(random.choice(operators))
		else:
			print("ERROR")
	return DNA



def validCheck(DNA):
	expoCounter = 0 # Used to minimize computational time... Before implementation delta time of completion: 35 hours After: 
	copyOfCleanNumbers = cleanNumbers[:]
	for x in range(len(DNA)):
		if (DNA[x] in cleanNumbers): #clean because we want this to loop through as long as there is a number
			#print(copyOfCleanNumbers)
			if not copyOfCleanNumbers: # List is empty. We do this to make sure that we don't have more than four of the same number in an equation
				return 0
			try:					# We have this here because the function might fail due to numbers not being in list... Not needed anymore, but just there for safety
				index = copyOfCleanNumbers.index(DNA[x])
				copyOfCleanNumbers.pop(index)
			except:
				return 0

		#elif((DNA[x] == '*') and (DNA[x+1] == '*')):
			#expoCounter += 1

	if not copyOfCleanNumbers: #List is empty
		# if expoCounter > 0:
		# 	return 0
		# else:
		# 	return 1
		return 1
	else:
		return 0

while(counter < numOfCycles):
	i = randomDNA(length) # i is the DNA/equation
	#print(counter)
	#print(i)
	#print(''.join(map(str, i)))
	#print "**010"
	y = []
	for x in range(len(i)-1):
		if (i[x] == "/" and i[x+1] == "/"):
			pass
		else:
			y.append(i[x])

	try:
		if(validCheck(y) == 1):
			evalNum = Decimal(eval(''.join(map(str, y))))
		else:
			evalNum = None
		#print "**020"
		#print(i)
		#print "**025"
	except:
		#print "**030"
		evalNum = None

	
	if((evalNum in numbersLeftAndSolutions)):
		#print(i)
		if evalNum % 1 == 0:
			#print(i)
			#print(evalNum)
			numbersLeftAndSolutions[int(evalNum) - 1] = y
	counter += 1

	if(counter % 10000 == 0):
		end_time = time.time()
		print(counter, " out of ", lengthOfPossibleChars**length)
		print("Percentage: ", (counter/(numOfCycles)*100))
		tdelta = end_time - start_time
		print(tdelta)
		start_time = time.time()
		#time.sleep(1)


for x in xrange(1, 101):
	print("The solution to ", x, " is: ", numbersLeftAndSolutions[x-1])
	if x != numbersLeftAndSolutions[x-1]:
		solCounter += 1

print("We have ", solCounter, " Solutions")



