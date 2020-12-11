class Cell():
    '''
    Stores data about certain cell.
    '''
    def __init__(self, type_, color, orientation = None, is_active=True, 
                 is_destroyed=False):
        self.type = type_
        self.color = color
        self.orientation = orientation
        self.is_active = is_active
        self.is_destroyed = is_destroyed


from globaldata import Colors
c = Colors()

class GameField():
    '''
    Stores all data about cells of gamefield.
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
            self.cells.append([])
            for j in range(self.hight):
                self.cells[i].append(Cell("Water", c.BLUE))        
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
                    