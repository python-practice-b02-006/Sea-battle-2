from menu import *
from renderer import *
from globaldata import *

class Manager():
    '''
    Manages game processes.
    '''
    def __init__(self):
        self.renderer = Renderer()
    
    def process(self, screen):
        '''
        Triggers all game processes.

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.

        Returns
        -------
        None.

        '''
        load_menu(screen)
        self.renderer.draw_game_field(screen, game_field)
        
        

if __name__ == "__main__":
    print("This module is not for direct call!")