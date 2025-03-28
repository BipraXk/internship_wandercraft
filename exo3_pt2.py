import re
from data_exo3 import data_ws

def sum_valid_multiplications(corrupted_memory):
    """
    Sum every mul(X,Y) pattern, considering the 'do()' and 'don't()' instructions.
    input: string
    output: integer
    """
    # Find all 'do()', 'don't()', and 'mul(X,Y)' patterns
    pattern = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted_memory)

    # Start with mul enabled by default
    mul_enabled = True
    total_sum = 0

    for match in matches:
        if match[0]:  # 'do()' found
            mul_enabled = True
        elif match[1]:  # 'don't()' found
            mul_enabled = False
        elif match[2] and match[3]:  # 'mul(X,Y)' found
            if mul_enabled:
                total_sum += int(match[2]) * int(match[3])

    return total_sum

# Test with website data
corrupted_memory = data_ws

print(sum_valid_multiplications(corrupted_memory))
