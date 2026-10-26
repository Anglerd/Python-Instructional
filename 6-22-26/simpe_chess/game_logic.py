import board_utils
import db_connector


class game_piece:
    def __init__(self, color: int, type: str):
        self.color = color # 1 = white, -1 = black
        self.type = type # lowercase is white, uppercase is black (when saving/loading from database

    def __str__(self):
        return "piece type is " + self.type + " and color is " + str(self.color)


def rook_move(board, old_spot, new_spot):
    row_dif = new_spot[0] - old_spot[0]
    col_dif = new_spot[1] - old_spot[1]
    if not(row_dif == 0 or col_dif == 0):
        return False
    if row_dif != 0:
        for i in range(0, row_dif, 1 if row_dif > 0 else -1):
            if i == 0:
                continue
            if board[old_spot[0] + i][old_spot[1]]:
                return False
    else:
        for i in range(0, col_dif, 1 if col_dif > 0 else -1):
            if i == 0:
                continue
            if board[old_spot[0]][old_spot[1] + i]:
                return False
    return True


def bishop_move(board, old_spot, new_spot):
    row_dif = new_spot[0] - old_spot[0]
    col_dif = new_spot[1] - old_spot[1]
    if abs(col_dif) != abs(row_dif):
        return False
    for i in range(abs(row_dif)):
        if i == 0:
            continue
        current_row = old_spot[0] + (i * 1 if row_dif > 0 else -1)
        current_column = old_spot[1] + (i * 1 if col_dif > 0 else -1)
        if board[current_row][current_column]:
            return False
    return True


def check_safety(color, spot, board):
    knights = [(2,1), (1,2), (-1,2), (1,-2), (-1,-2), (-2,1), (2,-1), (-2,-1)]
    for knight in knights:
        current_row = spot[0] + knight[0]
        current_column = spot[1] + knight[1]
        if current_column not in range(board_utils.board_size) or current_row not in range(board_utils.board_size):
            continue
        knight_spot = board[current_row][current_column]
        if knight_spot and knight_spot.color != color and knight_spot.type == "knight":
            return False
    rooks = [(0,1), (1,0), (-1,0), (0,-1)]
    for rook in rooks:
        current_row = spot[0] + rook[0]
        current_column =  spot[1] + rook[1]
        if current_column not in range(board_utils.board_size) or current_row not in range(board_utils.board_size):
            continue
        proposed_cell = board[current_row][current_column]
        if proposed_cell and proposed_cell.color != color and proposed_cell.type == "king":
            return False
        while current_row in range(board_utils.board_size) and\
                current_column in range(board_utils.board_size) and not board[current_row][current_column]:
            current_row += rook[0]
            current_column += rook[1]
        if current_column not in range(board_utils.board_size) or current_row not in range(board_utils.board_size):
            continue
        proposed_cell = board[current_row][current_column]
        if proposed_cell and proposed_cell.color != color and\
                (proposed_cell.type == "rook" or proposed_cell.type == "queen"):
            return False
    bishops = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for bishop in bishops:
        current_row = spot[0] + bishop[0]
        current_column = spot[1] + bishop[1]
        if current_column not in range(board_utils.board_size) or current_row not in range(board_utils.board_size):
            continue
        proposed_cell = board[current_row][current_column]
        if proposed_cell and proposed_cell.color != color and\
                (proposed_cell.type == "king" or (proposed_cell.type == "pawn" and current_row - color == spot[0])):
            return False
        while current_row in range(board_utils.board_size) and\
                current_column in range(board_utils.board_size) and not board[current_row][current_column]:
            current_row += bishop[0]
            current_column += bishop[1]
        if current_column not in range(board_utils.board_size) or current_row not in range(board_utils.board_size):
            continue
        proposed_cell = board[current_row][current_column]
        if proposed_cell and proposed_cell.color != color and\
                (proposed_cell.type == "bishop" or proposed_cell.type == "queen"):
            return False
    return True


