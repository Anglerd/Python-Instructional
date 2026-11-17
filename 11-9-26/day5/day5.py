import random
import os
if __name__ == "__main__":
    print("opening and reading files")
    # input("Please enter some input")
    """
    this_file = open("./day5/starting questions.txt", "rb")
    "r"
    "w"
    "x"
    "a"

    "t"
    "b"
    all_lines = []
    for line in this_file:
        print(line.strip())
        all_lines.append(line.strip())
    print(all_lines)
    print(this_file.read())
    this_file.close()
    my_math = 7 + 7
    my_math == 14
    with open("./day5/scratch.csv") as this_file:
        new_file = []
        for line in this_file:
            new_file.append(line.strip().split(" "))
    output_string = ""
    for line in new_file:
        for word in line:
            output_string += f"{word},"
        output_string = output_string[:-1] + "\n"
    output_string = output_string[:-1]
    with open("./day5/car.csv", "w") as this_file:
        this_file.write(output_string)
    # this_file is closed automagically here
    with open("./day5/starting questions.txt", "a") as this_file:
        this_file.write("This will be appended at the end")
    """
    MIN_NUM = 0
    MAX_NUM = 1000
    MAX_LIVES = 50
    SAVE_LOCATION = "day5/save_file.sav"
    lives = None
    try:
        with open(SAVE_LOCATION, "r") as save_file:
            for index, line in enumerate(save_file):
                if index == 0:
                    lives = int(line)
                elif index == 1:
                    number = int(line)
    except FileNotFoundError:
        print("Starting a new game")
        lives = MAX_LIVES
        number = random.randint(MIN_NUM, MAX_NUM)
    while True:
        if not lives:
            lives = MAX_LIVES
            number = random.randint(MIN_NUM, MAX_NUM)
        while lives > 0:
            guessed_num = int(input(f"Guess a number from {MIN_NUM} to {MAX_NUM}"))
            if guessed_num == number:
                print("You win!")
                break
            else:
                print("Guess again!")
                lives -= 1
                with open(SAVE_LOCATION, "w") as save_file:
                    save_file.write(f"{lives}\n{number}")
        os.remove(SAVE_LOCATION)
        if lives == 0:
            print("You lose!")
        lives = False
        if "y" not in input("Would you like to play again? y/n").lower():
            print("Goodbye")
            quit()