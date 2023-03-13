import random
import Agent

def CreateAgents(N: int, units_OM: int):
    """
    create N Agents
    units_OM: order of magnitude of units per agent
    """
    agents = []
    for i in range(N):

        units = random.randint(round(units_OM*0.1+1), units_OM+1)
        
        # TODO: choose number of tuples NT better
        NT = random.randint(5, 50)

        cost_curve = CreateCostCurve(units=units, id=i, NT=NT)
        agents.append(Agent(id = i, cost_structure=cost_curve))
    
    return agents


def CreateCostCurve(units: int, id: int, NT):
    """
    Create for agent 'id' a quasi linear, monotonically increasing, 
    piecewise continuous cost curve made of NT tuples, with 'units' 
    carbon reduction units
    Every tuple has the same number of units. Note that total number 
    of units might be higher than units, if U > units*NT
    """
    # initialise cost per unit
    CU = 0
    # initialise maximum and minimum cost per unit increase. 
    # They will be monotonically increasing to reflect the increasing cost of reducitng the next set of carbon emission units
    maxincrease = 1
    minincrease = 0
    tuples = []

    # TODO: add variability in units per tuple
    U = units / NT

    while units > 0:

        increase = random.randint(0, 10)
        maxincrease += increase

        # minimum increase is strictly bounded by maximum increase
        minincrease += random.randint (0, increase)

        CU += random.randint(minincrease,maxincrease)
        
        # create tuple
        tuples.append([id,U,CU])

        # update units
        units -= U

    return tuples
    


# TODO: DOCUMENT tuples are snot stored as per paper, but U indiicated the new units that can be reduced at that price