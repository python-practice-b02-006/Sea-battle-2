class GameField():
    '''
    Stores all data about squares of gamefield.
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
        self.squares = []
        for i in range(game_field_width):
            self.squares.append([])
            for j in range(game_field_hight):
                self.squares[i].append(["Water", None])
    
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
        for i in range(len(ships)):
            for j in range(len(ships[i])):
                for k in range(len(ships[i][j].structure)):
                    for l in range(len(ships[i][j].structure[k])):
                        if ships[i][j].orientation == "up":
                            self.squares[ships[i][j].x_coord - 1 + l][
                                ships[i][j].y_coord + k
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "down":
                            self.squares[ships[i][j].x_coord + 1 - l][
                                ships[i][j].y_coord - k
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "left":
                            self.squares[ships[i][j].x_coord + k][
                                ships[i][j].y_coord + 1 - l
                                ] = ships[i][j].structure[k][l]
                        if ships[i][j].orientation == "right":
                            self.squares[ships[i][j].x_coord - k][
                                ships[i][j].y_coord - 1 + l
                                ] = ships[i][j].structure[k][l]
                    