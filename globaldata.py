'''---------------------------Global---------------------------------------'''
FPS = 10

screen_width = 1000
screen_hight = 800

'''--------------------------Buttons---------------------------------------'''

rect_of_starting_button = [0, 0, 100, 100] #pygame rules of rectangle

'''--------------------------Game field------------------------------------'''

game_field_width = 30 #The width of game field (along x axis) 
                        #(an amount of squares)
game_field_hight = 30 #The hight of game field (along y axis) 
                        #(an amount of squares)
game_field = []
for i in range(game_field_hight):
    game_field.append([])
    for j in range(game_field_width):
        game_field[i].append(None)
        
'''---------------------------Colours--------------------------------------'''

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


if __name__ == "__main__":
    print("This module is not for direct call!")