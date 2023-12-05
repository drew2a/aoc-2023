with open('input.txt') as f:
    content = f.read()

# content = '''seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4'''

seeds, *categories = content.split('\n\n')
_, seeds = seeds.split(':')
seeds = [int(s) for s in seeds.split(' ') if s]
seed_ranges = set()
for i in range(0, len(seeds), 2):
    seed_ranges.add((seeds[i], seeds[i + 1]))


def _in(p, _start, _size):
    return _start <= p < _start + _size


def _split(p_start, p_size, _start, _size):
    points = sorted({p_start, p_start + p_size - 1, _start, _start + _size - 1})
    points = [p for p in points if _in(p, _start, _size)]
    if len(points) <= 2:
        yield _start, _size
    elif len(points) == 3:
        yield points[0], points[1] - points[0]
        yield points[1], 1
        yield points[1] + 1, points[-1] - points[1]
    else:
        yield points[0], points[1] - points[0]
        yield points[1], points[2] - points[1]
        yield points[2], points[3] - points[2]


def find_split(_start, _size, cr):
    for _d_start, _s_start, _c_size in cr:
        s = set(_split(_s_start, _c_size, _start, _size))
        if len(s) > 1:
            return s
    return None


def mega_split(_start, _size, cr):
    tmp_split = {(_start, _size)}
    result = set()
    while tmp_split:
        tst, tsz = tmp_split.pop()
        if new_split := find_split(tst, tsz, cr):
            tmp_split.update(new_split)
        else:
            result.add((tst, tsz))
    return result


for category in categories[::]:
    category_name, category_map = category.split(':')
    category_map = [m for m in category_map.split('\n') if m]
    category_ranges = [[int(s) for s in m.split(' ')] for m in category_map]
    split_seed_ranges = set()
    # split
    for start, size in seed_ranges:
        split_seed_ranges.update(mega_split(start, size, category_ranges))

    # map
    seed_ranges = set()
    for start, size, in split_seed_ranges:
        for d_start, s_start, c_size in category_ranges:
            if _in(start, s_start, c_size):  # seed in range
                seed_ranges.add((start - s_start + d_start, size))
                break
        else:
            seed_ranges.add((start, size))

print(min(start for start, size in seed_ranges))  # 136096660
