import os

with open(os.path.join('input', 'day-3-input.txt'), 'r') as f:
    vals = [x.strip('\n') for x in f.readlines()]
    
gamma_bin_string = ""
epsilon_bin_string = ""

for i in range(len(vals[0])):
    num_zeros = 0
    num_ones = 0
    
    for bin_string in vals:
        if bin_string[i] == '0':
            num_zeros += 1
        else:
            num_ones += 1
    
    if num_zeros > num_ones:
        gamma_bin_string += "0"
        epsilon_bin_string += "1"
    else:
        gamma_bin_string += "1"
        epsilon_bin_string += "0"
        
bin_string_len = len(gamma_bin_string)

gamma_val = 0
epsilon_val = 0

for i in range(bin_string_len):
    gammit_bit = gamma_bin_string[i]
    epsilon_bit = epsilon_bin_string[i]
    
    gamma_val += int(gammit_bit) * (2 ** (bin_string_len - i - 1))
    epsilon_val += int(epsilon_bit) * (2 ** (bin_string_len - i - 1))
    
print(gamma_val * epsilon_val)
