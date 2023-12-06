with open('input.txt') as f:
    content = f.read()

# content = '''Time:      7  15   30
# Distance:  9  40  200'''

time, distance = content.split('\n', maxsplit=1)
time_name, times = time.split(':')
distance_name, distances = distance.split(':')
times = [int(t) for t in times.split(' ') if t]
distances = [int(d) for d in distances.split(' ') if d]
score = 1
for t, d in zip(times, distances):
    distances = ((t - ts) * ts for ts in range(1, t))
    win = [wd for wd in distances if wd > d]
    score *= len(win)
print(score)
