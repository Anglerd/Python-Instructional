import readiness
import reports
import constants
import storage
import expense_logic


def get_input(prompt, type_converter):
    """Prompts the user for some input and validates that the input is of the expected type"""
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a valid input of the type {type_converter}")


def view_menu():
    print("--------------------------------------")
    print("Exam Readiness Calculator and database")
    print("--------------------------------------")
    print("1. Exit")
    print("2.. Calculate an average")
    print("3. Determine Exam Readiness")
    print("4. Save Exam Readiness Report for a student")
    print("5. Save an expense to the database")
    print("6. Print all expenses in the database")
    print("7. Show total amount spent in the expense report")
    print("8. Print expenses by category")
    print("9. Print total amount spent on a category")
    print("10. Get Exam Readiness Report for a student")


def get_categories(get_categories_expense_table):
    output = []
    for this_expense in get_categories_expense_table:
        if this_expense["category"].lower() not in output:
            output.append(this_expense["category"].lower())
    return output


if __name__ == "__main__":
    while True:
        view_menu()
        menu_option = get_input("", int)
        if menu_option == 1:
            print("Goodbye")
            break
        elif menu_option == 2:
            these_scores = []
            while True:
                proposed_number = get_input(f"Enter a number between {constants.minimum_score} and {constants.maximum_score}, else input a number outside the range to finish", float)
                if constants.minimum_score <= proposed_number <= constants.maximum_score:
                    these_scores.append(proposed_number)
                elif "y" not in input("You input a non-valid number, would you like to continue adding numbers to this average? y/n").lower():
                    break
            print(readiness.calculate_average(these_scores))
        elif menu_option == 3:
            print(readiness.determine_readiness(get_input("Enter the average score to determine the readiness of", float)))
        elif menu_option == 4:
            student_name = input("What is the student name?")
            score_dictionary = {}
            while True:
                proposed_number = get_input(f"Enter a number between {constants.minimum_score} and {constants.maximum_score}, else input a number outside the range to finish", float)
                if constants.minimum_score <= proposed_number <= constants.maximum_score:
                    this_domain = input(f"Enter the domain name for this score {proposed_number}")
                    score_dictionary[this_domain] = proposed_number
                elif "y" not in input(f"You input a non-valid number, would you like to continue adding domains and scores to generate the report for {student_name}? y/n").lower():
                    break
            reports.print_readiness_report(student_name, score_dictionary)
            storage.save_student(student_name, score_dictionary)
        elif menu_option == 5:
            category = input("What category is this expense?")
            description = input("Describe the expense")
            amount = get_input("How much was this expense in money", float)
            storage.save_expense(description, category, amount)
        elif menu_option == 6:
            reports.print_expense_report_table(storage.get_expense())
        elif menu_option == 7:
            expense_table = storage.get_expense()
            total_spent = expense_logic.adding_expenses(expense_table)
            print(total_spent)
        elif menu_option in [8, 9]:
            expense_table = storage.get_expense()
            categories = get_categories(expense_table)
            while True:
                user_input = input(f"Choose a category from the following {categories}").lower()
                if user_input not in categories:
                    print("That was not a valid option, please choose from the list shown")
                else:
                    break
            sub_expense_table = []
            for expense in expense_table:
                if expense["category"].lower() == user_input:
                    sub_expense_table.append(expense)
            if menu_option == 8:
                reports.print_expense_report_table(sub_expense_table)
            elif menu_option == 9:
                category_total_spent = expense_logic.adding_expenses(sub_expense_table)
                print(category_total_spent)
        elif menu_option == 10:
            all_students = storage.get_students()
            while True:
                for this_student in all_students:
                    print(f"The student with id {this_student['id']} is called {this_student['name']}")
                proposed_student = get_input("Choose a student id from above", int)
                if proposed_student > len(all_students):
                    print("Invalid option, please choose from above")
                else:
                    break
            all_groupings = storage.get_domain_groups()
            all_scores = storage.get_scores()
            chosen_student = all_students[proposed_student - 1]
            this_grouping = all_groupings[chosen_student["domain_groups_id"] - 1]["grouping"].split(",")
            starting_index = int(this_grouping[0]) - 1
            sub_grouping = all_scores[starting_index:starting_index + len(this_grouping)]
            score_dictionary = {}
            for score in sub_grouping:
                score_dictionary[score["domain"]] = score["score"]
            reports.print_readiness_report(chosen_student["name"], score_dictionary)
        if "y" not in input("Would you like to continue back to the menu? y/n").lower():
            print("Goodbye")
            break
