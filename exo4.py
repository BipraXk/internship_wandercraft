from data_exo4 import data_ws
def count_word_occurences(word,grid):
    """
    Counts the number of times "XMAS" appears in the grid in any direction.
    input: string, list of string
    output: integer
    """
    rows, colums = len(grid), len(grid[0])
    count = 0

    def check_direction(r, c, dr, dc):
        """
        check direction of word
        input: 4 integer
        output: boolean
        """
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= colums or grid[nr][nc] != word[i]:
                return False  
        return True
    
    # Check all positions in the grid
    for r in range(rows):
        for c in range(colums):
            # Check in 8 possible directions
            directions = [
                (0, 1),  (0, -1), (1, 0),  (-1, 0), (1, 1), (-1, -1), (1, -1),  (-1, 1), 
            ]
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
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
# test with website data

grid = convert_to_grid(data_ws)
word = "XMAS"
# Count occurrences of "XMAS"
print(count_word_occurences(word,grid)) 
