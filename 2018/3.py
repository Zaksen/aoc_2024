with open('inputs/3.in') as f:
    instructions = [x.strip() for x in f.readlines()]

grid = [['.' for i in range(8)] for i in range(8)]

FINAL = set()
SEEN = set()
OCCUPIED = set()

for x in instructions:
    a,b = x.split(':')
    width, height = [int(b) for b in b.strip().split('x')]
    _, top = a.split(',')
    top = int(top)
    id, left = _.split('@')
    left = int(left)
    max_height = top+height-1
    max_width = left+width-1
    FINAL.add((id, left, max_width, top, max_height))

for sq in FINAL:
    for i in range(sq[3], sq[4]+1):
        for j in range(sq[1], sq[2]+1):
            if (i,j) in SEEN:
                OCCUPIED.add((i,j))
            SEEN.add((i, j))

print(len(OCCUPIED))

UNIQUE = set()
for x in SEEN:
    if x not in OCCUPIED:
        UNIQUE.add(x)

for sq in FINAL:
    points = set([(i,j) for i in range(sq[3], sq[4]+1) for j in range(sq[1], sq[2]+1)])
    if points.issubset(UNIQUE):
        print(sq[0])
        break
    