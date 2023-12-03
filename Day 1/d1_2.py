with open('input.txt') as f:
    content = f.readlines()

dictionary = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
              'nine': '9'}
lengths = {len(k) for k in dictionary.keys()}

s = 0
for line in content:
    first, last = None, None


    def check_f_l(ch, first):
        return first or ch, ch


    for i in range(len(line)):
        if line[i].isnumeric():
            first, last = check_f_l(line[i], first)
            continue

        keys = [line[i:i + l:] for l in lengths]
        for k in keys:
            if replacement := dictionary.get(k):
                first, last = check_f_l(replacement, first)
                break
    s += int(first + last)

print(s)
