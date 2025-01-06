rules = []
p1 = 0

with open('inputs/5.in') as f:
    while True:
        r = f.readline()
        if r == "\n":
            break
        rules.append(r.strip().split('|'))
    for s in f.readlines():
        pages = s.strip().split(',')
        i = 0
        correct = True
        while i < len(pages):
            before = []
            after = []
            for rule in rules:
                if pages[i] in rule:
                    if pages[i] == rule[0]:
                        after.append(rule[1])
                    else:
                        before.append(rule[0])
            for j in range(i):
                if pages[j] in after:
                    correct = False
                    break
            for j in range(i+1, len(pages)):
                if pages[j] in before:
                    correct = False
                    break
            i += 1
        if correct == True:
            p1 += int(pages[len(pages)//2])
            

print(p1)        
