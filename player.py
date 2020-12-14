class Player():
    '''
    Stores a list of player's ships. Updates this list.
    '''
    def __init__(self, color, color_name, ships):
        self.color = color
        self.color_name = color_name
        self.ships = ships
        
    def update_ships_movement_points(self):
        '''
        Updates movement points of player's ships.

        Returns
        -------
        None.

        '''
        for i in range(len(self.ships)):
            self.ships[i].update_movement_points()
            
    def activate_cells_of_ships(self):
        '''
        Makes cannons of all ships active.

        Returns
        -------
        None.

        '''
        for i in range(len(self.ships)):
            self.ships[i].activate_cannons()
            
    def make_ships_not_chosen(self):
        '''
        Makes ships of the player not highlighted.

        Returns
        -------
        None.

        '''
        for i in range(len(self.ships)):
            self.ships[i].make_not_chosen() 
        
if __name__ == "__main__":
    print("This module is not for direct call!")