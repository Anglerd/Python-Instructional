# print("Today we will be opening and reading files")

# file = open("day5\\starting questions.txt", "rt")
# file.close()
def my_open(location, options="rt"):
    """Attempts to open a file, returns None on failure"""
    try:
        return open(location, options)
        """
        # deprecated when this turned into a function as the function does not work in this way
        with open(location, options) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(line)
            for line in file:
                line = line.strip()
                print(line)
        """
    except FileNotFoundError:
        print(f"The file you specified was in the wrong location: {location}")
        return None
# the file is closed here
"r" # read - default
"a" # append
"w" # write
"x" # create

"t" # text - default
"b" # binary

"""this is some text in a file
this is the next line in the file"""

if __name__ == "__main__":
    base_file = my_open(r"day5\scratch.txt")
    file_lines = base_file.readlines()
    new_lines = ""
    for line in file_lines:
        this_line = ""
        for character in line:
            if character == ":":
                character = ","
            this_line += character
        new_lines += this_line
    # new_lines = new_lines[:-2] # this is done to remove the newline at the end of the file if readlines is not used
    new_file = my_open(r"day5\example.csv", "w")
    new_file.write(new_lines)