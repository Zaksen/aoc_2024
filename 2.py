def same_direction(r):
    direction = r[0] - r[1]
    if direction > 0:
        return r == sorted(r, reverse=True)
    else:
        return r == sorted(r)

def adjacent(r):
    i = 0
    while i < len(r) - 1:
        d = abs(r[i] - r[i+1])
        if d < 1 or d > 3:
            return False
        i += 1
    return True

def is_safe(r):
    if adjacent(r) and same_direction(r):
        return True
    return False
p1 = 0
p2 = 0



with open('inputs/2.in') as f:
    for l in f.readlines():
        r = [int(x) for x in l.strip().split()]
        if is_safe(r):
            p1 += 1


with open('inputs/2.in') as f:
    for l in f.readlines():
        r = [int(x) for x in l.strip().split()]
        i = 0
        if is_safe(r):
            p2 += 1
        else:
            while i < len(r):
                r2 = r.copy()
                r2.pop(i)
                if is_safe(r2):
                    p2 += 1
                    break
                i += 1

print(p1)  
print(p2)