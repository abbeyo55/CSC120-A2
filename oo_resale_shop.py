from computer import *
# potential constraint 

class ResaleShop:
# have blueprint, now need an inventory 

    # What attributes will it need?
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = [] 
        #now have space and memory in the list, object are the computers 
        # always starts as an empty list, can add and remove to it 

#  buy, update_price, sell, print_inventory, refurbish

    # What methods will you need?
    # lists (not dictionary)
    
        #call computer (...) constructor
        # to create new computer instance

        #call inventory.append(...) to add the
        # new computer instance to the inventory
   
    def buy(self, c:Computer):
        self.inventory.append(c)
        # this buys a new computer, adds to the inventory
    
    #def new_computer(self):
        #self.inventory.append(c)
        # this coding is repeditive of buy

    def sell(self, c:Computer):
        if c in self.inventory: 
            self.inventory.remove(c)
        else: print("computer not in inventory")
        # this sells a computer if found in the inventory, if not in inventory it prints that it was not found

    def update_price(self, c:Computer, new_price: int):
        if c in self.inventory: 
            new_price: int
            c.price = new_price
        else:
            print("Item", c, "not found. Cannot update price.")
        # this finds the computer, then updates the price given a new int price, and will replace the old price given 

    def refurbish(self, c: Computer, operating_system_new: str):
        c.operating_system = operating_system_new
        # this finds the computer, then updates the operating system

    def print_inventory(self):
        for c in self.inventory:
            c.printDetails()
        # this prints the new inventory after all attributes 

main()