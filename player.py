class Player:
    def __init__(self, name):
        self.name = name
        self.current_position = 0
        
    def roll_dice(self, dice):
        return dice.roll()
    
    def get_current_position(self):
        return self.current_position
    
    def set_current_position(self, position):
        self.current_position = position