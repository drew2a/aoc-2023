import itertools

with open('input.txt') as f:
    matrix = f.readlines()

# matrix = '''
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# '''.split('\n')

result = 0
matrix = [[ch for ch in line if ch != '\n'] for line in matrix if line]


def print_matrix(m):
    print('-' * 40)
    print('\n'.join(''.join(str(ch) for ch in line) for line in m))


EXPAND_VALUE = 1


def expand_the_universe(m, gals):
    not_occupied_i = []
    not_occupied_j = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != '.':
                break
        else:
            not_occupied_i.append(i)
    for j in range(len(m[0])):
        for i in range(len(m)):
            if m[i][j] != '.':
                break
        else:
            not_occupied_j.append(j)

    result = []
    for g in gals:
        affected = 0
        for i in not_occupied_i:
            if i <= g[0]:
                affected += 1
        result.append((g[0] + (affected * EXPAND_VALUE), g[1]))

    final_result = []
    for g in result:
        affected = 0
        for j in not_occupied_j:
            if j < g[1]:
                affected += 1
        final_result.append((g[0], g[1] + (affected * EXPAND_VALUE)))

    print(not_occupied_i)
    print(not_occupied_j)
    return final_result


def find_galaxies(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '#':
                yield i, j


print('Before expansion:')
# print_matrix(matrix)
print('\nAfter expansion:')
galaxies = list(find_galaxies(matrix))
galaxies = expand_the_universe(matrix, galaxies)
print(f'Galaxies: {galaxies}')

distance_cache = {}


def find_shortest_path(m, g, g1):
    dif_i = abs(g[0] - g1[0])
    dif_j = abs(g[1] - g1[1])
    return dif_i + dif_j


score = 0
step = 0
combinations = list(itertools.combinations(galaxies, 2))
for gal1, gal2 in combinations:
    step += 1
    if not step % 1000:
        print(f'{step}/{len(combinations)}')
    score += find_shortest_path(matrix, gal1, gal2)

# print_matrix(matrix)
print(f'Score: {score}')  # 9418609
