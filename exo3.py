import re
from data_exo3 import data_ws

def sum_valid_multiplications(corrupted_memory):
    """
    sum every mul(X,Y) pattern
    input: string
    output: integer
    """
    #find valid "mul(X,Y)" patterns
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted_memory)
    
    # sum every mul(X,Y) pattern
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

# test with website data
corrupted_memory = data_ws

print(sum_valid_multiplications(corrupted_memory))
