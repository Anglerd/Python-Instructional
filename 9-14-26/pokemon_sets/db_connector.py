from db_config import db_config
import mysql.connector
# pip install mysql-connector-python
import card

DEBUG = False

def start_mysql_connection():
    connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
    # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
    # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
    cursor = connection.cursor()
    return connection, cursor

def connect_and_execute(sql, values):
    try:
        connection, cursor = start_mysql_connection()
        cursor.execute(sql, values)
        return connection, cursor
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)

def insert_into_db(database, insert_string, values):
    try:
        values_substring = ", ".join(["%s"] * len(values)) # creates a string of "%s, %s, %s..." based on the number of values we are inserting
        sql = """
            INSERT INTO """ + database + " (" + insert_string + """)
            VALUES (""" + values_substring + """)
            """ # note the use of VALUES (%s...) this is a different way of formmating strings (insert man yelling at clouds meme)
        # we are forced to use this method because of the way mysql.connector works, it does not allow us to use f-strings or .format() for "sEcUrItY" reasons (I know a lazy developer when I see one)
        connection, cursor = connect_and_execute(sql, values)
        cursor.execute(sql, values)
        connection.commit()
        print("Saved to MySQL.")
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def save_card(set_number, name, category, poke_type, rarity):
    insert_string = "set_number, name, category, type, rarity"
    values = (set_number, name, category, poke_type, rarity)
    insert_into_db("card", insert_string, values)

def save_set(name):
    insert_string = "name"
    values = [name]
    insert_into_db("card_set", insert_string, values)

def get_all_from_db():
    """Gets all cards and sets from db and loads them into lists
    returns all_sets, all_cards"""
    try:
        connection, cursor = start_mysql_connection()
        cursor.execute("SELECT * FROM card")
        raw_all_cards = cursor.fetchall()
        all_cards = []
        for this_card in raw_all_cards:
            if DEBUG:
                print(this_card)
                print(*this_card)
            all_cards.append(card.Card(this_card[1], this_card[2], this_card[3], this_card[4], this_card[5]))
        all_sets = []
        cursor.execute("SELECT * FROM card_set")
        raw_all_sets = cursor.fetchall()
        for this_set in raw_all_sets:
            if DEBUG:
                print(this_set)
                print(*this_set)
            all_sets.append(card.Set(this_set[1]))
        return all_sets, all_cards
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def get_enums(database, table, column):
    """Gets enums from the database"""
    try:
        connection, cursor = start_mysql_connection()
        cursor.execute(
            f"""
            SELECT SUBSTRING(COLUMN_TYPE,5)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA='{database}' 
            AND TABLE_NAME='{table}'
            AND COLUMN_NAME='{column}'
            """
        )
        raw_all_enums = cursor.fetchall()
        for this_enum in raw_all_enums:
            if DEBUG:
                print(this_enum)
                print(*this_enum)
            some_list = this_enum[0].split(",")
            for index, this_string in enumerate(some_list):
                some_list[index] = this_string.strip(("()'"))
            # print(some_list)
        return some_list
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    print(get_enums("card_collection", "card", "category"))
    print(get_enums("card_collection", "card", "type"))
    print(get_enums("card_collection", "card", "rarity"))