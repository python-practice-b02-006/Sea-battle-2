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
            
    def move_chosen_ship(self, direction, game_field):
        '''
        Moves chosen ship in the needed direction if possible. If not, stops 
        the process.

        Parameters
        ----------
        direction : TYPE string
            DESCRIPTION. Where chosen ship should go.

        Returns
        -------
        None.

        '''
        for i in range(len(self.ships)):
            if self.ships[i].is_chosen:
                if self.ships[i].is_possible_to_move(direction,
                                                     game_field)[0]:
                    self.ships[i].move(direction)
                else:
                    print(self.ships[i].is_possible_to_move(direction,
                                                            game_field)[1])
                
    def ship_is_clicked(self, x, y):
        '''
        Checks if any ship of the player is clicked or not.

        Parameters
        ----------
        x : TYPE int 
            DESCRIPTION. x mouse coordinate
        y : TYPE int
            DESCRIPTION. y mouse coordinate

        Returns
        -------
        bool
            DESCRIPTION. True if any ship of the player is clicked, else 
            False.

        '''
        clicked = False
        for i in range(len(self.ships)):
            if self.ships[i].is_clicked(x, y):
                clicked = True
        return clicked
    
    def make_clicked_ship_chosen(self, x, y):
        '''
        Makes clicked ship chosen.

        Parameters
        ----------
        x : TYPE int 
            DESCRIPTION. x mouse coordinate
        y : TYPE int
            DESCRIPTION. y mouse coordinate

        Returns
        -------
        None.

        '''
        for i in range(len(self.ships)):
            if self.ships[i].is_clicked(x, y):
                self.ships[i].make_chosen()
    
    def there_is_an_appropriate_cannon(self):
        '''
        Checks if there is a cannon that can shoot at the enemy.

        Returns
        -------
        None.

        '''
        pass
    
    def shoot():
        '''
        Makes needed cannon shoot at the enemy.

        Returns
        -------
        None.

        '''
        pass
    
if __name__ == "__main__":
    print("This module is not for direct call!")
