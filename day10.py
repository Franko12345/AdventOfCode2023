with open("day10.txt", "r") as arq:
    mapTraversal = list(map(lambda x: list(x), arq.readlines()))
    
options = [(1,0, "|LJ"), (0,1,"-7J"), (-1, 0, "|F7"), (0, -1, "-FL")]

connectors_out = {
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "S" : options
}

lookup_options = {
    (0,1): (0,1,"-7J"),
    (1,0): (1,0, "|LJ"),
    (-1, 0): (-1, 0, "|F7"),
    (0, -1): (0, -1, "-FL")
}

for conn in connectors_out:
    if conn == "S": break
    for x in range(2):
        connectors_out[conn][x] = lookup_options[connectors_out[conn][x]]
        

pos = (-1,-1)
for line in range(len(mapTraversal)):
    for i in range(len(mapTraversal[0])):
        if mapTraversal[line][i] == "S":
            pos = (line, i)
            break
    if pos != (-1, -1):
        break

def nextStep(pos, mapTraversal, options, lastMove=None):
    options = list(filter(lambda x: x[0:2] != (-lastMove[0], -lastMove[1]), options))
    
    # print(options)
    for option in options:
        newPos = (pos[0]+option[0], pos[1]+option[1])
        if newPos[0] < 0 or newPos[0] > len(mapTraversal)-1 or newPos[1] < 0 or newPos[1] > len(mapTraversal[0])-1:
            continue
        
        # print(f"newPos: {newPos}, Current Symbol: {mapTraversal[newPos[0]][newPos[1]]}, Allowed Symbols: {option[2]}")
        
        if mapTraversal[newPos[0]][newPos[1]] == "S":
            return (newPos, "OVER")
        if mapTraversal[newPos[0]][newPos[1]] in option[2]:
            return (newPos, option)

out = (0,0)
cont = 0
while out != "OVER":
    pos, out = nextStep(pos, mapTraversal, connectors_out[mapTraversal[pos[0]][pos[1]]], out)
    
    print(f"Pos: {pos}, Current Symbol: {mapTraversal[pos[0]][pos[1]]}, laststep: {out}")

    cont += 1
print(cont/2)
    