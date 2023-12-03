with open('input.txt') as f:
    content = f.readlines()

s = 0
for line in content:
    first, last = None, None
    numeric = (ch for ch in line if ch.isnumeric())
    for n in numeric:
        if not first:
            first = n
        last = n

    s += int(first + last)

print(s)
