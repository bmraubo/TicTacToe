class UserInterface:

    # Display Welcome Message
    def display_welcome_message():
        print("Welcome to Tic Tac Toe")

    # Display Game Instructions
    def display_game_instructions(size):
        instructions = f"Each square on the board have a value from 1-{size*size}. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)

    def display_message(message):
        print(message)
        return message

    def declare_winner(winner_name):
        if winner_name == "Draw!":
            message = f"It's a {winner_name}"
            print(message)
            return message
        elif winner_name == None:
            pass
        else:
            message = f"{winner_name} has won the game\N{Party Popper}"
            print(message)
            return message

    # Get Player Information from User
    def get_player_info():
        # Obtains player names from user
        custom_marker_list = []
        player_list = []
        while len(player_list) != 2:
            player_name = UserInterface.input_player_name()
            player_type = UserInterface.get_player_type()
            custom_marker = UserInterface.get_custom_marker(custom_marker_list)
            custom_marker_list.append(custom_marker)
            player_list.append([player_name, player_type, custom_marker])
        return player_list

    def input_player_name(player_name=None):
        if player_name == None:
            player_name = input("Enter Player name: ")
            return player_name
        else:
            return player_name

    # Obtaining Player Type (Human/Computer) from User
    def get_player_type():
        valid_player_type = False
        while valid_player_type == False:
            player_type = UserInterface.input_player_type()
            valid_player_type = UserInterface.validate_player_type(player_type)
        return player_type

    def input_player_type(player_type=None):
        if player_type == None:
            player_type = input("Enter player type (human/computer): ")
            return player_type
        else:
            return player_type

    def validate_player_type(player_type):
        valid_player_types = ["human", "computer"]
        if player_type.lower() in valid_player_types:
            return True
        else:
            return False

    # Obtaining custom marker from User
    # Must be unused, a single character, and not be a number
    def get_custom_marker(custom_marker_list):
        valid_custom_marker = False
        while valid_custom_marker == False:
            custom_marker = UserInterface.input_custom_marker()
            valid_custom_marker = UserInterface.validate_custom_marker(
                custom_marker, custom_marker_list
            )
        return custom_marker

    def input_custom_marker(custom_marker=None):
        if custom_marker == None:
            custom_marker = input("Enter custom marker: ")
            return custom_marker
        else:
            return custom_marker

    def validate_custom_marker(custom_marker, custom_marker_list):
        if custom_marker in custom_marker_list:
            error_message = f"{custom_marker} invalid: Custom marker already used"
            UserInterface.display_message(error_message)
            return False
        elif custom_marker in [str(x) for x in list(range(0, 10))]:
            error_message = f"{custom_marker} invalid: Custom marker cannot be a number"
            UserInterface.display_message(error_message)
            return False
        elif len(custom_marker) > 1:
            error_message = f"{custom_marker} invalid: Custom marker cannot take up more than one space"
            UserInterface.display_message(error_message)
            return False
        else:
            return True

    # Get Board Size information from user
    def get_board_size():
        def validate_player_choice(size):
            def validate_unsupported_choice(choice):
                if choice.upper() in ["Y", "N"]:
                    return True
                else:
                    error_message = f"{choice} is not a valid option, please try again."
                    UserInterface.display_message(error_message)
                    return False

            try:
                if int(size) not in [3, 4]:
                    warning_message = f"{size} is not supported - do you wish to continue at own risk?"
                    UserInterface.display_message(warning_message)
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
                error_message = (
                    f"ValueError: {size} is not a valid choice. Please try again."
                )
                UserInterface.display_message(error_message)
                return False

        info_message = "The game is played on an N x N board.\n Currently supported sizes are: 3x3 and 4x4... but you can try higher values. No promises."
        print(info_message)
        valid_player_choice = False
        while valid_player_choice == False:
            player_choice = input("Please enter board size: ")
            valid_player_choice = validate_player_choice(player_choice)
        return int(player_choice)
