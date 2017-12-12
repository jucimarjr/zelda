from MenuComponent import *
from Menu import *
from Diner import *

def main():
    all_menus = Menu()

    diner = Diner()

    all_menus.add(diner)

    print("{}".format(all_menus.get_name()))
    print("{}".format(all_menus.get_description()))
    print("{}".format(all_menus.is_vegetarian()))
    print("{}".format(all_menus.get_price()))

if __name__ == "__main__":
    main()
