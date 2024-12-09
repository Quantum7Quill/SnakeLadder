from collections import defaultdict
from snake import Snake
from ladder import Ladder
from player import Player

class Board:
    def __init__(self, start_position, end_position):
        self.start_position = start_position
        self.end_position = end_position
        self.board_elements = {}
        self.current_players = {}
        
    def add_ladder(self, start, end):
        ladder = Ladder(start, end)
        self.board_elements[start] = ladder
        
    def add_snake(self, start, end):
        snake = Snake(start, end)
        self.board_elements[start] = snake
        
    def add_player(self, name):
        player_count = len(self.current_players.keys())
        player_id  = player_count + 1
        self.current_players[player_id] = Player(name, player_id)
        
        
    
        
    