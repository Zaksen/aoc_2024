
p1 = 0
p2 = 0
SEEN = [0]

with open('inputs/1.in') as f:
    instructions = [l.strip() for l in f.readlines()]
        
for i in instructions:
        if i[0] == '+':
            p1 += int(i[1:])
        else:
            p1 -= int(i[1:])

print(p1)

j = 0
while True:
    indice = instructions[j % len(instructions)]
    if indice[0] == '+':
        p2 += int(indice[1:])
    else:
        p2 -= int(indice[1:])
    if p2 not in SEEN:
        SEEN.append(p2)
    else:
        break
    j += 1

print(p2)
        
    

