from itertools import cycle

with open('input.txt') as f:
    content = f.read()

# content = '''RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)'''

instructions_type, raw_instructions = content.split('\n\n')
instructions = {}
for key, value in (i.split('=') for i in raw_instructions.split('\n') if i):
    key = key.strip()
    value = value.strip(' )(').replace(' ', '').split(',')
    instructions[key] = value

pattern = [0 if it == 'L' else 1 for it in instructions_type]

instructions_pattern = cycle(pattern)
step = 0
current_instruction = 'AAA'
while True:
    step += 1
    i_type = next(instructions_pattern)
    current_instruction = instructions[current_instruction][i_type]
    print(current_instruction)
    if current_instruction == 'ZZZ':
        break

print(step)  # 16697
