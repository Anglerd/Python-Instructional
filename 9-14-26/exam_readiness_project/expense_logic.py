def adding_expenses(expense_table):
    total_spent = 0
    for expense in expense_table:
        total_spent += expense["amount"]
    return total_spent
