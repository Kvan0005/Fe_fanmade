from Weapon import Weapon
from Statistics import Statistics
from Inventory import Inventory
from WeaponSkill import WeaponSkill
from const import *

class Character:
    def __init__(self,name, lv , hp, att, ski, spd, lck, deff, res, con, mov):
        self.name = name
        self.stat_ = Statistics(lv_=lv , m_hp_=hp, att_=att, ski_=ski, spd_=spd, lck_=lck, def_=deff, res_=res, con_=con, mov_=mov)
        self.inv_ = Inventory()
        self.stat_eff_ = None
        self.wps_ski_ = WeaponSkill()

    def launch_attack(self, other):
        self.attack(other)

    def defend(self, other):
        pass

    def lv_up(self):
        pass

    def attack(self, other) -> int:
        dmg = self.stat_.att_
        if self.is_runesword(self.main_wps): # pas fait les porp des arme
            dmg //= 2
        dmg += self.wp_dmg_calculation(self.main_wps, other.main_wps) * self.wp_vs_class_coef(self.main_wps, other)

    @staticmethod
    def wp_dmg_calculation(wp_1:Weapon, wp_2:Weapon) -> int:
        wp_dmg = wp_1.mt_
        pass

    @staticmethod
    def wp_vs_class_coef(main_wp:Weapon, other) -> int:
        pass

    def is_runesword(self, wps):
        return wps.property in ["Runesword", "Light Brand (indirect)"]

    @property
    def main_wps(self)  -> Weapon:
        return self.inv_.main_wps

if __name__ == '__main__':
