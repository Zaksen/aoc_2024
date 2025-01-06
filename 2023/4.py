with open('input/4.txt') as f:

    cards = f.readlines()

data = {}
p1 = 0
for i, card in enumerate(cards):
    winning_numbers, numbers = card.split(':')[1].split('|')
    matches = [n for n in numbers.split() if n in winning_numbers.split()]
    
    if len(matches) > 0:
        p1 += pow(2, len(matches) - 1)

print(p1)