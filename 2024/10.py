with open('inputs/10.in') as f:
    grid = [[int(x) for x in list(l.strip())] for l in f.readlines()]

max_i = len(grid)
max_j = len(grid[0])

