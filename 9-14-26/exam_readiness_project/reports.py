import readiness


def print_readiness_report(student_name, score_dictionary):
    these_scores = score_dictionary.values()
    average = readiness.calculate_average(these_scores)
    readiness_result = readiness.determine_readiness(average)
    weakest_domain, weakest_score = readiness.identify_weak_area(score_dictionary)
    print("----------------------")
    print("Exam Readiness Report")
    print("----------------------")
    print("Student:", student_name)
    print("Practice Exam Scores:", score_dictionary)
    print("Average Score:", average)
    print("Readiness Result:", readiness_result)
    print("Weakest Domain:", weakest_domain)
    print("Weakest Domain Score:", weakest_score)
    print("----------------------")


def print_expense_report_table(expenses):
    if len(expenses) == 0:
        print("No more expenses to report")
        return
    print("-----------------------")
    print("Expense Report")
    print("-----------------------")
    this_expense = expenses[-1]
    print("ID:", this_expense["id"])
    print("Description:", this_expense["description"])
    print("Category:", this_expense["category"])
    print("Amount:", this_expense["amount"])
    print("Created at:", this_expense["created_at"])
    print_expense_report_table(expenses[:-1])
