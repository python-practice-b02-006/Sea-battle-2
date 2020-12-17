class Cell():
    '''
    Stores data about certain cell.
    '''
    def __init__(self, type_, color, orientation = None, is_active=True, 
                 is_destroyed=False, is_chosen=False, number = 0, writing = ""
                 ):
        '''
        Initializes the cell.

        Parameters
        ----------
        type_ : TYPE string
            DESCRIPTION. The type of the cell.
        color : TYPE tuple of int-s
            DESCRIPTION. The color of the cell.
        orientation : TYPE string, optional
            DESCRIPTION. The default is None. Where the cell "looks" to.
        is_active : TYPE bool, optional
            DESCRIPTION. The default is True. True if the cell 
        is_destroyed : TYPE, optional
            DESCRIPTION. The default is False.
        is_chosen : TYPE, optional
            DESCRIPTION. The default is False.
        number : TYPE, optional
            DESCRIPTION. The default is 0. The number of ship-owner of the 
            cell.
        writing : TYPE string, optional
            DESCRIPTION. The default is "". Sth that will be written on the 
            cell.

        Returns
        -------
        None.

        '''
        self.type = type_
        self.color = color
        self.orientation = orientation
        self.is_active = is_active
        self.is_destroyed = is_destroyed
        self.is_chosen = is_chosen
        self.owner = number
        self.writing = writing


from globaldata import (Colors, pixels_per_cell, left_indent, top_indent)
c = Colors()

class GameField():
    '''
    Stores all data about cells of game field.
    '''
    def __init__(self, game_field_width, game_field_hight):
        '''
        Creates a 2-dimensional list which stores all squares.

        Parameters
        ----------
        game_field_width : TYPE int
            DESCRIPTION. The width of game field (along x axis) 
            (an amount of squares)
        game_field_hight : TYPE
            DESCRIPTION. The hight of game field (along y axis) 
            (an amount of squares)

        Returns
        -------
        None.

        '''
        self.cells = []
        self.width = game_field_width
        self.hight = game_field_hight
        for i in range(self.width):
            self.cells.append([])
            for j in range(self.hight):
                self.cells[i].append(Cell("water", c.BLUE))
    
    def update(self, ships):
        '''
        Updates the 2-dimensional list of squares of game field.

        Parameters
        ----------
        ships : TYPE list of lists of objects
            DESCRIPTION. The list of lists of ships of players.

        Returns
        -------
        None.

        '''
        for i in range(self.width):
            for j in range(self.hight):
                self.cells[i][j] = Cell("water", c.BLUE)        
        for i in range(len(ships)):
            for j in range(len(ships[i])):
                for k in range(len(ships[i][j].structure)):
                    for l in range(len(ships[i][j].structure[k])):
                        if ships[i][j].orientation == "up":
                            self.cells[ships[i][j].x_coord - 1 + l][
                                ships[i][j].y_coord + k
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "down":
                            self.cells[ships[i][j].x_coord + 1 - l][
                                ships[i][j].y_coord - k
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "left":
                            self.cells[ships[i][j].x_coord + k][
                                ships[i][j].y_coord + 1 - l
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "right":
                            self.cells[ships[i][j].x_coord - k][
                                ships[i][j].y_coord - 1 + l
                                ] = ships[i][j].structure[k][l]

    def make_cells_not_chosen(self):
        '''
        Makes cells of the game field not chosen.

        Returns
        -------
        None.

        '''
        for i in range(self.width):
            for j in range(self.hight):
                self.cells[i][j].is_chosen = False
    
    def make_clicked_cell_chosen(self, x, y):
        '''
        Make clicked cell chosen.

        Parameters
        ----------
        x : TYPE int 
            DESCRIPTION. x mouse coordinate
        y : TYPE int
            DESCRIPTION. y mouse coordinate

        Returns
        -------
        None.

        '''
        (self.cells[int((x - left_indent) // pixels_per_cell)]
         [int((y - top_indent) // pixels_per_cell)].is_chosen) = True
        print((x - left_indent) // pixels_per_cell, (y - top_indent) //
              pixels_per_cell, "chosen")
    
    def aim_is_close_enough(m, n, x, y):
        '''
        Checks if aim is close enough to the cannon.

        Parameters
        ----------
        m : TYPE int
            DESCRIPTION. x coordinate of the cannon in game field coordinates.
        n : TYPE int  
            DESCRIPTION. y coordinate of the cannon in game field coordinates.
        x : TYPE int
            DESCRIPTION. x coordinate of the aim in real coordinates.
        y : TYPE int
            DESCRIPTION. y coordinate of the aim in real coordinates.

        Returns
        -------
        bool
            DESCRIPTION. True if aim is close enough to the cannon, else
            False.

        '''
        pass
        
    
if __name__ == "__main__":
    print("This module is not for direct call!")
