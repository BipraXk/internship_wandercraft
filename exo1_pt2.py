from collections import Counter
from data_exo1 import data_ws

def distance(list1, list2):
    """
    calculate the distance between each element of list multiplied by 
    the number of times it appears then the total distance
    input: 2 lists
    output: 1 integer
    input: 2 lists
    output: 1 integer 
    """
    # count occurrences of elements in list2
    list2_count = Counter(list2)

    total_dist = 0
    if len(list1) != len(list2):
        raise ValueError('List are not the same size, calculations impossible!')
    elif len(list1) == len(list2):
    # for each element in list1, check how often it appears in list2 and calculate the score
        for num in list1:
            total_dist += num * list2_count[num]

    return total_dist


# test with website data
def string_to_tuple_list(data_str):
    # separate lines
    lines = data_str.splitlines()
    # convert lines to tuple
    tuple_list = []
    for line in lines:
        # separate each line
        values = line.split()
        if len(values) == 2:
            tuple_list.append((int(values[0]), int(values[1])))
    
    return tuple_list

# list of data as tuples
data_ws = string_to_tuple_list(data_ws)

# separate into 2 lists
list1, list2 = zip(*data_ws)

# convert to list
list1 = list(list1)
list2 = list(list2)


print(distance(list1,list2))