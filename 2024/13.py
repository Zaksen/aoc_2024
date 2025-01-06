A = []
B = []
prizes = []


def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        print(r, a, b)
        return pgcd(b,r)



with open('inputs/13.in') as f:
    for line in f:
        if line.startswith('Button A'):
            c = line.strip()[12:].split(', Y+')
            A.append(c)
        elif line.startswith('Button B'):
            c = line.strip()[12:].split(', Y+')
            B.append(c)
        elif line.startswith('P'):
            c = line.strip()[9:].split(', Y=')
            prizes.append(c)
        else:
            continue





print(A)
print(B)
print(prizes)
pgcd(544, 315)
