import pygame
from renderer import *
from globaldata import *
clock = pygame.time.Clock() 


def load_menu(screen):
    '''
    Suggests choosing settings if there are any. Then lets players start
    playing.

    Parameters
    ----------
    screen : TYPE Pygame screen.
        DESCRIPTION. Where everything is drawn.


    Returns
    -------
    None.

    '''
    menu = Menu()
    menu.let_start(screen)
    started = False
    while not started:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                started = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((event.button == 1) and 
                    (menu.starting_button_is_clicked(event.pos[0], 
                                                     event.pos[1]))):
                    started = True
    

class Menu():
    '''
    Contains all methods for "load_menu" function.
    '''
    def __init__(self):
        self.renderer = Renderer()
    
    def let_start(self, screen):
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
        """
        Displays a button "START".

        Returns
        -------
        None.

        """
        self.renderer.draw_starting_button(screen)

    def starting_button_is_clicked(self, x_mouse_coord, y_mouse_coord):
        '''
        Checks if starting button is clicked or not.

        Parameters
        ----------
        x_mouse_coord : TYPE int
            DESCRIPTION. x coordinate of mouse cursor.
        y_mouse_coord : TYPE int
            DESCRIPTION. y coordinate of mouse cursor.

        Returns
        -------
        bool
            DESCRIPTION. Returns True if starting button is clicked, else 
            returns False.

        '''
        if ((x_mouse_coord >= rect_of_starting_button[0]) and 
            (x_mouse_coord <= rect_of_starting_button[0] +
             rect_of_starting_button[2]) and 
            (y_mouse_coord >= rect_of_starting_button[1]) and 
            (y_mouse_coord <= rect_of_starting_button[1] +
             rect_of_starting_button[3])):
            return True
        else:
            return False
        

if __name__ == "__main__":
    print("This module is not for direct call!")