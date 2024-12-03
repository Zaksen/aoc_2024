import re
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"

with open('inputs/3.in') as f:
    mystring = f.read()

matches = re.findall(pattern, mystring)

p1 = 0
p2 = 0
mul = True

for m in matches:
    if m == 'do()':
        mul = True
    elif m == "don't()":
        mul = False
    else:
        x, y = m[4:-1].split(',')
        p1 += int(x) * int(y)
        p2 += int(x) * int(y) * mul

print(p1, p2)