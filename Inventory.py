from Fe_fanmade.const import *
from Fe_fanmade.Weapon import Weapon

class Inventory:
    def __init__(self, *args):
        assert (len(args)<=INVENTORY_SIZE)
        self.buffer_ = [None]*INVENTORY_SIZE
        for slot,item in enumerate(args):
            self.buffer_[slot] = item

    def swap(self, slot_a , slot_b):
        self.buffer_[slot_a], self.buffer_[slot_b] = self.buffer_[slot_b], self.buffer_[slot_a]

    def pick_first_valid_wps(self, wp_rank, wp_type):
        #todo faire le systeme de première arme
        for item in self.buffer_:
            if isinstance(item, Weapon):
                pass

    def __str__(self):
        printed = ""
        for slot,item in enumerate(self.buffer_):
            printed += f"slot {slot} : {item} \n"
        return printed


