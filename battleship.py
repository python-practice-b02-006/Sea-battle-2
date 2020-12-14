from gamefield import Cell
from globaldata import pixels_per_cell

class BattleShip():
    '''
    Contains attributes and methods of the battleship.
    '''
    max_movement_points = 8
    def __init__(self, color, x, y, orientation, toughness=12, 
                 movement_points=8, is_chosen=False):
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
        self.is_chosen = is_chosen
        dictionary_of_orientations = {"left" : 0, "up" : 1, "right" : 2, 
                                      "down" : 3}
        list_of_orientations = ["left", "up", "right", "down"]
        empty_cell = Cell("empty", color)
        left_cannon = Cell("cannon", color, list_of_orientations[
            (dictionary_of_orientations[orientation] - 1) % 4])
        right_cannon = Cell("cannon", color, list_of_orientations[
            (dictionary_of_orientations[orientation] + 1) % 4])
        self.structure = [[empty_cell,  empty_cell, empty_cell],  #Front side.
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell],
                          [empty_cell,  empty_cell, empty_cell],
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell]]   #Back side.
        

    def update_movement_points(self):
        '''
        updates movement points of the ship.

        Returns
        -------
        None.

        '''
        self.movement_points = self.max_movement_points
        
    def activate_cannons(self):
        '''
        Makes cannons of the ship active.

        Returns
        -------
        None.

        '''
        self.structure[1][0].is_active = True
        self.structure[1][2].is_active = True
        self.structure[4][0].is_active = True
        self.structure[4][2].is_active = True
        
    def make_not_chosen(self):
        '''
        Makes the ship not chosen.

        Returns
        -------
        None.

        '''
        self.is_chosen = False
        
    def move(self, direction):
        '''
        Moves the ship in the needed direction.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship should go.

        Returns
        -------
        None.

        '''
        pass
    
    def is_possible_to_move(self, direction, game_field):
        '''
        Checks if the movement is possible.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship is going to go.
        game_field : TYPE object of GameField
            DESCRIPTION. Contains all data about cells of game field.

        Returns
        -------
        bool
            DESCRIPTION. True if the movement is possible, else False.
        string
            DESCRIPTION. The message with the reason of inability to move.
        '''
        if (self.is_enough_movement_points(direction) and 
            not self.will_be_out_of_game_field(direction, game_field) and
            not self.will_collide(direction, game_field)):
            return [True, ""]
        else:
            if not self.is_enough_movement_points(direction):
                return [False, "Не достаточно очков передвижения!"]
            else:
                return [False, "Движение в этом направлении невозможно!"]
        
    def is_enough_movement_points(self, direction):
        '''
        Checks if the ship has enough movement points to move or not.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship is going to go.
        
        Returns
        -------
        bool
            DESCRIPTION. True if the ship has enough movement points to move,
            else False.

        '''
        pass
    
    def will_be_out_of_game_field(self, direction, game_field):
        '''
        Checks if the ship is out of game field after movement or not.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship is going to go.
        game_field : TYPE object of GameField
            DESCRIPTION. Contains all data about cells of game field.

        Returns
        -------
        bool
            DESCRIPTION. True if the ship is out of game field after movement,
            else False.

        '''
        pass
      
    def will_collide(self, direction, game_field):
        '''
        Checks if the ship collides with others after movement or not.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship is going to go.
        game_field : TYPE object of GameField
            DESCRIPTION. Contains all data about cells of game field.

        Returns
        -------
        bool
            DESCRIPTION. True if the ship collides with others after movement,
            else False.

        '''
        pass
    
if __name__ == "__main__":
    print("This module is not for direct call!")    