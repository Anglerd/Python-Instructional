from db_config_DO_NOT_SHOW_THIS_ONE import db_config
import constructor
import mysql.connector
# pip install mysql-connector-python

DEBUG = True

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
        print("Saved to MySQL.")
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def save_character(name, alignment, weapon, level):
    insert_string = "name, alignment, weapon, level"
    values = (name, alignment, weapon, level)
    insert_into_db("pc", insert_string, values)

def save_action(pc_name, action, result):
    insert_string = "pc_name, action_type, result"
    values = (pc_name, action, result)
    insert_into_db("action", insert_string, values)

def save_adjective(adjective, alignment):
    insert_string = "adjective, alignment"
    values = (adjective, alignment)
    insert_into_db("adjectives", insert_string, values)

def get_all_from_db():
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pc")
        raw_all_characters = cursor.fetchall()
        all_characters = []
        for character in raw_all_characters:
            if DEBUG:
                print(character)
                print(*character)
            all_characters.append(constructor.Player(character[0], character[1], character[2], character[3])) # this is written this way to allow for "multi-word" names and weapons, for example "The Sword of Destiny" would be stored as a single string in the database and would be split into multiple strings if we used *character instead of character[0], character[1], etc.
        cursor.execute("SELECT * FROM action")
        raw_all_actions = cursor.fetchall()
        all_actions = []
        for action in raw_all_actions:
            if DEBUG:
                print(action)
            action = list(action)
            action[1] = next((player for player in all_characters if player.name == action[1]), None) # find the player object that matches the name in the action tuple
            all_actions.append(constructor.Action(action[2], action[1], action[3])) # this is ordered in this way because the action table is ordered as (id, pc_name, action_type, result) and the Action constructor is ordered as (action_type, this_player, action_result)
            # we can be more explicit by using constructor.Action(action_type=action[2], this_player=action[1], action_result=action[3])
        cursor.execute("SELECT * FROM adjectives")
        raw_all_adjectives = cursor.fetchall()
        all_adjectives = [[], [], [], [], [], [], [], [], []] # create a list of lists for each alignment
        for adjective in raw_all_adjectives:
            all_adjectives[adjective[2]].append(adjective[1])
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
    return all_characters, all_actions, all_adjectives