import math
from itertools import cycle

with open('input.txt') as f:
    content = f.read()

# content = '''LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)'''

instructions_type, raw_instructions = content.split('\n\n')
instructions = {}
for key, value in (i.split('=') for i in raw_instructions.split('\n') if i):
    key = key.strip()
    value = value.strip(' )(').replace(' ', '').split(',')
    instructions[key] = value

pattern = [0 if it == 'L' else 1 for it in instructions_type]
instructions_pattern = cycle(pattern)
step = 0
reached_z = {}
current_instructions = {i for i in instructions if i[2] == 'A'}
finish_instructions = {i for i in instructions if i[2] == 'Z'}
print(current_instructions)
print(finish_instructions)
repeat = True
while repeat:
    step += 1
    i_type = next(instructions_pattern)
    new_current_instructions = set()
    for i in current_instructions:
        new_instruction = instructions[i][i_type]
        new_current_instructions.add(new_instruction)
        if new_instruction in finish_instructions:
            reached_z[new_instruction] = step
            if len(reached_z) == len(finish_instructions):
                repeat = False

    current_instructions = new_current_instructions

print(reached_z)
x = math.lcm(*reached_z.values())
print(x)  # 10668805667831
