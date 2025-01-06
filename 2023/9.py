L = [0, 3, 6, 9, 12, 15]

def sequence(L):
	return [L[i] - L[i-1] for i in range(1, len(L))]

def get_next_element(L, first=True):
	p = -1 if first else 0
	m = 1 if first else -1
	elements = [L[p]]
	while any(L):
		L = sequence(L)
		elements.insert(0, L[p])		
	for n in range(1, len(elements)):
		elements[n] += m * elements[n-1]
	return elements[-1]

p1 = 0
p2 = 0

with open('input/9.txt') as f:
	content = f.readlines()

for line in content:
	history = [int(i) for i in line.split()]
	p1 += get_next_element(history)
	p2 += get_next_element(history, first=False)

print(p1)
print(p2)