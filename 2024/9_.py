from collections import deque


D = open('inputs/9.in').read().strip()

A = deque([])
SPACE = deque([])
file_id = 0
FINAL = []
pos = 0

for i,c in enumerate(D):
    if i%2==0:
        A.append((pos, int(c), file_id))
        for i in range(int(c)):
            FINAL.append(file_id)
            pos += 1
        file_id += 1
    else:
        SPACE.append((pos, int(c)))
        for i in range(int(c)):
            FINAL.append(None)
            pos += 1
print(A)
print(SPACE)
print(FINAL)