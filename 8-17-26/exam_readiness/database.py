import sys
sys.path.append(r"E:\Random Stuff\Certification Classes\Python Instructional\6-22-26\narrative_constructor")
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
        if DEBUG:
            print(sql)
            byte_message = bytes(sql, 'utf-8')
            print(byte_message)
            print(values)
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


def save_student(school_year, age, name="", gender=""):
    insert_string = "school_year, age, gender, name"
    values = (school_year, age, gender, name)
    insert_into_db("student", insert_string, values)


def save_test_scores(student_id, domain_scores, average_score, readiness_result, weakest_domain, weakest_score, notes=""):
    insert_string = "student_id, domain_scores, average_score, readiness_result, weakest_domain, weakest_score, notes"
    domain_string = ""
    for key in domain_scores:
        domain_string += f"{key} {domain_scores[key]},"
    domain_string = domain_string[:-1]
    values = (student_id, domain_string, average_score, readiness_result, weakest_domain, weakest_score, notes)
    insert_into_db("grade_history", insert_string, values)


def save_purchase(student_id, description, category, amount):
    insert_string = "student_id, description, category, amount"
    values = (student_id, description, category, amount)
    insert_into_db("expenses", insert_string, values)


def get_all_from_db():
    all_grades = []
    all_students = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM grade_history")
        raw_all_grades = cursor.fetchall()
        for grade in raw_all_grades:
            current_grade = []
            for value in grade:
                current_grade.append(value)
            current_grade[2] = current_grade[2].split(",")
            domain_dict = {}
            for domain in current_grade[2]:
                current_domain, this_grade = domain.split(" ")
                domain_dict[current_domain] = this_grade
            current_grade[2] = domain_dict
            if DEBUG:
                print(grade)
            all_grades.append(current_grade)
        cursor.execute("SELECT * FROM student")
        raw_all_students = cursor.fetchall()
        for student in raw_all_students:
            if DEBUG:
                print(student)
            all_students.append(student)
    except mysql.connector.Error as error:
        print("Database select failed")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
    return all_grades, all_students


def get_expenses_from_db(student_id):
    all_expenses = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM expenses WHERE student_id = {student_id}")
        raw_all_expenses = cursor.fetchall()
        for expense in raw_all_expenses:
            if DEBUG:
                print(expense)
            all_expenses.append(expense)
    except mysql.connector.Error as error:
        print("Database select failed")
        print("Error:", error)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
    return all_expenses


if __name__ == "__main__":
    save_student(name='Tomas', age=2, school_year=16, gender='M')
    test_dict = {
        "Python": 90,
        "Java": 85,
        "Syntax": 80
    }
    save_test_scores(1, test_dict, 80, 'Needs More Practice', 'Syntax', 80)
    grades,students = get_all_from_db()
    print(grades)
    print(students)
