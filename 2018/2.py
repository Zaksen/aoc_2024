from collections import defaultdict

with open('inputs/2.in') as f:
    boxes = [x.strip() for x in f.readlines()]

x = 0
y = 0

for b in boxes:
    d = {v:b.count(v) for v in b}
    if 2 in d.values():
        x += 1
    if 3 in d.values():
        y += 1

p1 = x * y 
print(p1)
for id in boxes:
    for id2 in boxes:
        if id != id2:
            for i in range(len(id)):
                first = list(id)
                del first[i]
                second = list(id2)
                del second[i]
                if first == second:
                    print(''.join(first))