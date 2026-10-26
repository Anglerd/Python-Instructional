for x in range(9):
    for x in range(1):
        print(x)
    print(x)


print("string")

print("Winter is coming"[1:15:2])

print("😈".lower())
print("😈".upper())


def get_input(prompt, type_converter):
    while True:
        try:
            attempt_score = type_converter(input(f"{prompt}\n"))
            return attempt_score
        except ValueError:
            print("Please input a valid value, restarting")


some_input = get_input("Please enter nothing", str)

if some_input and some_input == "No":
    print("Why would you do this?")

if some_input:
    if some_input == "No":
        print("Why would you do this?")
