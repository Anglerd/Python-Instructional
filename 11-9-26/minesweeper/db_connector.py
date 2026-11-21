import sys
sys.path.append(r"C:\SECRETS")
from SOMETHING_CRAZY import db_config
#the previous lines were for my implementation, yours is different and will simply use the file in the same folder
#from db_config import db_config
import mysql.connector
# pip install mysql-connector-python

DEBUG = False

def insert_into_db(database, insert_string, values):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        values_substring = ", ".join(["%s"] * len(values)) # creates a string of "%s, %s, %s..." based on the number of values we are inserting
        sql = """
            INSERT INTO """ + database + " (" + insert_string + """)
            VALUES (""" + values_substring + """)
            """ # note the use of VALUES (%s...) this is a different way of formmating strings (insert man yelling at clouds meme)
        # we are forced to use this method because of the way mysql.connector works, it does not allow us to use f-strings or .format() for "sEcUrItY" reasons (I know a lazy developer when I see one)
        cursor.execute(sql, values)
        connection.commit()
        print("Saved to MySQL")
        return cursor.lastrowid
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def save_board(difficulty, num_row, num_column, cell_list):
    insert_string = "difficulty, num_row, num_column"
    values = (difficulty, num_row, num_column)
    this_id = insert_into_db("minefield", insert_string, values)
    def save_cell(mine_row, mine_column, revealed, flagged, num_bomb, minefield_id):
        insert_string = "mine_row, mine_column, revealed, flagged, num_bomb, minefield_id"
        values = (mine_row, mine_column, revealed, flagged, num_bomb, minefield_id)
        insert_into_db("cell", insert_string, values)
    for row_index in range(num_row):
        for column_index in range(num_column):
            func_dict = {**cell_list[row_index][column_index], "mine_row": row_index, "mine_column": column_index, "minefield_id": this_id}
            save_cell(**func_dict)
    return this_id

def update_cell(mine_row, mine_column, revealed, flagged, minefield_id):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        set_string = f"revealed = {revealed}, flagged = {flagged}"
        where_string = f"minefield_id = {minefield_id} AND mine_row = {mine_row} AND mine_column = {mine_column}"
        sql = """
            UPDATE cell
            SET """ + set_string + """
            WHERE """ + where_string + """
            """ # note the use of VALUES (%s...) this is a different way of formmating strings (insert man yelling at clouds meme)
        # we are forced to use this method because of the way mysql.connector works, it does not allow us to use f-strings or .format() for "sEcUrItY" reasons (I know a lazy developer when I see one)
        cursor.execute(sql)
        connection.commit()
        print("Updated MySQL")
    except mysql.connector.Error as error:
        print("Database update failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def get_all_games_from_db():
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM minefield")
        raw_all_board = cursor.fetchall()
        all_boards = []
        for board in raw_all_board:
            this_board = {
                "minefield_id": board[0],
                "difficulty": board[1],
                "num_row": board[2],
                "num_column": board[3]
                }
            if DEBUG:
                print(this_board)
            all_boards.append(this_board)
        print("Loaded from MySQL")
        return all_boards
    except mysql.connector.Error as error:
        print("Database load failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def get_all_cells_from_game(id, num_row, num_column):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM cell WHERE minefield_id = {id}")
        raw_all_cell = cursor.fetchall()
        # all_cells = [[0] * num_column] * num_row
        all_cells = []
        for local_x in range(num_row):
            all_cells.append([])
            for local_y in range(num_column):
                all_cells[local_x].append([])
        for cell in raw_all_cell:
            if DEBUG:
                print(cell)
            this_row = cell[1]
            this_column = cell[2]
            all_cells[this_row][this_column] = {
                "revealed": bool(cell[3]),
                "flagged": bool(cell[4]),
                "num_bomb": cell[5]
            }
        print("Loaded from MySQL")
        return all_cells
    except mysql.connector.Error as error:
        print("Database load failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def delete_game_from_db(game_id):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM minefield WHERE id = {game_id}")
        connection.commit()
        print("Game deleted from db")
    except mysql.connector.Error as error:
        print("Database load failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    get_all_cells_from_game(8, 6, 8)