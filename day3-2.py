def define_priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38
    
def get_match(elfs):
    itemsHash = {}
    for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        itemsHash[i] = 0
    
    elfCount = 0
    for elf in elfs:
        for item in elf:
            itemsHash[item] = itemsHash[item] | 2**elfCount
        elfCount += 1
    
    for x in itemsHash:
        if itemsHash[x] == 0b111:
            return x
        
with open("./day3.txt", "r") as arq:            
    textInput = arq.read().split("\n")

totalSum = 0
for line in range(0, len(textInput), 3):
    elfs = textInput[line:line+3]
    item = get_match(elfs)
    print(elfs)
    print(item)
    totalSum += define_priority(item)
    
print(totalSum)