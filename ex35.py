from sys import exit

def gold_room():
    print "This room is full of gold, How much do you take?"

    choice = raw_input("> ")

    try:
        int(choice)
    except ValueError:
        print "Type a number"
    else:
            if int(choice) < 50:
                print "Nice, not greedy, win"
                exit(0)
            else:
                dead("You greedy")

def bear_room():
    print "Bear here"
    print "Honey here"
    print "Fat bear blocks door"
    print "How do you move it?"

    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead(why="The bear mauled your face")
        elif choice ==  "taunt bear"   and not bear_moved:
            print "Bear has moved"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead(why="You annoyed Pinky")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "you can use 'taunt bear' or 'open door'"


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print "You are dead, nice",why
    exit(0)


def start():
    print "dark room, two doors"

    choice = raw_input("> ")

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead(why="You starve")

start()
