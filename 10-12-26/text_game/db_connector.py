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
        print("Saved to MySQL.")
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def save_history(replacements, base_letter):
    #todo add saving logic
    insert_string = "replacements, base_letter"
    values = (replacements, base_letter)
    insert_into_db("ffd", insert_string, values)

def get_all_from_db():
    #todo get all 5 tables (items, people, history, location, connection)
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        raw_all_ffd = cursor.fetchall()
        fat_finger_dictionary = {}
        for this_dict in raw_all_ffd:
            if DEBUG:
                print(this_dict)
            fat_finger_dictionary[this_dict[2]] = list(this_dict[1])
            if DEBUG:
                print(fat_finger_dictionary)
        cursor.execute("SELECT * FROM page_search")
        raw_all_sl = cursor.fetchall()
        search_list = []
        for this_list in raw_all_sl:
            if DEBUG:
                print(this_list)
            search_list.append([this_list[1], this_list[2]])
        print("Successfully loaded from MYSQL")
        return fat_finger_dictionary, search_list
    except mysql.connector.Error as error:
            print("Database load failed.")
            print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    get_all_from_db()