size = [101, 103]

import time

def move(x, y, u, v, size):
    return [(x+u)%size[0], (y+v)%size[1]]

robots = []

with open('inputs/14.in') as f:
    for robot in f:
        p, v = robot.strip().split()
        p = [int(x) for x in p[2:].split(',')]
        v = [int(x) for x in v[2:].split(',')]
        robots.append([p, v])


def print_grid(robots, size):
    grid = [['.' for x in range(size[0])] for y in range(size[1])]
    for p in robots:
        grid[p[0][1]][p[0][0]] = '#'
    for l in grid:
        print(''.join(l))

i=0
while True:
    r_set = set()
    for r in robots:
        x, y = r[0]
        u, v = r[1]
        r[0] = move(x, y, u, v, size)
        r_set.add((r[0][0], r[0][1]))
    if len(r_set) == len(robots):
        print(i+1)
        break
    i+=1


print_grid(robots, size)
