#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(user_name, count=0):
    print("{} walks through the door to see a dimly lit hallway.".format(user_name))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} takes the stairs'.format(user_name))
        if (count > 0):
            print("but {}'s not happy about it".format(user_name))
        infinite_stairway_room(user_name, count + 1)
    else:
        back_room(user_name)


def gold_room(user_name):
    print("This room is full of gold.  How much does {} take?".format(user_name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {}'s' not greedy, {} wins!".format(user_name, user_name))
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room(user_name):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(user_name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey" or next == "take" or next == "honey":
            dead("The bear looks at {} then slaps his face off.".format(user_name))
        elif (next == "taunt bear" or next == "taunt") and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(user_name))
            bear_moved = True
        elif (next == "taunt bear" or next == "taunt") and bear_moved:
            dead("The bear gets pissed off and chews {}'s leg off.".format(user_name))
        elif (next == "open door" or next == "open" or next == "door") and bear_moved:
            gold_room(user_name)
        else:
            print("I got no idea what that means.")


def cthulhu_room(user_name):
    print("Here {} sees the great evil Cthulhu.".format(user_name))
    print("He, it, whatever stares at {} and {} goes insane.".format(user_name,user_name))
    print("Does {} flee for his life or eat his head?".format(user_name))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        infinite_stairway_room(user_name)

def back_room(user_name):
    print("{} enters through a back door.".format(user_name))
    print("It is filled with awesome programmers")
    print("{} states his name, and they welcome {} with open arms".format(user_name, user_name))
    print("{} soon starts programming python and never leaves.".format(user_name))
    exit(0)

def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    user_name = input ("What's your name?")
    print("{} is in a dark room.".format(user_name))
    print("There is a door to {}'s right and left.".format(user_name))
    print("Which one does {} take?".format(user_name))

    next = input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    else:
        dead("{} stumble's around the room until he starves.".format(user_name))

if __name__ == '__main__':
    main()
