import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(tacklebox):
    print_pause("Let's go to the window and check the weather outside.")
    weather = random.choice(['great', 'terrible', 'ok'])
    print_pause("It is " + weather + " outside.")
    print_pause("Do you want to go fishing?")
    enter("go fishing", "take a nap")
    while True:
        choice = input()
        if choice == '1':
            print_pause("Let's see if we can catch a fish over 6 lbs!")
            house(tacklebox)
        elif choice == '2':
            print_pause("YOU LOSE! GAME OVER!")
            nap()
            play_again()
        else:
            print_pause("Sorry, I don't understand.")
            enter("go fishing", "go take a nap")


def house(tacklebox):
    print_pause("You better hurry before the fish stop biting.\n"
                "Do you want to go to the garage or down to the lake?")
    enter("go to the garage", "go down to the lake")
    while True:
        choice = input()
        if choice == '1':
            garage(tacklebox)
        elif choice == '2':
            lake(tacklebox)
        else:
            print_pause("Sorry, I don't understand.")
            enter("go to the gargae", "go down to the lake")


def garage(tacklebox):
    print_pause("The garage is a mess! I hope you can find your lucky lure!")
    if "lucky lure" in tacklebox:
        print_pause("You already put your lucky lure in your tacklebox. "
                    "Let's go down to the lake.")
        lake(tacklebox)
    else:
        print_pause("There it is, by your tacklebox. "
                    "Let's go down to the lake.")
        tacklebox.append("lucky lure")
        lake(tacklebox)


def lake(tacklebox):
    print_pause("The fish are jumping! Let's see if we can catch a big one!\n"
                "You cast your lure into the water... now we wait.")
    if "lucky lure" in tacklebox:
        print_pause("You got a bite, set the hook!.")
        fish_weight = random.randint(1, 10)
        print_pause("The fish weighed " + str(fish_weight) + "lbs")
        if fish_weight > 6:
            print_pause("YOU WIN!")
            play_again()
        else:
            print_pause("Your fish wasn't over 6 lbs.\n"
                        "Do you want to cast again or go take a nap?")
            enter("keep fishing", "go take a nap")
            while True:
                choice = input()
                if choice == '1':
                    lake(tacklebox)
                elif choice == '2':
                    print_pause("YOU LOSE! GAME OVER!")
                    nap()
                    play_again()
                else:
                    print_pause("Sorry, I don't understand.")
                    enter("keep fishing", "go take a nap")
    else:
        print_pause("They don't seem to like your lure...\n")
        print_pause("Do you want to cast again or look for your lucky lure?")
        enter("go to garage", "cast again")
        while True:
            choice = input()
            if choice == '1':
                garage(tacklebox)
            elif choice == '2':
                lake(tacklebox)
            else:
                print_pause("Sorry, I don't understand.")
                enter("go to the garage", "cast again")


def nap():
    print_pause("Night night. Zzzzzzzzzzzzz")


def play_again():
    enter("play again", "exit")
    while True:
        choice = input()
        if choice == '1':
            go_fishing()
        elif choice == '2':
            print_pause("Bye bye!")
            quit()
        else:
            print_pause("Sorry, I don't understand.")
            enter("play again", "exit")


def enter(str1, str2):
    print_pause("Enter 1 to " + str1 + ".")
    print_pause("Enter 2 to " + str2 + ".")
    print_pause("What would you like to do? ")
    print_pause("(Please enter 1 or 2).")


def go_fishing():
    tacklebox = []
    intro(tacklebox)


go_fishing()
