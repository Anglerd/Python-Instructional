import day1.day1 as day1

some_number = day1.add(0.2, 0.1)
print(day1.add(0.2, 0.1))
print(some_number)
day1.Paid_a_lot_of_money("I paid a lot of money for this function")

def some_function():
    print("This is a function defined in day1part2.py" + str(day1.training_day))
    if __name__ == "__main__":
        print("This program is being run directly.")

some_list = [0, "This is the second index at 1 with some string", 2]

for num in some_list:
    print("This is a loop defined in day1part2.py" + str(num))

def another_function():
    day1.this_will_crash()

another_function()