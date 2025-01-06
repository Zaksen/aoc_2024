with open('input/2.txt') as f:
    content = [l for l in f.readlines()]


p1 = 0
p2 = 0
for line in content:
    ok = True
    id_, line = line.split(':')
    max_ = {'red' : 0, 'green' : 0, 'blue' : 0}
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            if int(n) > int(max_.get(color, 0)):
                max_[color] = max(int(n), max_[color])
            if int(n) > {'red' : 12, 'green' : 13, 'blue': 14}.get(color, 0):
                ok = False
    ans = 1
    for i in max_:
        ans = ans * int(max_[i])
    p2 += ans

    if ok:
        p1 += int(id_.split()[-1])

print(p1)
print(p2)

        
    