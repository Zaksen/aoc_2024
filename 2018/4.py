from datetime import datetime
from collections import OrderedDict

D = {}
with open('inputs/4.in') as f:
    for x in f.readlines():
        date, content = x.strip().split(']')
        date = date[1:]
        if '#' in content:
            id_end = content.find(' ', 7)
            value = int(content[8:id_end])
        elif 'asleep' in content:
            value = 'asleep'
        else:
            value = 'up'
        D[date] = value

D = dict(sorted(D.items()))


# D = OrderedDict(D.items(), key= lambda x:datetime.strptime(x[0], '%Y-%m-%d %H:%M'))
guards = {k:[] for k in D.values() if isinstance(k, int)}

current = ''

for k,v in D.items():
    if isinstance(v, int):
        current = v
        continue
    if v == 'asleep':
        start = int(k[-2:])
        continue
    if v == 'up':
        end = int(k[-2:])
        for i in range(start, end):
            guards[current].append(i)

guard = max(guards.items(), key = lambda x : len(x))

minute_max = 0
length = 0


print(guards)
for x in guard[1]:
    if guard[1].count(x) >= length:
        length = guard[1].count(x)
        minute_max = x

print(minute_max*guard[0])