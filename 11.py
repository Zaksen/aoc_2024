with open('inputs/11.in') as f:
    stones = [int(x) for x in f.read().strip().split()]


def transform(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        _ = str(stone)
        return [int(_[:len(_)//2]), int(str(_)[len(_)//2:]) ]
    else:
        return [stone*2024]

def blink(stones, r=1):
    for i in range(r):
        stones = [y for xs in [transform(x) for x in stones] for y in xs]
    return len(stones)

print(blink(stones,75))