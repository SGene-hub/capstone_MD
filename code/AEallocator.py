import numpy as np

def allocator(tuples: list(), m): 
    """ 
    - take in tuples for different agents, as an ordered list 
        in the form [agent_index, number of units, cost per unit]
    1) sort tuples in ascending order of cost 
        a. if two tuples have the same cost, the order does not matter for final cost 
            but we will sort by decreasing ui (or check paper)
    2) initialise cost = 0;
    2) pick first element of queue 
    3)  - if ui > m
        1) cost = cost + m
        2) return cost
        - if ui > m
        1) cost = cost + ui
        2) tuple is removed from queue
        3) m = m - ui 
        3) repeate from 2
     """
    # sort tuples
    tuples.sort(key = lambda x: x[2])

    # initialise cost 
    cost = 0

    # allocate 
    while m > 0:
        tuple = tuples[0]
        units = tuple[1]
        cost_unit = tuple[2]
        

        if m >= units: 
            cost += units * cost_unit
            m -= units
            tuples.pop(0)
        else: 
            cost += m * cost_unit
            # update units in tuple that is not exhausted
            tuples[0][1] = units - m
            # allocated all emission units
            m = 0
           
    
    return cost
        
    
    # TODO: tweak to register how many units and cost each egent incurs


    