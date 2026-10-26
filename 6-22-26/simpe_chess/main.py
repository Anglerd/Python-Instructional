import db_connector


def get_boards(user_id):
    boards = db_connector.get_board_from_db(user_id)
    return boards
