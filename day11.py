with open("day11.txt", 'r') as arq:
    lines = arq.read().split("\n")
    
def expand(array):
    newArray = []
    for line in array: 
        for _ in range(1 + (not ("#" in line))):
            newArray.append(line)
    return newArray

def subVector(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])
 
lines = expand(lines)
    
columns = [[line[i] for line in lines] for i in range(len(lines[0]))]

columns = expand(columns)

finalMatrix = [[line[i] for line in columns] for i in range(len(columns[0]))]

galaxies = []
for x in range(len(finalMatrix)):
    for y in range(len(finalMatrix[0])):
        if finalMatrix[x][y] == "#":
            galaxies.append((x,y))

total = 0
for x in range(len(galaxies)):
    for y in range(len(galaxies)-x):
        distanceVector = subVector(galaxies[x], galaxies[x+y])
        total += abs(distanceVector[0]) + abs(distanceVector[1])

print(total)