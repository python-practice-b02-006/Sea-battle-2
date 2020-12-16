import pygame
from pygame.draw import *
from globaldata import (Colors, pixels_per_cell, left_indent, top_indent)  
c = Colors()

class Renderer():
    '''
    Visualizes everything.
    '''
    def __init__(self, screen):
        pygame.init()
        screen.fill(c.BLACK)
        background_image = pygame.image.load("fon.jpg")
        screen.blit(background_image, [0, 0])
        pygame.display.update()
    
    def draw_game_field(self, screen, cells_of_game_field, ships):
        '''
        Draws game field with objects on it.

        Parameters
        ----------
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.
        game_field : TYPE list of lists
            DESCRIPTION. 2-dimensional list with data about squares.
        ships : TYPE list of lists of objects
            DESCRIPTION. The list of lists of ships of players.

        Returns
        -------
        None.

        '''
        screen.fill(c.BLACK)
        for i in range(len(cells_of_game_field)):
            for j in range(len(cells_of_game_field[i])):
                self.draw_cell(screen, cells_of_game_field[i][j], i, j)
        for i in range(len(ships)):
            for j in range(len(ships[i])):
                if ships[i][j].is_chosen:
                    self.highlight_chosen_ship(screen, ships[i][j])
                    
    def highlight_chosen_ship(self, screen, ship):
        '''
        Draws a rectangle around the ship.

        Parameters
        ----------
        ship : TYPE object
            DESCRIPTION. object of BattleShip
        screen : TYPE Pygame screen.
            DESCRIPTION. Where everything is drawn.

        Returns
        -------
        None.

        '''
        pass # Use method ship.rect() - data about needed rectangle.
        
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
        Draws button.

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
