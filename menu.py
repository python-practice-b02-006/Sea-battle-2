import pygame
from renderer import Renderer
from globaldata import FPS, rect_of_starting_button
from GUI import Button

clock = pygame.time.Clock() 

    
class Menu():
    '''
    Loads menu and contains other methods.
    '''
    def __init__(self):
        self.renderer = Renderer()
        self.starting_button = Button("Начать", rect_of_starting_button)
    
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
        self.renderer.draw_button(screen, self.starting_button.name, 
                                  self.starting_button.location)
        
    def load(self, screen):
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
        self.let_start(screen)
        started = False
        while not started:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    started = True 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ((event.button < 4) and 
                        (self.starting_button.is_clicked(event.pos[0], 
                                                         event.pos[1]))):
                        started = True
        

if __name__ == "__main__":
    print("This module is not for direct call!")