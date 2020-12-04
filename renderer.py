from globaldata import * 

class Renderer():
    def __init__(self):
        pass
    
    def draw_game_field(self, screen, squares_of_game_field):
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
        screen.fill(BLACK)
        pass
    
    def draw_starting_button(self, screen):
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
        screen.fill(BLACK)
        pass
    

if __name__ == "__main__":
    print("This module is not for direct call!")