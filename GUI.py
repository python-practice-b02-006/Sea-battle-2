class Button():
    '''
    Stores a functional of the button.
    '''
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def is_clicked(self, x_mouse_coord, y_mouse_coord):
        '''
        Checks if the button is clicked or not.

        Parameters
        ----------
        x_mouse_coord : TYPE int
            DESCRIPTION. x coordinate of mouse cursor.
        y_mouse_coord : TYPE int
            DESCRIPTION. y coordinate of mouse cursor.

        Returns
        -------
        bool
            DESCRIPTION. Returns True if starting button is clicked, else 
            returns False.

        '''
        if ((x_mouse_coord >= self.location[0]) and 
            (x_mouse_coord <= self.location[0] + self.location[2]) and 
            (y_mouse_coord >= self.location[1]) and 
            (y_mouse_coord <= self.location[1] + self.location[3])):
            return True
        else:
            return False
    
if __name__ == "__main__":
    print("This module is not for direct call!")