with open('input.txt') as f:
    content = f.read()

# content = '''Time:      7  15   30
# Distance:  9  40  200'''

time, distance = content.split('\n', maxsplit=1)
time_name, times = time.split(':')
distance_name, distances = distance.split(':')
t = int(times.replace(' ', ''))
d = int(distances.replace(' ', ''))
distances = [int(d) for d in distances.split(' ') if d]
dd = ((t - ts) * ts for ts in range(1, t))
win = [wd for wd in dd if wd > d]
print(len(win))
