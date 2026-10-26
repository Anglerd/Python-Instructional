# This file runs the main application

from readiness import calculate_averages, determine_readiness, identify_weak_area
from reports import print_readiness_report
import database
from students import Student, Expense


def get_input(prompt, type_converter):
    while True:
        try:
            attempt_score = type_converter(input(f"{prompt}\n"))
            return attempt_score
        except ValueError:
            print("Please input a valid value, restarting")


def get_score(prompt):
    while True:
        local_score = get_input(prompt, float)
        if local_score < 0 or local_score > 100:
            print("Please input a valid number between 0 and 100")
        else:
            return local_score


"""
def get_practice_scores(num_amount):
    local_scores = []
    for _ in range(num_amount):
        local_scores.append(get_score(f"Please enter a test score\nCurrent Values = {local_scores}"))
    return local_scores
"""


def build_domain_test_score_dictionary():
    num_keys = get_input("Please enter a number of domains to test", int)
    local_domains = []
    for _ in range(num_keys):
        local_domains.append(input(f"Please enter a domain\nCurrent Domains: {local_domains}\n"))
    local_domain_dictionary = {}
    local_scores = []
    for single_domain in local_domains:
        local_score = get_score(f"Enter score for {single_domain}")
        local_scores.append(local_score)
        local_domain_dictionary[single_domain] = local_score
    return local_domain_dictionary, local_scores


def dissplay_menu():
    print("-----------------------------")
    print("Student Tracker with MySQL History Logger")
    print("-----------------------------")
    print("1. Exit")
    print("2. Save new student")
    print("3. Look up a students grades")
    print("4. Save tests for a student")
    print("5. Look up all students")
    print("6. Save a student purchase")
    print("7. View a student's purchase history")
    print("-----------------------------")


if __name__ == "__main__":
    while True:
        dissplay_menu()
        choice = get_input("", int)
        if choice == 1:
            print("Goodbye")
            exit()
        if choice == 2:
            this_student = input("Please enter the student name\n")
            this_age = get_input(f"Please enter the age of {this_student}", int)
            school_year = get_input(f"Please enter the school year for {this_student}", int)
            gender = input(f"Please enter the gender of {this_student}\n")
            database.save_student(school_year=school_year, age=this_age, name=this_student, gender=gender)
        elif choice in [3, 4, 5, 6, 7]:
            tests, students = database.get_all_from_db()
            for student in students:
                this_student = Student(*student)
                print(this_student)
            if choice != 5:
                student_num = get_input("Please pick a student number from above", int)
                this_student = Student(*students[student_num])
                if choice == 3:
                    for test in tests:
                        if test[1] == student_num + 1:
                            print(f"Test history number {test[0]}, with the following domain scores {test[2]}, has an average of {test[3]}. Meaning they {test[4]}. Weakest domain {test[5]}, with a score of {test[6]}. This was saved in the database at {test[7]}, with the following notes {test[8]}")
                    print("No more test history for this student")
                elif choice == 4:
                    domain_dictionary, scores = build_domain_test_score_dictionary()
                    average_score = calculate_averages(scores)
                    readiness_result = determine_readiness(average_score)
                    weak_domain, weak_score = identify_weak_area(domain_dictionary)
                    print_readiness_report(this_student.name, domain_dictionary, average_score, readiness_result, weak_domain, weak_score)
                    notes = input("Would you like to add any notes to this entry? Leave blank for no notes\n")
                    database.save_test_scores(student_num + 1, domain_dictionary, average_score, readiness_result, weak_domain, weak_score, notes)
                elif choice == 6:
                    amount = round(get_input("Enter the amount the student spen on this purchase", float), 2)
                    category = get_input("What category of purchase was this", str)
                    description = get_input("Describe the purchase the student made", str)
                    database.save_purchase(student_num + 1, description, category, amount)
                elif choice == 7:
                    this_history = database.get_expenses_from_db(student_num + 1)
                    for item in this_history:
                        temp_item = (item[0], *item[2:])
                        this_student.expenses.append(Expense(*temp_item))
                    print(this_student)
                    print("No more purchase history for this student")
        if "y" not in input("Would you like to continue? y/n\n").lower():
            print("Goodbye")
            exit()
