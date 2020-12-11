from menu import Menu
from renderer import Renderer
from globaldata import (starting_set_of_ships_for_player1,
                        starting_set_of_ships_for_player2,
                        game_field_width, game_field_hight)
from player import Player
from gamefield import GameField

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
        menu = Menu()
        menu.load(screen)
        player1 = Player(1, starting_set_of_ships_for_player1)
        player2 = Player(2, starting_set_of_ships_for_player2)
        game_field = GameField(game_field_width, game_field_hight)
        game_field.update([player1.ships, player2.ships])
        
        out = open('observe.txt', 'a')
        out = open('observe.txt', 'w')
        for i in range(30):
            for j in range(30):
                print(game_field.cells[i][j].type,
                      game_field.cells[i][j].color,
                      game_field.cells[i][j].orientation, end='|', file = out)
            print(end='\n', file = out)
        
        self.renderer.draw_game_field(screen, game_field.cells)
        

if __name__ == "__main__":
    print("This module is not for direct call!")