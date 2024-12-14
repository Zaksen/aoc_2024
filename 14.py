p1 = []
size = [101, 103]
def move(x, y, u, v):
    return [(x+u)%size[0], (y+v)%size[1]]

q1 = 0
q2 = 0
q3 = 0
q4 = 0
origin = [size[0]//2, size[1]//2]

with open('inputs/14.in') as f:
    for robot in f:
        p, v = robot.strip().split()
        p = [int(x) for x in p[2:].split(',')]
        v = [int(x) for x in v[2:].split(',')]
        for i in range(100):
            p = move(p[0], p[1], v[0], v[1])
        p = [p[0] - origin[0], p[1] - origin[1]]
        if p[0] > 0 and p[1] > 0:
            q1 += 1
        elif p[0] < 0 and p[1] < 0:
            q2 += 1
        elif p[0] > 0 and p[1] < 0:
            q3 += 1
        elif p[0] < 0 and p[1] > 0:
            q4 += 1
        else:
            continue

p1 = q1 * q2 * q3 * q4
print(p1)






# size = [11, 7]

# p = [2, 4]
# v = [2, -3]



# for i in range(5):
#     p = move(p[0], p[1], v[0], v[1])
#     print(p)