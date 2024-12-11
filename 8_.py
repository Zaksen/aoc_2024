antennas = []
nodes = []
with open('inputs/8.in') as f:
    grid = [x.strip() for x in f.readlines()]

antennas = {}

for x in grid:
    for y in x:
        if y != '.':



def find_nodes(a, b):
    nodes = []
    x = [2*a[0] - b[0], 2*a[1] - b[1]]
    y = [2*b[0] - a[0], 2*b[1] - a[1]]
    if min(x[0], x[1]) >= 0 and max(x[0],x[1]) < 10:
        nodes.append(x)
    if min(y[0], y[1]) >= 0 and max(y[0],y[1]) < 10:
        nodes.append(y)
    return nodes

