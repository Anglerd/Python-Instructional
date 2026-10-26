# open("file_name", "some_options")
# input("some_input")

if __name__ == "__main__":
    try:
        test_file = open("day5\\scratch_paper.txt", "r")
    except FileNotFoundError:
        print("File not found.")
    else:
        with test_file:
            stripped_array = test_file.readlines()
        #we have exited the with block on this level of indentation    
        for num, line in enumerate(stripped_array):
            stripped_array[num] = line.strip().split(" ")
        """
        stripped_array = []
        for line in test_file:
            stripped_array.append(line.strip().split(" "))
        test_file.close
        """
        print(stripped_array)
        collected_string = ""
        for line in stripped_array:
            for info in line:
                collected_string += f"{info},"
                #collected_string += info + ","
            collected_string += "\n"
        test_file_2 = open("day5\\some_new_file.csv", "w")
        test_file_2.write(collected_string)