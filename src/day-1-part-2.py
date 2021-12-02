import os

with open(os.path.join('input', 'day-1-input.txt'), 'r') as f:
    vals = [int(x.strip('\n')) for x in f.readlines()]
    
window_depths = []

for i in range(0, len(vals) - 2):
    window_depths.append(vals[i] + vals[i + 1] + vals[i + 2])

current_depth = window_depths.pop(0)
num_descents = 0

for x in window_depths:
    if x > current_depth:
        num_descents += 1
    current_depth = x

print(num_descents)