from globaldata import * 

class battleship():
    '''
    Contains attributes and methods of the battleship.
    '''
    toughness = 12
    movement_points = 8
    structure = [[None,     None,  None], 
                 ["cannon", None, "cannon"],
                 [None,     None,  None],
                 [None,     None,  None],
                 ["cannon", None, "cannon"],
                 [None,     None,  None]]
    
    def __init__(self, owner_number):
        self.owner = owner_number
        
    