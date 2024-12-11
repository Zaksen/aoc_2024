with open('inputs/9.in') as f:
    diskmap = f.readline().strip()

blocks = []

for _, x in enumerate(diskmap):
    if _ % 2 == 0:
        for i in range(int(x)):
            blocks.append(str(_//2))
    else:
        for i in range(int(x)):
            blocks.append('.')

while blocks.count('.') > 0:
    if blocks[-1] == '.':
        blocks.pop()
        continue
    else:
        i = 0
        while i < len(blocks):
            if blocks[i] == '.':
                blocks[i] = blocks[-1]
                blocks.pop()
                break
            i += 1

p1 = 0
for i, j in enumerate(blocks):
    p1 += i * int(j)

print(p1)