from gamefield import Cell
from globaldata import pixels_per_cell

class BattleShip():
    '''
    Contains attributes and methods of the battleship.
    '''
    max_movement_points = 8
    dictionary_of_orientations = {"left" : 0, "up" : 1, "right" : 2, 
                                      "down" : 3}
    list_of_orientations = ["left", "up", "right", "down"]
    def __init__(self, color, x, y, orientation, number, toughness=12, 
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
        is_chosen : TYPE bool
            DESCRIPTION. True if the ship was clicked, else False
        number : TYPE int
            DESCRIPTION. An absolute number of the ship.
        

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
        self.number = number
        empty_cell = Cell("empty", color, number = self.number)
        left_cannon = Cell("cannon", color, self.list_of_orientations[
            (self.dictionary_of_orientations[orientation] - 1) % 4], 
            number = self.number)
        right_cannon = Cell("cannon", color, self.list_of_orientations[
            (self.dictionary_of_orientations[orientation] + 1) % 4], 
            number = self.number)
        self.structure = [[empty_cell,  empty_cell, empty_cell],  #Front side.
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell],
                          [empty_cell,  empty_cell, empty_cell],
                          [left_cannon, empty_cell, right_cannon],
                          [empty_cell,  empty_cell, empty_cell]]   #Back side.
    
    def rect(self):
        '''
        Returns data about rectangle of the ship.

        Returns
        -------
        list of int-s
            DESCRIPTION. Pygame rectangle data in game field coordinates.

        '''
        d = dict([("up", [self.x_coord - 1, self.y_coord, 3, 6]),
                  ("down", [self.x_coord - 1, self.y_coord - 5, 3, 6]),
                  ("left", [self.x_coord, self.y_coord - 1, 6, 3]),
                  ("right", [self.x_coord - 5, self.y_coord - 1, 6, 3])
                  ]) # Dictionary of sth that will be returned.
        return d[self.orientation]

    def update_movement_points(self):
        '''
        Updates movement points of the ship.

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
        #Decrease movement points.
        if direction == self.orientation:
            self.movement_points -= 1
        else:
            self.movement_points -= 2
        #Change coordinates.
        d = dict([("up", dict([("up", [0, -1]), ("down", [0, -1]), ("left", [2, -2]), ("right", [-2, -2])])),
                  ("down", dict([("up", [0, 1]), ("down", [0, 1]), ("left", [2, 2]), ("right", [-2, 2])])),
                  ("left", dict([("up", [-2, 2]), ("down", [-2, -2]), ("left", [-1, 0]), ("right", [-1, 0])])),
                  ("right", dict([("up", [2, 2]), ("down", [2, -2]), ("left", [1, 0]), ("right", [1, 0])]))
                  ])#Dictionary of coordinates changes. [delta x, delta y]
        self.x_coord += d[direction][self.orientation][0]
        self.y_coord += d[direction][self.orientation][1]
        #Change orientation.
        if (self.dictionary_of_orientations[direction] - 
            self.dictionary_of_orientations[self.orientation]) % 2 != 0:
            self.orientation = direction
        #Change orientation of cannons.
        self.structure[1][0].orientation = self.list_of_orientations[
            (self.dictionary_of_orientations[self.orientation] - 1) % 4]
        self.structure[1][2].orientation = self.list_of_orientations[
            (self.dictionary_of_orientations[self.orientation] + 1) % 4]
        self.structure[4][0].orientation = self.list_of_orientations[
            (self.dictionary_of_orientations[self.orientation] - 1) % 4]
        self.structure[4][2].orientation = self.list_of_orientations[
            (self.dictionary_of_orientations[self.orientation] + 1) % 4]
        
    def moved(self, direction):
        '''
        Returns an object of theoretically moved ship in the needed direction.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where the ship should go.

        Returns
        -------
        object of BattleShip
            Description. An object of theoretically moved ship.

        '''
        #Coordinates.
        d = dict([("up", dict([("up", [0, -1]), ("down", [0, -1]), ("left", [2, -2]), ("right", [-2, -2])])),
                  ("down", dict([("up", [0, 1]), ("down", [0, 1]), ("left", [2, 2]), ("right", [-2, 2])])),
                  ("left", dict([("up", [-2, 2]), ("down", [-2, -2]), ("left", [-1, 0]), ("right", [-1, 0])])),
                  ("right", dict([("up", [2, 2]), ("down", [2, -2]), ("left", [1, 0]), ("right", [1, 0])]))
                  ])#Dictionary of coordinates changes. [delta x, delta y]
        x = self.x_coord + d[direction][self.orientation][0]
        y = self.y_coord + d[direction][self.orientation][1]
        #Orientation.
        if (self.dictionary_of_orientations[direction] - 
            self.dictionary_of_orientations[self.orientation]) % 2 != 0:
            orientation = direction
        else:
            orientation = self.orientation
        return BattleShip(self.color, x, y, orientation, self.number)
        
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
        if direction == self.orientation:
            if self.movement_points == 0:
                return False
            else:
                return True
        else:
            if self.movement_points < 2:
                return False
            else:
                return True
    
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
        rect = self.moved(direction).rect() # A rectangle of theoretically 
                                                                #moved ship.
        if ((rect[0] < 0) or (rect[1] < 0) or ((rect[0] + rect[2] - 1) >=
                                              game_field.width) or 
            ((rect[1] + rect[3] - 1) >= game_field.hight)):
            return True
        else:
            return False
      
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
        will_collide = False
        rect = self.moved(direction).rect() # A rectangle of theoretically 
                                                                #moved ship.
        for i in range(rect[2]):
            for j in range(rect[3]):
                if ((game_field.cells[rect[0] + i][rect[1] + j].type != 
                     "water") and (game_field.cells[rect[0] + i]
                                   [rect[1] + j].owner != self.number)):
                    will_collide = True
        return will_collide                    
                    
    
if __name__ == "__main__":
    print("This module is not for direct call!")    
