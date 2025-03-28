from data_exo2 import data_ws

def is_secured(rapport):
    """
    Verify the security of a report
    input: report
    output: boolean, True if secured, False if not
    """
    # Check if the report is strictly increasing or strictly decreasing with a max difference of 3
    increasing = all(0 < rapport[i+1] - rapport[i] <= 3 for i in range(len(rapport) - 1))
    decreasing = all(0 < rapport[i] - rapport[i+1] <= 3 for i in range(len(rapport) - 1))
    return increasing or decreasing

def is_secured_with_dampener(rapport):
    """
    Verify the security of a report with the Problem Dampener: 
    allowing the removal of one level to make it secure.
    input: report
    output: boolean, True if secured with or without removing one level, False if not
    """
    # Check if report is already secure
    if is_secured(rapport):
        return True
    
    # Try removing one element and check if the result is secure
    for i in range(len(rapport)):
        modified_report = rapport[:i] + rapport[i+1:]  # Remove the element at index i
        if is_secured(modified_report):
            return True
    
    return False

def nb_secu_rep(rapports):
    """
    Calculate number of secure reports with the Problem Dampener
    input: list of report
    output: integer of secure report
    """
    # Sum the number of secured reports (with or without dampener)
    return sum(1 for rapport in rapports if is_secured_with_dampener(rapport))

# test with website data
def convert_to_matrix(input_string):
    # Split the input string by new lines to get the rows
    rows = input_string.strip().split('\n')
    
    # Convert each row into a list of integers
    matrix = [list(map(int, row.split())) for row in rows]
    
    return matrix

# Convert the reports from the data
reports = convert_to_matrix(data_ws)

# Print the number of safe reports
print(nb_secu_rep(reports))
