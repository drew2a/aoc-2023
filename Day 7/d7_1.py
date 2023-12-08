from collections import Counter
from functools import cmp_to_key

with open('input.txt') as f:
    content = f.readlines()

# content = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.split('\n')

strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def find_type(a):
    counter = Counter(a)
    mc = counter.most_common()
    if len(mc) == 1:  # Five of a kind
        return 6
    if len(mc) == 2:
        if mc[0][1] == 4:  # Four of a kind
            return 5
        if mc[0][1] == 3 and mc[1][1] == 2:  # Full house
            return 4
    if len(mc) == 3:
        if mc[0][1] == 3:  # Three of a kind
            return 3
        if mc[0][1] == 2 and mc[1][1] == 2:  # Two pair
            return 2
    if len(mc) == 4:  # One pair
        return 1

    return 0  # High card


# print(find_type('AAAAA'))
# print(find_type('AAAAB'))
# print(find_type('AAABB'))
# print(find_type('AAABC'))
# print(find_type('AABBC'))
# print(find_type('AABCD'))
# print(find_type('ABCDE'))


def greater(a, b):
    a_type = find_type(a)
    b_type = find_type(b)
    if a_type == b_type:
        for a_ch, b_ch in zip(a, b):
            a_score = strengths[a_ch]
            b_score = strengths[b_ch]
            if a_score == b_score:
                continue
            elif a_score > b_score:
                return 1
            else:
                return -1
    elif a_type > b_type:
        return 1
    else:
        return -1
    return 0


bids = dict(a.split(' ') for a in content)
score = 0
for rank, hand in enumerate(sorted(bids, key=cmp_to_key(greater)), 1):
    score += int(bids[hand]) * rank
print(score)  # 249483956
