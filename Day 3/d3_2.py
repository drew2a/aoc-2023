import math
from collections import defaultdict

from colorama import Fore, Style

with open('input.txt') as f:
    content = f.readlines()


# content = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''.split('\n')


def get_adjacent(m, i, j):
    for ii in range(-1, 2, 1):
        row = m[i + ii]
        for ij in range(-1, 2, 1):
            c = row[j + ij]
            if c == '*':
                return i + ii, j + ij
    return None


first_and_last = ['.' * (len(content[0]) + 4)]
content = first_and_last + [f'..{l}..' for l in content] + first_and_last
adjacents = defaultdict(list)

for i in range(1, len(content) - 1):
    line = content[i]
    number = ''
    adjacent = None
    for j in range(1, len(line) - 1):
        ch = line[j]
        if ch.isnumeric():
            number += ch
            adjacent = adjacent or get_adjacent(content, i, j)
        else:
            if number:
                if adjacent:
                    adjacents[adjacent].append(number)
                    print(Fore.GREEN + number, end='')
                else:
                    print(Fore.RED + number, end='')

            number = ''
            adjacent = False
            print(Fore.WHITE + ch, end='')
    print()

print(Style.RESET_ALL)
gears = (ad for ad in adjacents.values() if len(ad) != 1)
gears_prod = (math.prod(int(i) for i in g) for g in gears)
print(sum(gears_prod)) #87263515
