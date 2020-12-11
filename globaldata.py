'''---------------------------Global---------------------------------------'''
FPS = 10

screen_width = 1000
screen_hight = 800
  
'''---------------------------Colors--------------------------------------'''

class Colors():
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)


c = Colors()

'''--------------------------Buttons---------------------------------------'''

rect_of_starting_button = [0, 0, 100, 100] #pygame rules of rectangle

'''--------------------------Game field------------------------------------'''

game_field_width = 30 #The width of game field (along x axis) 
                        #(an amount of cells)
game_field_hight = 30 #The hight of game field (along y axis) 
                        #(an amount of cells)

'''-------------------------Starting-set-----------------------------------'''

from battleship import BattleShip

battleship1 = BattleShip(color = c.GREEN, x = 5, y = 20, orientation = "up", 
                         toughness = 12, movement_points = 8)
battleship2 = BattleShip(color = c.GREEN, x = 15, y = 20, orientation = "up", 
                         toughness = 12, movement_points = 8)
battleship3 = BattleShip(color = c.GREEN, x = 25, y = 20, orientation = "up", 
                         toughness = 12, movement_points = 8)
starting_set_of_ships_for_player1 = [battleship1, battleship2, battleship3]

battleship4 = BattleShip(color = c.RED, x = 5, y = 10, orientation = "down", 
                         toughness = 12, movement_points = 8)
battleship5 = BattleShip(color = c.RED, x = 15, y = 10, orientation = "down", 
                         toughness = 12, movement_points = 8)
battleship6 = BattleShip(color = c.RED, x = 25, y = 10, orientation = "down", 
                         toughness = 12, movement_points = 8)
starting_set_of_ships_for_player2 = [battleship4, battleship5, battleship6]


'''------------------------------------------------------------------------'''

if __name__ == "__main__":
    print("This module is not for direct call!")