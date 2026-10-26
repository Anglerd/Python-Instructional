def my_open(location, options="rt"):
    try:
        return open(location, options)
    except FileNotFoundError:
        print(f"The specified file does not exist: {location}")
        return None

def get_lognum(file):
    lines = file.readlines()
    last_line = lines[-1]
    sections = last_line.split(",")
    return int(sections[0][12:])

def create_log(log_info):
    global lognum
    lognum += 1
    return f"This is log {lognum}, with the information: {log_info}"

if __name__ == "__main__":
    log_file = "day5\\bills.log"
    keep_going = True
    log_string = ""
    this_log = my_open(log_file)
    lognum = get_lognum(this_log)
    this_log.close()
    while keep_going:
        log_string += create_log(input("Enter this log's info")) + "\n"
        if "y" not in input("Would you like to continue? y/n").lower():
            keep_going = False
    log_file = my_open(log_file, "a")
    log_file.write(log_string)
    log_file.close()