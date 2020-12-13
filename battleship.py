from gamefield import Cell

class BattleShip():
    '''
    Contains attributes and methods of the battleship.
    '''
    max_movement_points = 8
    def __init__(self, color, x, y, orientation, toughness=12, 
                 movement_points=8):
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
        self.color = color
        self.toughness = toughness
        self.movement_points = movement_points
        dictionary_of_orientations = {"left" : 0, "up" : 1, "right" : 2, 
                                      "down" : 3}
        list_of_orientations = ["left", "up", "right", "down"]
        empty_cell = Cell("empty", color)
        left_cannon = Cell("cannon", color, list_of_orientations[
            (dictionary_of_orientations[orientation] - 1) % 4])
        right_cannon = Cell("cannon", color, list_of_orientations[
            (dictionary_of_orientations[orientation] + 1) % 4])
        self.structure = [[empty_cell,  empty_cell, empty_cell],     #Front side.
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell],
                          [empty_cell,  empty_cell, empty_cell],
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell]]     #Back side.

    def update_movement_points(self):
        '''
        updates movement points of the ship.

        Returns
        -------
        None.

        '''
        self.movement_points = self.max_movement_points

if __name__ == "__main__":
    print("This module is not for direct call!")    