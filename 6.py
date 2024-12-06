with open('inputs/6.in') as f:
    grid = [list(r.strip()) for r in f.readlines()]



max_x = len(grid) - 1
max_y = len(grid[0]) - 1
for i in range(max_x):
        for j in range(max_y):
            if grid[i][j] == "^":
                starting_position = (i, j)
                break

def go(grid, starting_position):
    covered = set()
    covered.add(starting_position)
    p = starting_position
    dir = (-1, 0)

    while True:
        x = p[0] + dir[0]
        y = p[1] + dir[1]
        if x < 0 or y < 0:
            break
        if x > max_x or y > max_y:
            break
        if grid[x][y] == '#':
            dir = (dir[1], -dir[0])
            continue
        p = (x, y)
        covered.add(p)

    return len(covered)
        
