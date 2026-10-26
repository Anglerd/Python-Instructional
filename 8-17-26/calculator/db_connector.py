#import sys
#sys.path.append(r"E:\Random Stuff\Certification Classes\Python Instructional\6-22-26\narrative_constructor")
#the previous lines were for my implementation, yours is different and will simply use the file in the same folder
from db_config import db_config
import mysql.connector
#pip install mysql-connector-python

DEBUG = False

def insert_into_db(database, insert_string, values):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        #this section has to be updated
        values_substring = ", ".join(["%s"] * len(values))
        sql = f"""
            INSERT INTO {database} ({insert_string})
            VALUES ({values_substring})
            """ # note the use of VALUES (%s...) this is a different way of formmating strings (insert man yelling at clouds meme)
        # we are forced to use this method because of the way mysql.connector works, it does not allow us to use f-strings or .format() for "sEcUrItY" reasons (I know a lazy developer when I see one)
        cursor.execute(sql, values)
        connection.commit()
        print("Saved to MySQL")
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

def save_calculation(calculation, result, num1, num2, num3="", notes=""):
    insert_string = "calculation_performed, result, input_one, input_two"
    if num3:
        insert_string += ", input_three"
    if notes:
        insert_string += ", notes"
    if notes and num3:
        values = (calculation, result, num1, num2, num3, notes)
    elif notes:
        values = (calculation, result, num1, num2, notes)
    elif num3:
        values = (calculation, result, num1, num2, num3)
    else:
        values = (calculation, result, num1, num2)
    if DEBUG:
        print(f"Attempting to save {calculation} with inputs {num1}, {num2}, {num3}, and with the following notes {notes}")
        print(f"constructed the following insert_string {insert_string}")
        print(f"constructed the following values {values}")
    insert_into_db("calc_history", insert_string, values)

def get_all_from_db():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM calc_history")
        raw_all_calcs = cursor.fetchall()
        all_calcs = []
        for calc in raw_all_calcs:
            if DEBUG:
                print(calc)
            all_calcs.append(calc)
    except mysql.connector.Error as error:
        print("Database select failed")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
    return all_calcs

if __name__ == "__main__":
    save_calculation("add", 3, 2, 1)
    save_calculation("add", 3, 2, 1, notes="I added 2 numbers!")
    save_calculation("div", 2.0, 4, 2, num3=1)
    save_calculation("div", 2.0, 4, 2, num3=1, notes="DIVISION!")