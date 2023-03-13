class Agent:
    def __init__(self, id: int, cost_structure: list()):

        """
        Cost structure: tuple in the form [Agent.id, number of units, cost per unit]
        """
        self.id = id
        self.cost_structure = cost_structure
        self.available = cost_structure
        self.allocated = 0
        self.cost = 0

    def allocate(self, units, cost):
        """ 
        allocates 'units' carbon reduction units to 'Agent'
        Increases Agent cost by 'cost' 
        """
        self.allocated += units
        self.cost += cost
        self.available.pop(0)
    
     
    def is_exhausted(self):
        """ 
        true: agent has been allocated all  carbon credit reductions available at fixed cost 
        false: agent is still capable of reducing emissionsat some fixed cost 
        """
        
        return not bool(self.avaialable)





    

        