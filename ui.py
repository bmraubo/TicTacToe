class UserInterface:

    # Display Welcome Message
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    # Display Game Instructions
    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)

    # Get Player Information from User
    def get_player_info():
        # Obtains player names from user
        player_list = []
        while len(player_list) != 2:
            player_name = input(f"Enter Player {len(player_list)+1} Name: ")
            player_type = "human"
            player_list.append([player_name, player_type])
        return player_list
