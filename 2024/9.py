from collections import deque
with open('inputs/9.in') as f:
    diskmap = f.readline().strip()

blocks = deque()

for _, x in enumerate(diskmap):
    if _ % 2 == 0:
        for i in range(int(x)):
            blocks.append(str(_//2))
    else:
        for i in range(int(x)):
            blocks.append('.')

len_num = len(blocks) - blocks.count('.')
numbers = []
i = 0
j = 0

while len(numbers) < len_num:
    if blocks[i] == '.':
        while blocks[-1-j] == '.':
            j+=1
        numbers.append(blocks[-1-j])
        j+=1
    else:
        numbers.append(blocks[i])
    i+=1

p1 = 0
for _, i in enumerate(numbers):
    p1 += _ * int(i)



blocks = deque()
num_count = 0

for _, x in enumerate(diskmap):
    if _ % 2 == 0:
        blocks.append(str(_//2)*int(x))
        num_count += 1
    else:
        if int(x) > 0:
            blocks.append('.'*int(x))

numbers = []
i=0
j = 0
while -1-j > -len(blocks):
    elem = blocks[-1-j]
    while elem == '.':
        j+=1
        elem = blocks[-1-j]
    for _, b in enumerate(blocks):
        if _ > len(blocks)-1-j:
            break
        if '.' in b and len(b) >= len(elem):
            blocks[-1-j] = len(elem) * '.'
            blocks.remove(b)
            blocks.insert(_, elem)
            if len(b) > len(elem):
                blocks.insert(_+1, '.'*(len(b) - len(elem)))
            break
    j+=1

p2 = 0
for _, x in enumerate(''.join(blocks)):
    if x == '.':
        x = 0
    p2 += _ * int(x)

print(''.join(blocks))
print(p2)