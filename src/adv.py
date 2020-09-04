from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'knife': Item("knife", "for hand to hand combat"),
    'torch': Item("torch", "to light the way"),
    'pistol': Item("pistol", "in case of competition"),
}

print(vars(items['knife']))

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['torch'], items['knife']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  items['pistol']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['knife']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

newPlayer = Player('Alex', room['outside'])

print(newPlayer)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing = True

while playing:

    def formatPrint():
        print("\n")
        print("* * *")
        print("\n")

    key = input(f"You are in {newPlayer.location.name} \n\nWhat's next?  ")

    entry = key.split()

    if len(entry) > 1:
        if entry[0] == "grab":
            newPlayer.pick_up(entry[1])
            entry = 1
        elif entry[0] == "drop":
            newPlayer.drop(entry[1])
            entry = 1
        else:
            formatPrint()
            print(
                "Incorrect input! \n\n Enter grab or drop, followed by item name \n\nOr Q to quit")
            formatPrint()
            entry = 1
    elif len(entry) <= 1:
        if key == "n" or key == "s" or key == "e" or key == "w":
            newPlayer.move(key)
        elif key == "q":
            formatPrint()
            print("Goodbye!")
            formatPrint()
            playing = False
            exit()
        elif key == "i" or key == "inventory":
            newPlayer.get_inventory()
        else:
            formatPrint()
            print(
                "Incorrect input! \n\nEnter a cardinal direction to move \n\nOr Q to quit")
            formatPrint()
