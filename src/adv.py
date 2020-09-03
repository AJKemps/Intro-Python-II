from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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

    key = input("Where to next?  ")

    if key == "n":
        try:
            newPlayer.location = newPlayer.location.n_to
            print("---")
            print(f"You are now in the {newPlayer.location.name}")
            print(newPlayer.location.description)
            print("---")
            print("\n")
        except:
            print('Oops! No room in that direction')
    elif key == "s":
        try:
            newPlayer.location = newPlayer.location.s_to
            print("---")
            print(f"You are now in the {newPlayer.location.name}")
            print(newPlayer.location.description)
            print("---")
            print("\n")
        except:
            print('Oops! No room in that direction')
    elif key == "e":
        try:
            newPlayer.location = newPlayer.location.e_to
            print("---")
            print(f"You are now in the {newPlayer.location.name}")
            print(newPlayer.location.description)
            print("---")
            print("\n")
        except:
            print('Oops! No room in that direction')
    elif key == "w":
        try:
            newPlayer.location = newPlayer.location.w_to
            print("---")
            print(f"You are now in the {newPlayer.location.name}")
            print(newPlayer.location.description)
            print("---")
            print("\n")
        except:
            print('Oops! No room in that direction')
    elif key == "q":
        print("\n")
        print("---")
        print("Goodbye!")
        print("---")
        print("\n")
        key = 0
        exit()
    else:
        print("---")
        print("Invalid input. Input options are: \n n to move North \n s to move South \n e to move East \n w to move West \n q to move Quit")
        print("---")
        print("\n")
