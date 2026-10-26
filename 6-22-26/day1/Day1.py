student_name = "Tomás Poventud"
course_name = "Proffessional Python Developer"
training_week = 1
training_day = 1
tool_used = "VS Code"

print("Student Name: ", student_name)
print("Course Name: ", course_name)
print("Training Week: ", training_week)
print("Training Day: ", training_day)
print("Tool Used: " + tool_used)

print("Hello, World!")

print("Training Day:".__len__())
print("Training Week:".__len__())
print("2".__len__())

a = 12
b = 11.3
mod = 3 # this is the modulo number we will use later on to perform modulus operations
print(a.__mod__(mod))
print(b.__mod__(mod))
print(0.3)
print(0.1+0.2)
# 0.1 = "01111011 10011001100110011001101"
# 4 = "00000100"
# 2 = "00000010"
# 3 = "00000011"
# 2,147,483,647 = "11111111"

print(0.1+0.5)

def paid_a_lot_of_money():
    print("I paid a lot of money for this 0.3 to be 0.3.")

if __name__ == "__main__":
    variable_expression_of_some_form = "This is some string" * 12
    print(f"Some string text this will not be formatted in any way {variable_expression_of_some_form}")
    print(f"this is some c f string %s %d", "followed by some number", 12)
    print("This is the main module.")