from math import lcm

with open('input/8.txt') as f:
	instructions = [0 if item == 'L' else 1 for item in list(f.readline().strip())]
	f.readline()
	content = f.readlines()

nodes = {node[:3] : (node[7:10] , node[12:15]) for node in content}
starting_nodes = [n for n in nodes.keys() if n[-1] == 'A']

p1 = 0
p2 = 0
def goto(origin, instruction):
	return nodes[origin][instruction]

"""p = 'AAA'
while p != 'ZZZ':
	for i in instructions:
		p = goto(p, i)
		p1 += 1
"""
cycles = []

I = 0
for n in starting_nodes:
	count = 0
	while n[-1] != 'Z':
		for i in range(len(instructions)):
			n = goto(n, instructions[(i + I*len(instructions)) % len(instructions)])
			count += 1
			I+=1
			if n[-1] == 'Z':
				cycles.append(count)

print(lcm(*cycles))