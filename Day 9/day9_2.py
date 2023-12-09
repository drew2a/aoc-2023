with open('input.txt') as f:
    content = f.readlines()

# content = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''.split('\n')

result = 0
histories = [[int(i) for i in h.split(' ')] for h in content if h]
for history in histories:
    sequence = history[:]
    first = []
    tab = ''
    print(f'{tab}{sequence}')
    while any(s for s in sequence):
        tab += '  '
        next_sequence = []
        for j in range(len(sequence) - 1):
            next_sequence.append(sequence[j + 1] - sequence[j])
        first.append(next_sequence[0])
        sequence = next_sequence
        print(f'{tab}{sequence}')
    interpolated = 0
    for ff in reversed(first):
        interpolated = ff-interpolated

    interpolated = history[0] - interpolated
    result += interpolated
    print(interpolated)

print(f'Result: {result}')  # 1154
