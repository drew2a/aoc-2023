from dataclasses import dataclass

with open('input.txt') as f:
    matrix = f.readlines()

# matrix = '''
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...'''.split('\n')

result = 0
matrix = [[ch for ch in line] for line in matrix if line]
mp = [[ch for ch in line] for line in matrix if line]


def find_s_cordinates(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'S':
                return i, j


types = {
    'S': [],
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    '7': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    'L': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
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


start = Point(coordinates=find_s_cordinates(matrix), increment=[(0, -1), (1, 0)])
print(start)
print_matrix(mp)
print('-' * 40)

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

        mp[point.coordinates[0]][point.coordinates[1]] = step
        closed_points.add(point)
    if not new_open:
        break
    open_points = new_open

print_matrix(mp)
print(step)  # 6754
