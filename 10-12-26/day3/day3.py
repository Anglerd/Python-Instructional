#Today will mainly be about learning if, elif, else and fully explaining block logic
from random import randint

def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a value of the type {type_converter}")

if __name__ == "__main__":
    print("This is the main")
    user_guess = get_input("Guess my number!", int)
    #lottery = randint(0, 1000)
    lottery = 500
    #megaball = randint(0, 1000)
    megaball = 500
    if lottery == user_guess:
        print("You win the lottery!")
    elif lottery - 1 <= user_guess <= lottery + 1: # lottery - 1 <= user_guess && userguess <= lottery + 1
        if get_input("Close, guess again!", int) == lottery:
            print("You guessed correctly!")
        else:
            print("Maybe next time")
    elif lottery - 10 <= user_guess <= lottery + 10:
        print("Close but no cigar")
    elif lottery - 100 <= user_guess <= lottery + 100:
        print("At least in the ballpark")
    else:
        print("Not even close!")
        quit()
    print(f"The lottery number was {lottery}")
    if lottery != megaball:
        print("The megaball was a miss this time")
    elif user_guess == lottery:
        print("You are the super winner, get a super chicken dinner!")

    """
    and not or
    &&  !   | |
    6 == 6 and 7 == 7
    6 == 6 and 7 == 8
    not 6 == 6
    6 == 6 or 7 == 8
    """

    """
    and not or
    ==
    <
    >
    <=
    >=
    !=
    non-inclusive
    0 < number < 10
    inclusive
    1 <= number <= 9

    float
    non-inlusive
    0 < float_num < 10
    True 0.00000001
    False 0
    True 9.999999
    False 10
    inclusive
    0 <= float_num <= 10
    True 0.00000001
    True 0
    True 9.999999
    True 10
    """

    """
    match user_guess:
        case n if n == lottery:
            print("You win the lottery!")
        case n if lottery - 1 <= n <= lottery + 1:
            if get_input("Close, guess again!", int) == lottery:
                print("You guessed correctly!")
            else:
                print("Maybe next time")
        case n if lottery - 10 <= n <= lottery + 10:
            print("Close but no cigar")
        case n if lottery - 100 <= n <= lottery + 100:
            print("At least in the ballpark")
        case _:
            print("Not even close!")
            quit()
    print(f"The lottery number was {lottery}")
    """
"""
match user_guess:
  case n if n == lottery:
    print("You win the lottery!")
  case n if lottery - 1 <= n <= lottery + 1:
     if get_input("Close, guess again!", int) == lottery:
       print("You guessed correctly!")
     else:
       print("Maybe next time")
  case n if lottery - 10 <= n <= lottery + 10:
    print("Close but no cigar")
  case n if lottery - 100 <= n <= lottery + 100:
    print("At least in the ballpark")
  case _:
    print("Not even close!")
    quit()
print(f"The lottery number was {lottery}")
"""