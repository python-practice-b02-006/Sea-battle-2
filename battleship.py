from globaldata import * 

class BattleShip():
    '''
    Contains attributes and methods of the battleship.
    '''
    def __init__(self, colour, x, y, orientation, toughness, movement_points):
        '''
        Creates an object of battleship.

        Parameters
        ----------
        colour : TYPE tuple
            DESCRIPTION. A colour of the ship.
        x : TYPE int 
            DESCRIPTION. x coordinate of central square of front side of the
            battleship.
        y : TYPE int
            DESCRIPTION. y coordinate of central square of front side of the
            battleship.
        orientation : TYPE string
            DESCRIPTION. Shows where the front side of the battleship is
            directed to. 
        toughness : TYPE int
            DESCRIPTION. An amount of health points.
        movement_points : TYPE int
            DESCRIPTION. Maximum amount of squares to move in one turn.

        Returns
        -------
        None.

        '''
        self.x_coord = x
        self.y_coord = y
        self.orientation = orientation
        self.colour = colour
        self.toughness = toughness
        self.movement_points = movement_points
        self.structure = [[[None, colour],     [None, colour], [None, colour]],     #Front side.
                          [["cannon", colour], [None, colour], ["cannon", colour]],
                          [[None, colour],     [None, colour], [None, colour]],
                          [[None, colour],     [None, colour], [None, colour]],
                          [["cannon", colour], [None, colour], ["cannon", colour]],
                          [[None, colour],     [None, colour], [None, colour]]]     #Back side.

if __name__ == "__main__":
    print("This module is not for direct call!")    