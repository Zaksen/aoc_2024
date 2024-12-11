antennas = []
nodes = []
with open('inputs/8.in') as f:
    for x, y in enumerate(f.readlines()):
        for i, j in enumerate(y):
            if j == '#':
                nodes.append([x, i])
            if j == 'a':
                antennas.append([x, i])

def find_nodes(a, b):
    nodes = []
    x = [2*a[0] - b[0], 2*a[1] - b[1]]
    y = [2*b[0] - a[0], 2*b[1] - a[1]]
    if min(x[0], x[1]) >= 0 and max(x[0],x[1]) < 10:
        nodes.append(x)
    if min(y[0], y[1]) >= 0 and max(y[0],y[1]) < 10:
        nodes.append(y)
    return nodes


anti_nodes = []

for i in range(len(antennas)):
    a = antennas[i]
    for j in range(i, len(antennas)):
        if i != j:
            b = antennas[j]
            for x in find_nodes(a, b):
                if x not in anti_nodes:
                    anti_nodes.append(x)

print(anti_nodes)
