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

for category in categories:
    category_name, category_map = category.split(':')
    category_map = [m for m in category_map.split('\n') if m]
    new_seeds = []
    print(category_map)
    for seed in seeds:
        new_seed = None
        for m in category_map:
            destination_range_start, source_range_start, range_length = (int(s) for s in m.split(' '))
            distance = seed - source_range_start
            if 0 <= distance < range_length:
                new_seed = destination_range_start + distance
                break
        new_seeds.append(new_seed or seed)
    print(new_seeds)
    seeds = new_seeds

print(min(seeds))  # 825516882
