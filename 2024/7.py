p1 = 0
with open('inputs/7.in') as f:
    for equ in f.readlines():
        test_value, _ = equ.strip().split(': ')
        numbers = [int(x) for x in _.split()]
        length = len(numbers) - 1
        combinations = [format(i, '0{}b'.format(length)) for i in range(pow(2, length))]
        for c in combinations:
            operation = []
            result = numbers[0]
            for i in range(len(c)):
                if c[i] == '0':
                    result += numbers[i+1]
                else:
                    result *= numbers[i+1]
            if result == int(test_value):
                p1 += result
                break

print(p1)