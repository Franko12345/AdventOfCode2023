with open("day11.txt", 'r') as arq:
    lines = arq.read().split("\n")
    
galaxies = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == "#":
            galaxies.append((x,y))

def expand(array, galaxies, xy):
    newArray = [0 for _ in galaxies]
    for line in range(len(array)): 
        if "#" in array[line]:
            continue
        
        galaxies_affected = list(map(lambda galaxy: galaxy[xy] > line, galaxies))
        newArray = map(lambda x,y: x+y, newArray, galaxies_affected)
        
    galaxies = list(map(lambda galaxy, affected: (galaxy[0]+((xy==0)*1000000*affected), galaxy[1]+((xy==1)*1000000*affected)), galaxies, newArray))
    return galaxies

def subVector(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

 
galaxies = expand(lines, galaxies, 0)

columns = [[line[i] for line in lines] for i in range(len(lines[0]))]

galaxies = expand(columns, galaxies, 1)

total = 0
for x in range(len(galaxies)):
    for y in range(len(galaxies)-x):
        distanceVector = subVector(galaxies[x], galaxies[x+y])
        total += abs(distanceVector[0]) + abs(distanceVector[1])

print(total)