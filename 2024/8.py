from collections import defaultdict

with open('inputs/8.in') as f:
    grid = [x.strip() for x in f.readlines()]

R, C = len(grid), len(grid[0])

def is_in_grid(i, j, r, c):
    return True if 0 <= i < r and 0 <= j < c else False

def find_nodes(a, b, r, c):
    nodes = []
    x = [2*a[0] - b[0], 2*a[1] - b[1]]
    y = [2*b[0] - a[0], 2*b[1] - a[1]]
    if is_in_grid(x[0], x[1], r, c):
        nodes.append(x)
    if is_in_grid(y[0], y[1], r, c):
        nodes.append(y)
    return nodes

def pairs(l):
    return [(a, b) for idx, a in enumerate(l) for b in l[idx + 1:]]


def linear(a, b, r, c):
    points = []
    for i in range(r):
        for j in range(c):
            if j == (b[1] - a[1])/(b[0] - a[0])*(i-a[0]) + a[1]:
                points.append([i, j])
    return points



d = defaultdict(list)

for i, x in enumerate(grid):
    for j, y in enumerate(x):
        if y != '.':
            d[y].append([i, j])
    
p1 = []
p2 = []
for x, y in d.items():
    for v in pairs(y):
        for n in find_nodes(v[0], v[1], R, C):
            if n not in p1:
                p1.append(n)

for x, y in d.items():
    for v in pairs(y):
        for n in linear(v[0], v[1], R, C):
            if n not in p2:
                p2.append(n)

print(len(p1))
print(len(p2))

