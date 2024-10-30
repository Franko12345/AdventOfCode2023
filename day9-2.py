with open("day9.txt", "r") as arq:
    textinput = arq.readlines()
    textinput = list(map(lambda x: list(map(int, x.split(" "))), textinput))
    

def find_next_digit(sequence):
    sequence = sequence[::-1]
    cont = 0
    while True:
        tmp = []
        for x in range(len(sequence)-(1+cont)):
            tmp.append(sequence[x+1] - sequence[x])
        sequence = tmp + sequence[-cont-1:]
        
        cont += 1
        
        if len(set(tmp)) == 1:
            break
        
    return sum(sequence[-cont-1:])
        
    
    
print(sum(map(find_next_digit, textinput)))