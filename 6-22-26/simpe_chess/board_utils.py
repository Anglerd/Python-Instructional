import game_logic

board_size = 8

CHAR_TO_PIECE = {
    "r": (1, "rook"),   "R": (-1, "rook"),
    "n": (1, "knight"), "N": (-1, "knight"),
    "b": (1, "bishop"), "B": (-1, "bishop"),
    "q": (1, "queen"),  "Q": (-1, "queen"),
    "k": (1, "king"),   "K": (-1, "king"),
    "p": (1, "pawn"),   "P": (-1, "pawn")
}


PIECE_TO_CHAR = {v: k for k, v in CHAR_TO_PIECE.items()}


def strings_to_board(row_strings):
    board = []
    for row_str in row_strings:
        board_row = []
        for char in row_str:
            if char == "o":
                board_row.append(None)
            else:
                color, this_piece = CHAR_TO_PIECE[char]
                board_row.append(game_logic.game_piece(color, this_piece))
        board.append(board_row)
    return board


def board_to_strings(board):
    """This takes a board in memory and returns a single array containing the rows for the database"""
    rows = []
    for row in board:
        row_chars = []
        for cell in row:
            if not cell:
                row_chars.append("o")
            else:
                char = PIECE_TO_CHAR[(cell.color, cell.type)]
                row_chars.append(char)
        rows.append("".join(row_chars))
    return rows


if __name__ == "__main__":
    nothing = "oooooooo"
    board = strings_to_board(["rnbqkbnr", "pppppppp", nothing, nothing, nothing, nothing,
                             nothing, nothing, "PPPPPPPP", "RNBQKBNR"])
    strings = board_to_strings(board)
    for string in strings:
        print(string)
