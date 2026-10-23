def calls_crash(param):
    crash(param)

def crash(param):
    return 1/param

if __name__ == "__main__":
    print("I will print")
    calls_crash(0)