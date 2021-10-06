class UserInterface:

    # Display Welcome Message
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    # Display Game Instructions
    def game_instructions(size):
        instructions = f"Each square on the board have a value from 1-{size*size}. Select which square you would like to play by inputting the correct value when promoted."
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

    # Get Board Size information from user
    def get_board_size():
        def validate_player_choice(size):
            def validate_unsupported_choice(choice):
                if choice.upper() in ["Y", "N"]:
                    return True
                else:
                    print(f"{choice} is not a valid option, please try again.")
                    return False

            try:
                if int(size) not in [3, 4]:
                    print(
                        f"{size} is not supported - do you wish to continue at own risk?"
                    )
                    valid_choice = False
                    while valid_choice == False:
                        choice = input("Y/N: ")
                        valid_choice = validate_unsupported_choice(choice)
                    if choice.upper() == "Y":
                        return True
                    elif choice.upper() == "N":
                        return False
                else:
                    return True
            except ValueError:
                print(f"ValueError: {size} is not a valid choice. Please try again.")

        info_message = "The game is played on an N x N board.\n Currently supported sizes are: 3x3 and 4x4... but you can try higher values. No promises."
        print(info_message)
        valid_player_choice = False
        while valid_player_choice == False:
            player_choice = input("Please enter board size: ")
            valid_player_choice = validate_player_choice(player_choice)
        return int(player_choice)
