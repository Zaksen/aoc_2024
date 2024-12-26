with open('inputs/15.in') as f:
    map, moves = f.read().strip().split('\n\n')
    map = map.split('\n')

d = {
    '<' : [0, -1],
    '>' : [0, 1],
    '^' : [-1, 0],
    'v' : [1, 0]
}

for i, x in enumerate(map):
    print(i)
    for j, y in enumerate(x):
        print(j)
        if y == '@':
            starting_position = [i, j]
            break
    else:
        continue
    break

i = 0
p = starting_position

while i < len(moves):
    print(map)
    u = d[moves[i]]
    x = p[0] + u[0]
    y = p[1] + u[1]
    if x == 0 or y == 0:
        print('reached edge, continuing')
        i += 1
        continue
    if map[x][y] == 'O':
        if map[x+u[0]][y+u[1]] == '#':
            i+=1
            continue
        else:
            map[x][y] = '.'
            map[x+u[0], y+u[1]] = 'O'
            p = [x, y]
            i+=1
    else:
        p = [x,y]
        i+=1
