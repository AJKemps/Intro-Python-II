# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def formatPrint(self):
        print("\n")
        print("* * *")
        print("\n")

    def locationPrint(self):

        items = self.location.items

        if len(self.location.items) >= 1:
            self.formatPrint()
            print(f"You are now in the {self.location.name}.")
            print("\n")
            print(self.location.description)
            print("\n")
            for item in items:
                print(
                    f'There is a {item.name}, {item.description}.')
            self.formatPrint()
        elif len(self.location.items) < 1:
            self.formatPrint()
            print(f"You are now in the {self.location.name}.")
            print("\n")
            print(self.location.description)
            self.formatPrint()

    def move(self, key):
        try:
            if key == "n":
                self.location = self.location.n_to
                self.locationPrint()
            elif key == "s":
                self.location = self.location.s_to
                self.locationPrint()
            elif key == "e":
                self.location = self.location.e_to
                self.locationPrint()
            elif key == "w":
                self.location = self.location.w_to
                self.locationPrint()
        except:
            print("\n")
            print("* * *")
            print("\n")
            print('Oops! No room in that direction')
            print("\n")
            print("* * *")
            print("\n")

    def get_inventory(self):
        if len(self.inventory) < 1:
            self.formatPrint()
            print("No items in inventory")
            self.formatPrint()
        else:
            self.formatPrint()
            print('Current Inventory:')
            for item in self.inventory:
                print(f'A {item.name}, {item.description}')
            self.formatPrint()

    def pick_up(self, item):
        items = self.location.items

        name = ""
        description = ""
        exists = False

        for i, x in enumerate(items):
            if x.name == item:
                name = x.name
                description = x.description
                exists = True

        # for item in items:
        #     print(item.name)
        #     if str(item.name) == str(item):
        #         item.name = name
        #         item.description = description
        #         exists = True
        #         print("SUCCESS")

        if exists == False:
            print("Item not available")
        elif exists == True:
            self.inventory.append(Item(name, description))
            self.location.item_picked_up(item)
            self.formatPrint()
            print(f'You picked up a {item}')
            self.formatPrint()

    def drop(self, item):
        items = self.inventory

        name = ""
        description = ""
        exists = False
        id = ''

        for i, x in enumerate(items):
            if x.name == item:
                name = x.name
                description = x.description
                exists = True
                id = i

        if exists == False:
            print("Item not in inventory")
        elif exists == True:
            self.inventory.pop(id)
            self.location.item_dropped(name, description)
            self.formatPrint()
            print(f'You dropped a {item}')
            self.formatPrint()

    def __str__(self):
        return f"\n* * * \n\nWelcome {self.name}! \n\nYou are currently in the {self.location.name} room. \n\nPlease enter N, S, E, W, or Q. \n\n* * *\n"
