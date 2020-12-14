from menu import Menu
import pygame 
from renderer import Renderer
from globaldata import (starting_set_of_ships_for_player0,
                        starting_set_of_ships_for_player1,
                        game_field_width, game_field_hight, FPS)
from player import Player
from gamefield import GameField
clock = pygame.time.Clock()


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
        player = [Player(starting_set_of_ships_for_player0),
                   Player(starting_set_of_ships_for_player1)]
        game_field = GameField(game_field_width, game_field_hight)
        game_field.update([player[0].ships, player[1].ships])
        self.renderer.draw_game_field(screen, game_field.cells)
        finished = False
        number_of_active_player = 0
        while not finished:
            
            out = open('observe.txt', 'a')
            out = open('observe.txt', 'w')
            for i in range(30):
                for j in range(30):
                    print(game_field.cells[i][j].type,
                          game_field.cells[i][j].color,
                          game_field.cells[i][j].orientation, end='|', file = out)
                print(end='\n', file = out)
            
            number_of_active_player += 1
            number_of_active_player %= 2
            player[number_of_active_player].update_ships_movement_points()
            turn_passed = False
            while not turn_passed:
                clock.tick(FPS)
                turn_passed, finished = self.handle_events(pygame.event.get())
                
    def handle_events(self, events):
        '''
        Handles events

        Parameters
        ----------
        events : TYPE pygame event
            DESCRIPTION. Events got from pygame.event.get()

        Returns
        -------
        bool
            DESCRIPTION. turn_passed
        bool
            DESCRIPTION. finished

        '''
        turn_passed, finished = False, False
        for event in events:
            if event.type == pygame.QUIT:
                turn_passed, finished = True, True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    turn_passed = True
                    print("next_turn")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1): pass
        return turn_passed, finished
                        
        
if __name__ == "__main__":
    print("This module is not for direct call!")