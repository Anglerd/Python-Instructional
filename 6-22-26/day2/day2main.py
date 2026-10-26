# the following is borkend, I do not understand

print("Welcome to class!")
print("today we will be doing some simple drills")
print("using a \"student intake\" script") # only the truly dedicated will see the "problem" here

#def student_intake():
    # this function returns 2 values, the name and then the sex
    #student_name = input("What is your name? ")
    #student_sex = input("What is your sex? (M/F) ")
    #student_grade = input("What is your grade? (9/10/11/12) ")

    #return array_of_info

def simple_print(student_info):
    print(f"Hello, {student_info[0]}! Welcome to class!")
    print(f"You are {student_info[1]} and you are in grade {student_info[2]}.")

if __name__ == "__main__":
    student_info = {}
    while True:
        student_name = input("Enter student name: ")
        student_sex = input("Enter student sex: ")
        student_grade = input("Enter student grade: ")
        student_info[student_name] = {
            "sex": student_sex,
            "grade": student_grade
        }
        another = input("Would you like to enter another student? (Y/N) ")
        if another.lower() != 'y':
            break
    for name in student_info:
        print(f"Student Name: {name}, Sex: {student_info[name]['sex']}, Grade: {student_info[name]['grade']}. The dictionary for this student is: {student_info[name]}") # prints the dictionary for that student
        print(student_info[name]["sex"]) # prints the dictionary for that student