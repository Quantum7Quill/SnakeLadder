from board import Board
from dice import Dice
dice = Dice(
    minimum_value=1,
    maximum_value=6
)
class Game:
    def __init__(self):
        self.board = Board(1, 100)
        
    def setup_board(self):
        number_of_snakes = int(input("Enter number of snakes"))
        for _ in range(number_of_snakes):
            start, end = [int(position) for position in input("Enter start and end of snakes").split()]
            self.board.add_snake(start, end)
        number_of_ladders = int(input("Enter number of ladder"))
        for _ in range(number_of_ladders):
            start, end = [int(position) for position in input("Enter start and end of ladder").split()]
            self.board.add_ladder(start, end)
        number_of_players = int(input("Enter number of players"))
        for _ in range(number_of_players):
            player_name = input("Enter Player Name")
            self.board.add_player(player_name)
            
    def check_for_board_elements(self, position):
        element = self.board.board_elements.get(position, None)
        if not element:
            return position
        
        return self.check_for_board_elements(element.get_final_position())
        
            
    def play(self):
        total_number_of_players_left_on_board = len(self.board.current_players.keys())
        winner = []
        while total_number_of_players_left_on_board > 1:
            number_of_players = len(self.board.current_players.keys())
            for player_id in range(1, number_of_players + 1):
                if player_id in winner:
                    continue
                current_player = self.board.current_players[player_id]
                position_of_player = current_player.get_current_position()
                outcome = current_player.roll_dice(dice)
                new_position_of_player = self.check_for_board_elements(
                    (position_of_player + outcome)
                ) if (position_of_player + outcome <= 100) else position_of_player 
                
                current_player.set_current_position(new_position_of_player)
                
                print(
                    f'{current_player.name} rolled a {outcome} and moved from \
                        {position_of_player} to {new_position_of_player}'
                )
                
                if new_position_of_player == 100:
                    winner.append(current_player.id)
                    total_number_of_players_left_on_board-=1
                    print(f'{current_player.name} comes at position {len(winner)} in leaderboard')
                    
                if total_number_of_players_left_on_board == 1:
                    print("Game Over")
                    break
        
if __name__ == "__main__":
    game = Game()
    game.setup_board()
    game.play()
                
        