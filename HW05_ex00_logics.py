#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """

    try:
        input_no = int(input("Enter an integer:"))
    except:
        print("Please enter a valid integer!")
        return

    # Odd/even check, and print message
    if input_no % 2 == 0:
        print ("{} is an even integer".format(input_no))
    else:
        print ("{} is an odd integer".format(input_no))


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    
    for count in range(1, 101):
        print("{:<3}".format(repr(count)), end="")
        # Prints a new line after printing 10 digits on one line
        if count % 10 == 0:
            print("")


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    average = 0
    count = 0
    while True:
        user_input = input("Please enter a number (Enter 'done' to exit):")
        if user_input == 'done':
            return
        try:
            input_no = float(user_input)
        except:
            print("Please enter a valid number (or 'done')")
            continue
        average = (input_no + average * count) / (count + 1)
        count = count + 1
        print("The average so far is {}".format(average))


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
