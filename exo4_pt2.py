from data_exo4 import data_ws

def count_mas_cross(grid):
    """
    Counts the number of 'MAS' patterns in the form of a cross:
    input: list of strings (grid)
    output: integer
    """
    rows, colums = len(grid), len(grid[0])
    count = 0

    def test(y, x, ch):
        """Check if a specific character exists at (y, x) in the grid."""
        if 0 <= y < rows and 0 <= x < colums and grid[y][x] == ch:
            return True
        return False

    # Loop through the grid
    for r in range(1, rows - 1):  # Start from 1 to avoid boundary issues
        for c in range(1, colums - 1):  # Start from 1 to avoid boundary issues
            # Check if 'A' is at the center of the cross
            if test(r, c, 'A'):
                # M.M / .A. / S.S (Standard)
                if (test(r + 1, c - 1, 'M') and test(r + 1, c + 1, 'M') and 
                    test(r - 1, c - 1, 'S') and test(r - 1, c + 1, 'S')):
                    count += 1
                # version: S.S / .A. / M.M
                elif (test(r + 1, c - 1, 'S') and test(r + 1, c + 1, 'S') and 
                      test(r - 1, c - 1, 'M') and test(r - 1, c + 1, 'M')):
                    count += 1
                # version: S.M / .A. / S.M
                elif (test(r + 1, c - 1, 'S') and test(r + 1, c + 1, 'M') and 
                      test(r - 1, c - 1, 'S') and test(r - 1, c + 1, 'M')):
                    count += 1
                # version: M.S / .A. / M.S
                elif (test(r + 1, c - 1, 'M') and test(r + 1, c + 1, 'S') and 
                      test(r - 1, c - 1, 'M') and test(r - 1, c + 1, 'S')):
                    count += 1
    return count


def convert_to_grid(input_string):
    """
    Convert a multiline string into a list of strings (grid).
    input: multiline string
    output: list of strings
    """
    # Split the input string by new lines to get the rows
    grid = input_string.strip().split('\n')
    return grid


# Test with website data
grid = convert_to_grid(data_ws)

# Count occurrences of 'MAS' cross pattern
print(count_mas_cross(grid))
