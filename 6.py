with open('inputs/6.in') as f:
    grid = [list(r.strip()) for r in f.readlines()]

covered = set()

directions = {
    '^' : (0,-1),
    '>' : (1,0),    
    'v' : (0,1),    
    '<' : (-1,0),    
}

max_x = len(grid) - 1
max_y = len(grid[0]) - 1

for i in range(max_x):
    for j in range(max_y):
        if grid[i][j] == "^":
            starting_position = (i, j)
            covered.add(starting_position)
            break

in_grid = True

while in_grid:
    dir = "^"
    p = starting_position
    print(starting_position)
    x = p[0] + directions[dir][0]
    y = p[1] + directions[dir][1]
    if grid[x, y] == '#':
        dir
