import os

with open(os.path.join('input', 'day-1-part-1-input.txt'), 'r') as f:
    vals = [int(x.strip('\n')) for x in f.readlines()]
    
current_depth = vals.pop(0)
num_descents = 0

for x in vals:
    if x > current_depth:
        num_descents += 1
    current_depth = x
    
print(num_descents)