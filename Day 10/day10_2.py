from dataclasses import dataclass

with open('input.txt') as f:
    matrix = f.readlines()

# matrix = '''
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# '''.split('\n')

result = 0
matrix = [['.'] + [ch for ch in line] + ['.'] for line in matrix if line]
matrix.insert(0, ['.'] * len(matrix[0]))
matrix.append(['.'] * len(matrix[0]))
mp = [['.' for ch in line] for line in matrix if line]


def find_s_cordinates(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'S':
                return i, j


types = {
    'S': {(1, 0)},
    '-': {(0, -1), (0, 1)},
    '|': {(-1, 0), (1, 0)},
    '7': {(0, -1), (1, 0)},
    'J': {(0, -1), (-1, 0)},
    'L': {(0, 1), (-1, 0)},
    'F': {(0, 1), (1, 0)},
}


@dataclass()
class Point:
    coordinates: tuple
    increment: list

    def __hash__(self):
        return hash(self.coordinates)

    def __eq__(self, other):
        return self.coordinates.__eq__(other.coordinates)


def print_matrix(m):
    print('\n'.join(''.join(str(ch) for ch in line) for line in m))


def create_point(current: Point, inc: tuple):
    i = current.coordinates[0] + inc[0]
    j = current.coordinates[1] + inc[1]
    return Point(
        coordinates=(i, j),
        increment=types[matrix[i][j]]
    )


start = Point(coordinates=find_s_cordinates(matrix), increment=types['S'])

step = -1
open_points = {start}
closed_points = {start}

while True:
    step += 1
    new_open = set()
    for point in open_points:
        for increment in point.increment:
            p = create_point(point, increment)
            if p in closed_points:
                continue
            new_open.add(p)
        i = point.coordinates[0]
        j = point.coordinates[1]
        mp[i][j] = matrix[i][j]
        closed_points.add(point)
    if not new_open:
        break
    open_points = new_open

open_points = {start}
closed_points = {start}

tiles = 0
for i in range(len(mp)):
    counted = False
    for j in range(len(mp[0])):
        if mp[i][j] in {'|', '7', 'F', 'S'}:
            counted = not counted
        if types.get(mp[i][j]):
            continue
        if counted:
            tiles += 1
            mp[i][j] = '+'

print_matrix(mp)
print(tiles)  # 567
