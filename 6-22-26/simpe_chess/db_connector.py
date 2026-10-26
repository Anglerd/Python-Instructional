import sys
import subprocess


def install_package(package_name):
    """Install a package, automatically repairing pip if it's broken."""
    # First attempt
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package_name],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        # Check for the specific broken pip error
        if "ImpImporter" in result.stderr or "pkgutil" in result.stderr:
            print("pip is broken (ImpImporter error). Repairing pip...")
            # --default-pip forces a fresh install from the bundled version
            subprocess.run(
                [sys.executable, "-m", "ensurepip", "--upgrade", "--default-pip"],
                check=True
            )
            # Retry the installation
            subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name],
                check=True
            )
        else:
            # Some other error – print and raise
            print("pip install failed:")
            print(result.stderr)
            result.check_returncode()  # raises CalledProcessError
    else:
        print(f"Successfully installed {package_name}")

# ---------- Check for mysql.connector, install if missing ----------
try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python not found. Installing...")
    install_package("mysql-connector-python")
    import mysql.connector   # Now it should be available

"""
All of the above was for my personal implementation, due to an error in the linking of my main python and the python being used by pycharm
"""

from db_config_DO_NOT_OPEN import db_config


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
        last_id = cursor.lastrowid
        print("Saved to MySQL.")
        return last_id
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
        raise
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()


# TODO check if update uses same logic as insert on MYSQL connector (with VALUES and such)
def update_db(database, set_string, values, where_string):
    try:
        connection = mysql.connector.connect(**db_config) # ** "unrolls" the dictionary for us and sends in the key/value pairs to the function
        # for example "host": "localhost" becomes host="localhost" so this translates to mysql.connector.connect(host="localhost")
        # "unrolling" is used extensively in networking code as we "save" the connection settings and reuse them often in networking
        cursor = connection.cursor()
        sql = """UPDATE """ + database + " SET " + set_string + """ WHERE """ + where_string
        cursor.execute(sql, values)
        connection.commit()
        print("Updated MySQL.")
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()


def get_board_from_db(board_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql_query = "SELECT * FROM user_boards WHERE user_boards_id = %s"
        cursor.execute(sql_query, (board_id,))
        data = cursor.fetchone()
        return data
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()


def get_users_boards_from_db(user_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql_query = "SELECT user_boards_id FROM user_boards WHERE white_user_id = %s OR black_user_id = %s"
        cursor.execute(sql_query, (user_id, user_id))
        data = cursor.fetchone()
        return data
    except mysql.connector.Error as error:
        print("Database save failed.")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
