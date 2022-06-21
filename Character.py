import Weapon
from Statistics import Statistics
from Inventory import Inventory
from WeaponSkill import WeaponSkill
from const import *

class Character:
    def __init__(self, lv , hp, att, ski, spd, lck, deff, res, con, mov):
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

    def att_spd(self):
        if self.m_wp is None:
            return 0
        wp_mass = self.m_wp_.wt - self.con_
        return self.spd_ - (wp_mass if wp_mass > 0 else 0)

    def attack(self, other) -> int:
        dmg = self.stat_.att_
        if self.m_wp_.is_runesword():
            dmg //= 2
        dmg += self.wp_dmg_calculation(self.m_wp_, other.m_wp) * self.wp_vs_class_coef(self.m_wp_, other)

    @staticmethod
    def wp_dmg_calculation(wp_1:Weapon, wp_2:Weapon) -> int:
        wp_dmg = wp_1.mt
        pass

    @staticmethod
    def wp_vs_class_coef(main_wp:Weapon, other) -> int:
        pass

    def main_wps(self):
        return self.inv_.pick_first_valid_wps(self.stat_.)

if __name__ == '__main__':
