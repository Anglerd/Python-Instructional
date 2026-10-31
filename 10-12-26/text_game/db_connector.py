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

sys.path.append(r"C:\SECRETS")
from SOMETHING_CRAZY import db_config
#the previous lines were for my implementation, yours is different and will simply use the file in the same folder
#from db_config import db_config
import entity
import room
#import mysql.connector # this is commented out because of the craziness above
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

def save_history(action: str, health_delta: float):
    if len(action) > 50:
        print("Action string is too long for the current database implementation. To increase it... will require a few steps")
        quit()
    insert_string = "action, health_delta"
    values = (action, health_delta)
    insert_into_db("history", insert_string, values)

def get_all_from_db():
    #todo get all 5 tables (items, people, history, location, connection)
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM item")
        raw_all_item = cursor.fetchall()
        item_list = []
        for this_item in raw_all_item:
            if DEBUG:
                print(this_item)
            item_list.append(entity.Item(this_item[1], [
                        ("health", this_item[2]),
                        ("attack", this_item[3]),
                        ("max_health", this_item[4])
                    ]
                )
            )
            if DEBUG:
                print(item_list)
        cursor.execute("SELECT * FROM people")
        raw_all_people = cursor.fetchall()
        people_list = []
        for this_people in raw_all_people:
            if DEBUG:
                print(this_people)
            people_list.append(entity.NPC(
                this_people[1],
                this_people[3],
                this_people[4],
                this_people[2],
                this_people[2],
                this_people[5]
            ))
        cursor.execute("SELECT * FROM location")
        raw_all_location = cursor.fetchall()
        location_dict = {}
        for this_location in raw_all_location:
            if DEBUG:
                print(this_location)
            location_dict[this_location[1]] = room.Room(
                this_location[8],
                people_list[this_location[2] - 1] if this_location[2] else None,
                item_list[this_location[3] - 1] if this_location[3] else None,
                this_location[4],
                this_location[5],
                this_location[6] if this_location[6] else False,
            )
            for this_connection in this_location[7].split(","):
                location_dict[this_location[1]].add_connection(this_connection)
            if DEBUG:
                print(location_dict)
        print("Successfully loaded from MYSQL")
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