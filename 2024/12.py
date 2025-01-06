with open('inputs/12.in') as f:
    grid = [l.strip() for l in f.readlines()]

letters = set()
for x in grid:
    for y in x:
        letters.add(y)

def is_adjacent(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    if (p1[0] == p2[0] and y == 1) or (p1[1] == p2[1] and x == 1):
        return True
    return False

for plant in letters:
    coordinates = []
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == plant:
                coordinates.append([i, j])
    groups = []
    for c in coordinates:
        
        group = []
        group.append(c)

        i = 0

        print(coordinates)
        while i < len(group):
            for j in range(len(coordinates)):
                if is_adjacent(coordinates[j], group[i]):
                    group.append(coordinates[j])
                    print(group)
            i+=1
            

 