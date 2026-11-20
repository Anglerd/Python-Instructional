import minefield
import db_connector

def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Invalid input, please enter something of the type {type_converter}")

def validate_input(prompt, validation_list, type_converter: Type = str):
    while True:
        proposed_value = get_input(prompt, type_converter)
        if proposed_value in validation_list:
            return proposed_value
        print(f"Invalid input, please enter a value from the following list: {validation_list}")

def do_reveal(game_board, row, column, num_rows, num_columns, board_id):
    game_board[row][column]["revealed"] = True
    db_connector.update_cell(row, column, game_board[row][column]["revealed"], game_board[row][column]["flagged"], board_id)
    if game_board[row][column].get("num_bomb", 0) == 0:
        for local_row in range(max(row - 1, 0), min(row + 2, num_rows)):
            for local_column in range(max(column - 1, 0), min(column + 2, num_columns)):
                if not game_board[local_row][local_column].get("revealed", False):
                    do_reveal(game_board, local_row, local_column, num_rows, num_columns, board_id)

def printboard(game_board, num_rows, num_columns):
    for r in range(num_rows):
        for c in range(num_columns):
            print_string = game_board[r][c].get("num_bomb", 0) if game_board[r][c].get("revealed", False) else " "
            print(print_string, end=",")
        print()

if __name__ == "__main__":
    game_board = None
    if "y" in get_input("Would you like to load a game from the database? y/n", str).lower():
        # TODO loading (or saving?) is broken why?
        possible_boards = db_connector.get_all_games_from_db()
        for index, this_game in enumerate(possible_boards):
            print(f"Choose {index} for\n{this_game}")
        chosen_game = validate_input("Choose a game from above", range(len(possible_boards)), int)
        difficulty = possible_boards[chosen_game]["difficulty"]
        num_rows = possible_boards[chosen_game]["num_row"]
        num_columns = possible_boards[chosen_game]["num_column"]
        this_id = possible_boards[chosen_game]["minefield_id"]
        game_board = db_connector.get_all_cells_from_game(this_id, num_rows, num_columns)
    else:
        num_difficulty = validate_input("Choose a difficulty\n1. Easy\n2. Medium\n3. Hard\n4. Very Hard\n5. Impossible", range(1, 6), int)
        if num_difficulty == 1:
            difficulty = "Easy"
            num_rows = 5
            num_columns = 5
            number_of_bombs = 4
        elif num_difficulty == 2:
            difficulty = "Medium"
            num_rows = 6
            num_columns = 6
            number_of_bombs = 8
        elif num_difficulty == 3:
            difficulty = "Hard"
            num_rows = 6
            num_columns = 8
            number_of_bombs = 11
        elif num_difficulty == 4:
            difficulty = "Very Hard"
            num_rows = 7
            num_columns = 10
            number_of_bombs = 21
        elif num_difficulty == 5:
            difficulty = "Impossible"
            num_rows = 8
            num_columns = 12
            number_of_bombs = 44
    game_state = True
    while game_state:
        if not game_board:
            temp_board = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
            for temp_row in temp_board:
                print(temp_row)
        else:
            printboard(game_board, num_rows, num_columns)
        chosen_column = validate_input("Which column (x) are you choosing?", range(num_columns), int)
        chosen_row = validate_input("Which row (y) are you choosing?", range(num_rows), int)
        # TODO flag maybe?
        if not game_board:
            while True:
                game_board = minefield.make_field(num_rows, num_columns, number_of_bombs)
                if game_board[chosen_row][chosen_column].get("num_bomb", 0) == 0:
                    for local_x in range(num_rows):
                        for local_y in range(num_columns):
                            game_board[local_x][local_y]["revealed"] = False
                            game_board[local_x][local_y]["flagged"] = False
                            if game_board[local_x][local_y].get("num_bomb", 0) == 0:
                                game_board[local_x][local_y]["num_bomb"] = 0
                    board_id = db_connector.save_board(difficulty, num_rows, num_columns, game_board)
                    break
        do_reveal(game_board, chosen_row, chosen_column, num_rows, num_columns, board_id)
        if game_board[chosen_row][chosen_column].get("num_bomb", 0) == 9:
            game_state = False
            win_state = False
        else:
            num_check = True
            for local_x in range(num_rows):
                for local_y in range(num_columns):
                    if game_board[local_x][local_y].get("num_bomb", 0) != 9 and not game_board[local_x][local_y].get("revealed", False):
                        num_check = False
            if num_check:
                game_state = False
                win_state = True
    # game loop ends here
    if not win_state:
        printboard(game_board, num_rows, num_columns)
        print("You stole fizzy lifting drinks! You bumped into the ceiling which now has to be washed and sterilized, so you get nothing! You lose! Good day, sir!")
    else:
        print("Winner winner chicken dinner")
    # TODO delete board from DB