from Weapon import Weapon
from Statistics import Statistics
from Inventory import Inventory
from WeaponSkill import WeaponSkill
from const import *
import abc


class Character(metaclass=abc.ABCMeta):
    def __init__(self, name, lv, hp, att, ski, spd, lck, deff, res, con, mov):
        self.name = name
        self.stat_ = Statistics(lv_=lv, m_hp_=hp, att_=att, ski_=ski, spd_=spd, lck_=lck, def_=deff, res_=res, con_=con,
                                mov_=mov)
        self.inv_ = Inventory()
        self.stat_eff_ = None
        self.wps_ski_ = WeaponSkill()
        self.group = None
        self.wps_type = []

    # ----------------------------------attack/defense section----------------------------------------------------------
    #
    def launch_attack(self, other):
        self.attack(other)
        return True

    def attack(self, other) -> None:
        dmg = self.stat_.att_
        if self.is_runesword(self.main_wps):  # pas fait les porp des arme
            dmg //= 2
        dmg += self.wp_dmg_calculation(self.main_wps, other.main_wps) * self.wp_vs_class_coef(self.main_wps, other)

    @staticmethod
    def wp_dmg_calculation(wp_1: Weapon, wp_2: Weapon) -> int:
        wp_dmg = wp_1.mt_
        wp_dmg += wp_1.weapon_triangle(wp_2)
        return wp_dmg

    @staticmethod
    def wp_vs_class_coef(wp: Weapon, unit) -> int:
        pass

    def is_runesword(self, wps):
        return wps.property in WeaponsSeries.RUNE_SERIE.value

    @property
    def main_wps(self) -> Weapon:
        return self.inv_.main_wps

    def lv_up(self):
        pass

    def defend(self, other):
        pass


class LordLyn(Character):
    def __init__(self, *args):
        super(LordLyn, self).__init__(*args)
        self.group = Group.FOOT.value
        self.wps_type.append(WeaponsType.SWORD.value)


class BladeLord(Character):
    pass


class LordEliwood(Character):
    pass


class KnightLord(Character):
    pass


class LordHector(Character):
    pass


class Mercenary(Character):
    pass


class Hero(Character):
    pass


class Myrmidon(Character):
    pass


class Swordmaster(Character):
    pass


class Thief(Character):
    pass


class Assassin(Character):
    pass


class ArmourKnight(Character):
    pass


class General(Character):
    pass


class Soldier(Character):
    pass


class Fighter(Character):
    pass


class Warrior(Character):
    pass


class Bandit(Character):
    pass


class Pirate(Character):
    pass


class Corsair(Character):
    pass


class Berserker(Character):
    pass


class Archer(Character):
    pass


class Sniper(Character):
    pass


class Nomad(Character):
    pass


class NomadTrooper(Character):
    pass


class Cavalier(Character):
    pass


class Paladin(Character):
    pass


class PegasusKnight(Character):
    pass


class FalconKnight(Character):
    pass


class WyvernRider(Character):
    pass


class WyvernLord(Character):
    pass


class Monk(Character):
    pass


class Cleric(Character):
    pass


class Bishop(Character):
    pass


class Troubadour(Character):
    pass


class Valkyrie(Character):
    pass


class Mage(Character):
    pass


class Sage(Character):
    pass


class ArchSage(Character):
    pass


class Shaman(Character):
    pass


class Druid(Character):
    pass


class DarkDruid(Character):
    pass


class Bard(Character):
    pass


class Dancer(Character):
    pass


class MagicSeal(Character):
    pass


class Civilian(Character):
    pass


if __name__ == '__main__':
    a = Character("jorissen", 1, 16, 4, 7, 9, 5, 2, 0, 5, 5)
