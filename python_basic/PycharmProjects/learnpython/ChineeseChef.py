# inheritance happens here

from Chef import Chef

class ChineeseChef(Chef):

    def make_fried_rice(self):
        print("This chef makes fried rice")

    # overriding method
    def make_special_dish(self):
        print("This chef makes orange chicken")