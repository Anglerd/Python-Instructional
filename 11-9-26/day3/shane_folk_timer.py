# Simple timer written by Shane Folk
# Prompts the user for the number of integer minutes they want a timer for
# then works by performing integer division and modulo math to display
# the time remaining before the end of the timer.
# after the timer ends attempts to play an audible beep
#
# For long times this timer is slightly inaccurate due to how Sleep()
# functions.

import time
import winsound

def countdown(minutes: int) -> None:
    """This is my docstring, it will be shown when "help" is called, usually when you hover over me in an IDE"""
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)   # split into minutes and seconds
        print(f"\r{mins:02d}:{secs:02d}", end="")  # \r redraws the SAME line
        time.sleep(1)                             # wait 1 second
        total_seconds -= 1
    print("\rTime's up!     ")                     # \a (below) makes a beep on some terminals
    print("\a", end="")
    winsound.Beep(1000, 500)


def main():
    time = int(input("Pick a time in mins:"))
    countdown(time)

if __name__ == "__main__":
    main()