import math

def FindPath(sX, sY, tX, tY, pMap, width, height):
	openSet = [(sX, sY)]
	closedSet = []
	cameFrom = {}
	g = {}
	f = {}
	for i in range(width):
		for j in range(height):
			g[(i, j)] = float('inf')
			f[(i, j)] = float('inf')
	g[(sX, sY)] = 0
	f[(sX, sY)] = math.sqrt((sX - tX)**2 + (sY - tY)**2)

	while(len(openSet) > 0):
			minF = float('inf')
			current = None
			for n in openSet:
				if(f[n] < minF):
					minF = f[n]
					current = n
			if(current == (tX, tY)):
				totalPath = [current]
				while current in cameFrom:
					current = cameFrom[current]
					totalPath += [current]
				totalPath.reverse()
				return totalPath

			openSet.remove(current)
			closedSet += [current]
			cX, cY = current
			neighbors = []
			if(cY > 0):
				if(pMap[cY - 1][cX] == 1):
					neighbors += [(cX, cY - 1)]
			if(cX < width - 1):
				if(pMap[cY][cX + 1] == 1):
					neighbors += [(cX + 1, cY)]
			if(cY < height - 1):
				if(pMap[cY + 1][cX] == 1):
					neighbors += [(cX, cY + 1)]
			if(cX > 0):
				if(pMap[cY][cX - 1] == 1):
					neighbors += [(cX - 1, cY)]
			for neighbor in neighbors:
				if neighbor in closedSet:
					continue
				nX, nY = neighbor
				tentative_gScore = g[current] + math.sqrt((cX - nX)**2 + (cY - nY)**2)
				if(neighbor not in openSet):
					openSet += [neighbor]
				elif(tentative_gScore >= g[neighbor]):
					continue

				cameFrom[neighbor] = current
				g[neighbor] = tentative_gScore
				f[neighbor] = g[neighbor] + math.sqrt((nX - tX)**2 + (nY - tY)**2)

	return -1

#Test
m = [[0, 0, 1],
	[1, 1, 1],
	[1, 0, 1]]
print FindPath(2, 0, 0, 2, m, 3, 3)