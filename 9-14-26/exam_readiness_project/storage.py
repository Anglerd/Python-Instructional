# Expense Tracker Storage
# This file handles saving and retrieving expenses from MYSQL

import mysql.connector
from db_config import db_config

DEBUG = False


def start_mysql_connection():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    return connection, cursor


def connect_and_execute(sql, values):
    try:
        connection, cursor = start_mysql_connection()
        cursor.execute(sql, values)
        return connection, cursor
    except mysql.connector.Error as error:
        print("Databse connection failed")
        print("Error:", error)


def insert_into_db(database, insert_string, values):
    try:
        values_substring = ", ".join(["%s"] * len(values))
        sql = """
            INSERT INTO """ + database + " (" + insert_string + """)
            VALUES (""" + values_substring + """)
            """
        connection, cursor = connect_and_execute(sql, values)
        connection.commit()
        print("Saved to MYSQL")
    except mysql.connector.Error as error:
        print("Database save failed")
        print("Error:", error)
    finally:
        if "cursoe" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()


def save_expense(description, category, amount):
    insert_string = "description, category, amount"
    values = (description, category, amount)
    insert_into_db("expenses", insert_string, values)


def save_student(name, list_of_score_dictionary):
    for domain in list_of_score_dictionary:
        insert_string = "domain, score"
        values = (domain, list_of_score_dictionary[domain])
        insert_into_db("scores", insert_string, values)
    all_scores = get_scores()
    added_entries = len(list_of_score_dictionary)
    starting_index = len(all_scores) - added_entries
    insert_string = "domain_grouping"
    group_string = ""
    for num in range(added_entries):
        group_string += str(starting_index + num) + ","
    values = (group_string[:-1],)
    insert_into_db("domain_groups", insert_string, values)
    all_groupings = get_domain_groups()
    most_recent_id = all_groupings[-1]["id"]
    insert_string = "name, domain_groups_id"
    values = (name, most_recent_id)
    insert_into_db("students", insert_string, values)


def get_expense():
    connection, cursor = start_mysql_connection()
    cursor.execute("SELECT * FROM expenses")
    raw_all_expenses = cursor.fetchall()
    all_expenses = []
    for this_expense in raw_all_expenses:
        if DEBUG:
            print(this_expense)
            print(*this_expense)
        this_dictionary = {
            "id": this_expense[0],
            "description": this_expense[1],
            "category": this_expense[2],
            "amount": this_expense[3],
            "created_at": this_expense[4]
        }
        all_expenses.append(this_dictionary)
    return all_expenses


def get_scores():
    connection, cursor = start_mysql_connection()
    cursor.execute("SELECT * FROM scores")
    raw_all_scores = cursor.fetchall()
    all_scores = []
    for this_score in raw_all_scores:
        if DEBUG:
            print(this_score)
            print(*this_score)
        this_dictionary = {
            "id": this_score[0],
            "domain": this_score[1],
            "score": this_score[2]
        }
        all_scores.append(this_dictionary)
    return all_scores


def get_domain_groups():
    connection, cursor = start_mysql_connection()
    cursor.execute("SELECT * FROM domain_groups")
    raw_all_scores = cursor.fetchall()
    all_scores = []
    for this_score in raw_all_scores:
        if DEBUG:
            print(this_score)
            print(*this_score)
        this_dictionary = {
            "id": this_score[0],
            "grouping": this_score[1]
        }
        all_scores.append(this_dictionary)
    return all_scores


def get_students():
    connection, cursor = start_mysql_connection()
    cursor.execute("SELECT * FROM students")
    raw_all_scores = cursor.fetchall()
    all_scores = []
    for this_score in raw_all_scores:
        if DEBUG:
            print(this_score)
            print(*this_score)
        this_dictionary = {
            "id": this_score[0],
            "name": this_score[1],
            "domain_groups_id": this_score[2]
        }
        all_scores.append(this_dictionary)
    return all_scores


if __name__ == "__main__":
    get_expense()
