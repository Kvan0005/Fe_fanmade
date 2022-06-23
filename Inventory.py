from const import *
from Weapon import Weapon

class Inventory:
    def __init__(self, *args):
        assert (len(args) <= INVENTORY_SIZE)
        self.buffer_ = [None]*INVENTORY_SIZE
        for slot,item in enumerate(args):
            self.buffer_[slot] = item
        self.main_wps_ = self.pick_weapons()

    def swap(self, slot_a , slot_b):
        self.buffer_[slot_a], self.buffer_[slot_b] = self.buffer_[slot_b], self.buffer_[slot_a]


    def pick_weapons(self):pass
    #    if self[0]
    #    for item in self.buffer_:
    #        if isinstance(item, Weapon):
    #
    #def pick_first_valid_wps(self, wp_rank, wp_type):
    #    #todo faire le systeme de première arme
    #    for item in self.buffer_:
    #        if isinstance(item, Weapon):
    #            pass
    #def is_valid_wps(self, wp_rank, wp_type):

    @property
    def main_wps(self):
        return self.main_wps_

    def __getitem__(self, item):
        return self.buffer_[item]

    def __str__(self):
        printed = ""
        for slot,item in enumerate(self.buffer_):
            printed += f"slot {slot} : {item} \n"
        return printed


