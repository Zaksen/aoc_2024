with open('inputs/4.in') as f:
    grid = [l.strip() for l in f.readlines()]

def is_in_grid(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False
     
def diagonal(i, j, n):
    x = ''
    if is_in_grid(i+n, j+n):
        for m in range(n+1):
            x += grid[i+m][j+m]
    return x

def anti_diagonal(i, j, n):
    x = ''
    if is_in_grid(i+n, j-n):
        for m in range(n+1):
            x+= grid[i+m][j-m]
    return x

def horizontal(i, j):
    x = ''
    if is_in_grid(i, j+3):
        for n in range(4):
            x += grid[i][j+n]
    return x

def vertical(i, j):
    x = ''
    if is_in_grid(i+3, j):
        for n in range(4):
            x += grid[i+n][j]
    return x

d_count = 0
a_count = 0
h_count = 0
v_count = 0

for i in range(len(grid)):
   for j in range(len(grid[0])):
        if diagonal(i, j, 3) in ('XMAS', 'SAMX'):
            d_count += 1
        if anti_diagonal(i, j, 3) in ('XMAS', 'SAMX'):
            a_count += 1
        if vertical(i, j) in ('XMAS', 'SAMX'):
            v_count += 1
        if horizontal(i, j) in ('XMAS', 'SAMX'):
            h_count += 1

p1 = d_count + a_count + h_count + v_count
print(p1)

p2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if diagonal(i, j, 2) in ('SAM', 'MAS') and anti_diagonal(i, j+2, 2) in ('SAM', 'MAS'):
            p2 += 1

print(p2)


