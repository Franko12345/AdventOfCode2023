import math

with open("./day6.txt", "r") as arq:            
    textInput = arq.read().split("\n\n")

steps = textInput[0]
maps = list(map(lambda x: (x[:3], x[7:10], x[12:15]),textInput[1].split('\n')))
maps = {m[0]: [m[1], m[2]] for m in maps}

agents = list(filter(lambda x: x[-1] == "A", maps.keys()))

cont = 0
continueI = True
while continueI:
	continueI = False
	for step in steps:
		cont+=1
		for agent in range(len(agents)):

			if not type(agents[agent]) == int:
				agents[agent] = maps[agents[agent]][step=="R"]
				continueI = True			
 
				if agents[agent][-1] == "Z":
					agents[agent] = cont
				
print(agents)

print(math.lcm(*agents))