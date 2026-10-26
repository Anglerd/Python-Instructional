class Student:
    def __init__(self, id, name, school_year, age, gender):
        self.id = id
        self.name = name
        self.school_year = school_year
        self.age = age
        self.gender = gender
        self.expenses = []

    def __str__(self):
        expense_str = "\n".join(str(item) for item in self.expenses)
        if not expense_str:
            expense_str = "No purchase history at this time."
        return f"This is student number {self.id}. Whose name is {self.name}. They are in school year {self.school_year}, and are {self.age} years old. They are a {self.gender}. The following is their expense history\n{expense_str}"


class Expense:
    def __init__(self, id, category, description, cost, date):
        self.id = id
        self.category = category
        self.description = description
        self.cost = cost
        self.date = date

    def __str__(self):
        return f"Purchase number: {self.id}. This is the purchase of a {self.category} that is a {self.description}. Costing {self.cost} at {self.date}"
