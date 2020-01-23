import random

def createArr(num, dimensions):
	# creates a 2d arr
	array = []
	for i in range(dimensions):
		array.append([])
		for j in range(dimensions):
			array[i].append(num)
	return array

def createMap():
	dimensions = 20
	maxTunnels = 5
	maxLength = 5
	newMap = createArr(1,dimensions) #fills 2d arr with 1's. 1's will be walls 0's will be path
	currentColumn = random.randint(1, dimensions)
	currentRow = random.randint(1, dimensions)
	directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] #to go up, subtract 1 from its row. to go down, add 1 to its row. to go right, add 1 to its column. to go left, subtract 1 from its column
	lastDirection = [0,0]
	randomDirection = [0,0]

	while not randomDirection[0] == abs(lastDirection[0]) and randomDirection[1] == abs(lastDirection[1]):
		# do stuff
		randomDirection = directions[random.randint(0,len(directions) -1)]

	randomLength = random.randint(1,maxLength)
	tunnelLength = 0

	while tunnelLength < randomLength:
		if currentRow == 0 and randomDirection[0] == -1 or currentColumn == 0 and randomDirection[1] == -1 or currentRow == dimensions -1 and randomDirection[0] == 1 or currentColumn == dimensions -1 and randomDirection[1] == 1 :
			break
		else:
			newMap[currentRow][currentColumn] = 0
			currentRow += randomDirection[1]
			tunnelLength += 1
			print(f'{currentRow} {currentColumn}')

	if tunnelLength:
		lastDirection = randomDirection
		maxTunnels -= 1

	return newMap






print(createMap())
