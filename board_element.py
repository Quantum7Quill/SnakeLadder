class BoardElement:
    def __init__(self, start, end):
        self.start_position = start
        self.end_position = end
    
    def get_final_position(self):
        return self.end_position