def check_piece_move(board, old_spot, new_spot, this_piece: game_piece): # [row] [column] as in home/pawn row and such
    proposed_cell = board[new_spot[0]][new_spot[1]]
    if old_spot == new_spot:
        return False
    if new_spot[0] not in range(8) or new_spot[1] not in range(8):
        return False
    if this_piece.type == "pawn":
        if old_spot[0] + this_piece.color != new_spot[0]: # add more conditionals that can allow this pawn to move 2 squares if it has never moved
            #old_spot[0] == this_piece.color or old_spot[0] == board_utils.boaard_size - 1 + this_piece.color
            return False
        if abs(old_spot[1] - new_spot[1]) > 1:
            return False
        if old_spot[1] == new_spot[1] and proposed_cell:
            return False
        if old_spot[1] != new_spot[1] and not proposed_cell:
            return False
    if this_piece.type == "knight":
        row_dif = old_spot[0] - new_spot[0]
        col_dif = old_spot[1] - new_spot[1]
        if row_dif == 0 or col_dif == 0:
            return False
        if abs(row_dif) + abs(col_dif) != 3:
            return False
    if this_piece.type == "rook" and not rook_move(board, old_spot, new_spot):
        return False
    if this_piece.type == "bishop" and not bishop_move(board, old_spot, new_spot):
        return False
    if this_piece.type == "queen":
        if not (bishop_move(board, old_spot, new_spot) or rook_move(board, old_spot, new_spot)):
            return False
    if this_piece.type == "king":
        if abs(new_spot[0] - old_spot[0]) > 1 or abs(new_spot[1] - old_spot[1]) > 1:
            return False
        if not check_safety(this_piece.color, new_spot, board):
            return False
    if proposed_cell and proposed_cell.color == this_piece.color:
        return False
    return True


def update_board(board_data, new_turn_id):
    set_string = "=%s, ".join(f"row{i}" for i in range(1, board_utils.board_size + 1)) + "=%s, turn_id=%s, check_state=%s"
    values = (*board_utils.board_to_strings(board_data["board"]), new_turn_id, board_data["check_state"], board_data["board_id"])
    where_string = "user_boards_id=%s"
    db_connector.update_db("user_boards", set_string, values, where_string)


def check_king_safety(color, board):
    """checks for check of the given color 1 for white, -1 for black"""
    this_king = None
    for num1, row in enumerate(board):
        for num2, cell in enumerate(row):
            if cell and cell.type == "king" and cell.color == color:
                this_king = (num1, num2)
                break
        if this_king:
            break
    if not this_king:
        print(f"An error has occured, there is no king of the given color {color}")
    return check_safety(color, this_king, board)


def move_piece(board_data, old_spot, new_spot):
    this_board = board_data["board"]
    this_piece = this_board[old_spot[0]][old_spot[1]]
    if not this_piece:
        return False
    if (this_piece.color == 1 and board_data["turn_id"] == board_data["white_player"]) or\
            (this_piece.color == -1 and board_data["turn_id"] == board_data["black_player"]):
        if check_piece_move(this_board, old_spot, new_spot, this_piece):
            this_board[old_spot[0]][old_spot[1]] = None
            temp_old = this_board[new_spot[0]][new_spot[1]]
            this_board[new_spot[0]][new_spot[1]] = this_piece
            if not check_king_safety(this_piece.color, this_board):
                this_board[old_spot[0]][old_spot[1]] = this_piece
                this_board[new_spot[0]][new_spot[1]] = temp_old
                return False
            #if piece is pawn and pawn is at last square board
            #this_board[new_spot[0]][new_spot[1]] = this_piece.type = "queen"
            if board_data["check_state"] == "check":
                board_data["check_state"] = None
            if not check_king_safety(this_piece.color * -1, this_board):
                board_data["check_state"] = "check"
            new_turn_id = board_data["white_player"] if this_piece.color == -1 else board_data["black_player"]
            update_board(board_data, new_turn_id)
            return True
    return False


def start_board(white_player, black_player):
    insert_string = "white_user_id, black_user_id, "
    for num in range(1, board_utils.board_size + 1):
        insert_string += "row" + str(num) + ", "
    insert_string += "turn_id"
    nothing = "oooooooo"
    values = (white_player, black_player, "rnbqkbnr", "pppppppp", nothing, nothing, nothing, nothing,
              "PPPPPPPP", "RNBQKBNR", white_player)
    board_id = db_connector.insert_into_db("user_boards", insert_string, values)
    return board_id


def load_board(board_id):
    row = db_connector.get_board_from_db(board_id)
    if not row:
        return None
    board = board_utils.strings_to_board(row[3:11])
    return {
        "board_id": row[0],
        "white_player": row[1],
        "black_player": row[2],
        "board": board,
        "turn_id": row[11],
        "check_state": row[12]
    }
