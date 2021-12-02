import os

with open(os.path.join('input', 'day-2-input.txt'), 'r') as f:
    vals = [x.strip('\n').split(' ') for x in f.readlines()]

pos_horz = 0
pos_vert = 0

for command in vals:
    direction = command[0]
    amount = int(command[1])
    
    if direction == 'forward':
        pos_horz += amount
    elif direction == 'down':
        pos_vert += amount
    elif direction == 'up':
        pos_vert -= amount
        
print(pos_horz * pos_vert)