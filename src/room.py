# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, *items):
        self.name = name
        self.description = description
        self.items = [*items]

    def item_picked_up(self, item):

        remove_id = "hi"

        for i, x in enumerate(self.items):
            if x.name == item:
                remove_id = i

        self.items.pop(remove_id)

    def item_dropped(self, name, description):

        self.items.append(Item(name, description))

        # for i, x in enumerate(self.items):
        #     if x.name == item:
        #         remove_id = i
        #         print("SUCCESS Item Picked Up", i)

        # self.items.pop(remove_id)
