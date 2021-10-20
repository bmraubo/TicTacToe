from app.ui import UserInterface
from app.tictactoe import TicTacToe

if __name__ == "__main__":
    UserInterface.display_welcome_message()
    size = UserInterface.get_board_size()
    players = UserInterface.get_player_info()
    UserInterface.display_game_instructions(size)
    game = TicTacToe(size, players)
    game.play_game()
    print("Game is closing gracefully")
    exit()
