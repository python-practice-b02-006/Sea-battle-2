from globaldata import (Colors, screen_width, screen_hight, game_field_width,
                        game_field_hight)  
c = Colors()

class Renderer():
    '''
    Visualizes everything.
    '''
    def __init__(self):
        pass
    
    def draw_game_field(self, screen, cells_of_game_field):
        '''
        Draws game field with objects on it.

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.
        game_field : TYPE list of lists
            DESCRIPTION. 2-dimensional list with data about squares.
        Returns
        -------
        None.

        '''
        screen.fill(c.BLACK)
        k = min(screen_width // game_field_width, screen_hight //
                game_field_hight) # An amount of pixels in the side of the 
                                                              #cell.(int type)
        for i in range(len(cells_of_game_field)):
            for j in range(len(cells_of_game_field[i])):
                self.draw_cell(screen, cells_of_game_field[i][j], i, j, k)
    
    def draw_cell(self, screen, cell, m, n, k):
        '''
        Draws a certain cell.

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.
        cell : TYPE object
            DESCRIPTION. object of class Cell
        m : TYPE int 
            DESCRIPTION. x coordinate of the cell on the gamefield
        n : TYPE int 
            DESCRIPTION. y coordinate of the cell on the gamefield
        k : TYPE int 
            DESCRIPTION. An amount of pixels in the side of the cell.
        Returns
        -------
        None.

        '''
        pass 
    
    def draw_button(self, screen, button_name, button_location):
        '''
        Draws starting button.

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.


        Returns
        -------
        None.

        '''
        screen.fill(c.BLACK)
        pass
    

if __name__ == "__main__":
    print("This module is not for direct call!")