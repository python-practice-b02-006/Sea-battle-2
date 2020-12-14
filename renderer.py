from globaldata import (Colors, pixels_per_cell)  
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
        for i in range(len(cells_of_game_field)):
            for j in range(len(cells_of_game_field[i])):
                self.draw_cell(screen, cells_of_game_field[i][j], i, j)
    
    def draw_cell(self, screen, cell, m, n):
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
    
    def finish_the_game(self, screen, color, color_name):
        '''
        Displays caption:"/color_name/ игрок побеждает!"

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.
        color : TYPE tuple of int-s
            DESCRIPTION. The color of text.
        color_name : TYPE string
            DESCRIPTION. This should be written in the caption.

        Returns
        -------
        None.

        '''
        screen.fill(c.BLACK)
        pass
    

if __name__ == "__main__":
    print("This module is not for direct call!")