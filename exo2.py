from data_exo2 import data_ws

def is_secured(rapport):
    """
    verify the security of a report
    input: report
    output: boolean, True if secured, False if not
    """
    # verify if every report is increasing or decreasing with a difference of max. 3 between each element
    increasing = all(0 < rapport[i+1] - rapport[i] <= 3 for i in range(len(rapport) - 1))
    decreasing = all(0 < rapport[i] - rapport[i+1] <= 3 for i in range(len(rapport) - 1))
    return increasing or decreasing

def nb_secu_rep(rapports):
    """
    Calculate number of secure reports 
    input: list of report
    output: integer of secure report
    """
    # sum the number of secured reports
    return sum(1 for rapport in rapports if is_secured(rapport))

# test with website data
def convert_to_matrix(input_string):
    # Split the input string by new lines to get the rows
    rows = input_string.strip().split('\n')
    
    # Convert each row into a list of integers
    matrix = [list(map(int, row.split())) for row in rows]
    return matrix

reports = convert_to_matrix(data_ws)

print(nb_secu_rep(reports))
