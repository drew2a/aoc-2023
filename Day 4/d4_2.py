from collections import defaultdict

with open('input.txt') as f:
    content = f.readlines()

# content = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')

instances = defaultdict(int)
for card_number, line in enumerate(content, 1):
    win_card, your_card = line.split('|')
    _, win_points = win_card.split(':')
    your_points = {p for p in your_card.replace('\n', '').split(' ') if p}
    win_points = {p for p in win_points.split(' ') if p}
    card_score = len(your_points.intersection(win_points))
    instances[card_number] += 1
    for c in range(card_number + 1, card_number + card_score + 1):
        instances[c] += instances[card_number]

print(sum(instances.values())) #5625994
