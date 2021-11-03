from app.ui import UserInterface
from app.tictactoe import TicTacToe
from app.parser import Parser

if __name__ == "__main__":
    parser = Parser.create_parser()
    args = parser.parse_args()
    UserInterface.display_welcome_message()
    size = UserInterface.get_board_size()
    players = UserInterface.get_player_info()
    UserInterface.display_game_instructions(size)
    game = TicTacToe(size, players, server=args.server)
    game.play_game()
    game_close_message = "Game is closing gracefully"
    UserInterface.display_message(game_close_message)
    exit()
