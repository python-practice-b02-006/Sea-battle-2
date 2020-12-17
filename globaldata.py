if __name__ == "__main__":
    print("This module is not for direct call!")
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
    LIGHTBLUE = (204, 229, 255)
    GREY = (156, 161, 181)
    BROWN = (140, 114, 89)
    DARKBROWN = (135, 75, 15)

c = Colors()

'''--------------------------Buttons---------------------------------------'''

rect_of_starting_button = [1, 1, 100, 100] #pygame rules of rectangle

'''--------------------------Game field------------------------------------'''

game_field_width = 30 #The width of game field (along x axis) 
                        #(an amount of cells)
game_field_hight = 30 #The hight of game field (along y axis) 
                        #(an amount of cells)
pixels_per_cell = min(screen_width // game_field_width, screen_hight //
                game_field_hight) # An amount of pixels in the side of one 
                                                              #cell.(int type)

left_indent = (screen_width - game_field_width * pixels_per_cell) / 2  
top_indent = (screen_hight - game_field_hight * pixels_per_cell) / 2 
'''-------------------------Starting-set-----------------------------------'''

from battleship import BattleShip

color_of_player = [c.GREEN, c.RED]
color_name_of_player = ["Зелёный", "Красный"]
battleship1 = BattleShip(color_of_player[0], x = 5, y = 20, is_chosen = True,
                         orientation = "up")
battleship2 = BattleShip(color_of_player[0], x = 15, y = 20, 
                         orientation = "up")
battleship3 = BattleShip(color_of_player[0], x = 25, y = 20,
                         orientation = "up")
starting_set_of_ships_for_player0 = [battleship1, battleship2, battleship3]

battleship4 = BattleShip(color_of_player[1], x = 5, y = 10,
                         orientation = "down")
battleship5 = BattleShip(color_of_player[1], x = 15, y = 10,
                         orientation = "down")
battleship6 = BattleShip(color_of_player[1], x = 25, y = 10,
                         orientation = "down")
starting_set_of_ships_for_player1 = [battleship4, battleship5, battleship6]

'''------------------------------------------------------------------------'''

