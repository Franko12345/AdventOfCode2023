def define_priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38
    
def get_match(comp1, comp2):
    for i in comp1:
        for j in comp2:
            if i == j:
                return i

with open("./day3.txt", "r") as arq:            
    textInput = arq.readlines()

totalSum = 0
for line in textInput:
    comp1 = line[:int(len(line)/2)]
    comp2 = line[int(len(line)/2):]
    item = get_match(comp1, comp2)
    totalSum += define_priority(item)
    
print(totalSum)