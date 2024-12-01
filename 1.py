with open('inputs/1.in') as f:
    content = f.readlines()

first = []
second = []
for l in content:
    first.append(int(l.strip().split()[0]))
    second.append(int(l.strip().split()[1]))

distances = [abs(y - x) for x, y in zip(sorted(first), sorted(second))]
p1 = sum(distances)
print(p1)

p2 = 0
for i in first:
    p2 += second.count(i) * i
print(p2)



