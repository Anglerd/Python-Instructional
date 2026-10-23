if __name__ == "__main__":
    with open(r".\day5\output.txt") as file:
        file_lines = []
        for line in file:
            file_lines.append(line.strip().split(" "))
        #print(file_lines)
    file_writer = ""
    for line in file_lines:
        for info in line:
            file_writer += f"{info},"
        file_writer = file_writer[:-1] + "\n"
    file_writer = file_writer[:-1]
    file_to_write = open(r".\day5\output.csv", "w")
    file_to_write.write(file_writer)
    file_to_write.close()