import math

with open('input.txt') as f:
    content = f.readlines()

# content = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split('\n')

s = 0
for line in content:
    name, rounds = line.split(':')
    _, name_id = name.split(' ')
    max_kubes = {'red': 0, 'blue': 0, 'green': 0}
    for r in rounds.split(';'):
        kubes = dict(reversed(k.strip().split(' ')) for k in r.split(','))
        for k in kubes:
            max_kubes[k] = max(max_kubes[k], int(kubes[k]))
    s += math.prod(k for k in max_kubes.values() if k)

print(s)  # 67335
