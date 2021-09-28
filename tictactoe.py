class Info:
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)


if __name__ == "__main__":
    Info.welcome_message()
    Info.game_instructions()
