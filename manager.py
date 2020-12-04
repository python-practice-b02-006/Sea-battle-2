from menu import *
from renderer import *
from globaldata import *
from player import *
from gamefield import *

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
        player1 = Player(1, starting_set_of_ships_for_player1)
        player2 = Player(2, starting_set_of_ships_for_player2)
        game_field = GameField(game_field_width, game_field_hight)
        game_field.update([player1.ships, player2.ships])
        out = open('observe.txt', 'a')
        out = open('observe.txt', 'w')
        for i in range(30):
            print(game_field.squares[i], end='\n', file = out)
        self.renderer.draw_game_field(screen, game_field.squares)
        
        

if __name__ == "__main__":
    print("This module is not for direct call!")