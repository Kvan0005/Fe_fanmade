from Weapon import *
import random
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
        self.terrain = None

    # ----------------------------------attack/defense section----------------------------------------------------------
    def fight(self, other:"Character"):
        speed_advantage = self.speed_advantage(other)
        self.launch_attack(other)
        if other.stat_.hp > 0 and other.in_range(self):
            pass


    def launch_attack(self, other: "Character"):
        tot_dmg = self.attack(other) - other.defence()
        if self.battle_accuracy(other) > PERCENT():
            if self.battle_critical_rate(other) > PERCENT():
                if isinstance(self, Assassin):
                    if 50 > PERCENT():
                        other.stat_.hp -= other.stat_.hp  # one hit ko
                tot_dmg *= 3
            other.stat_.hp -= tot_dmg


    def attack(self, other) -> int:
        dmg = self.stat_.att_
        if self.is_runesword(self.main_wps):  # pas fait les porp des arme
            dmg //= 2
        dmg += self.wp_dmg_calculation(self.main_wps, other.main_wps) * self.wp_vs_class_coef(self.main_wps, other)
        # dmg += self.support_dmg_bonus
        return dmg

    @staticmethod
    def wp_dmg_calculation(wp_1: Weapon, wp_2: Weapon) -> int:
        wp_dmg = wp_1.mt_
        wp_dmg += wp_1.weapon_triangle(wp_2)
        return wp_dmg

    @classmethod
    def wp_vs_class_coef(cls, wp: Weapon, unit: "Character") -> int:
        return 2 if wp.effect_.groups_effectiveness == unit.group or f"{cls}" == wp.effect_.groups_effectiveness else 1

    def is_runesword(self, wps):
        return wps.effect_.weapon_series == WeaponsSeries.RUNE_SERIE

    @property
    def main_wps(self) -> Weapon:
        return self.inv_.main_wps

    def lv_up(self):
        pass

    def defence(self) -> int:
        deff = self.stat_.def_
        # connect to terrain stat >?
        pass

    def battle_accuracy(self, other: "Character") -> int:
        assert (self.main_wps, Weapon)
        return self.accuracy(other) - other.avoid()

    def accuracy(self, other: "Character") -> int:
        if isinstance(self.main_wps, Staff):
            return 30 + (self.stat_.att_ * 5) + self.stat_.ski_
        triangle_bonus = 15  # can be modulate
        hit = self.main_wps.hit_
        hit += self.stat_.ski_ * 2
        hit += self.stat_.lck_ * 2
        # hit += support_bonus
        hit += triangle_bonus * self.main_wps.weapon_triangle(other.main_wps)
        if self.main_wps.rank_ == 6:
            hit += 5
        # tactician bonus ?
        return hit

    def avoid(self) -> int:
        if isinstance(self.main_wps, Staff):
            return (self.stat_.res_ * 5) + 1  # enemy distance * 2 todo
        avoid = self.stat_.spd_ * 2
        avoid += self.stat_.lck_
        # avoid += support_bonus
        # avoid += terrain bonus
        # avoid += tactician bonus
        return avoid

    def battle_critical_rate(self, other: "Character") -> int:
        assert (self.main_wps, Weapon)
        if self.main_wps.effect_.weapon_series == WeaponsSeries.RUNE_SERIES:
            return 0
        return self.critical_rate() - other.critical_evade()

    def critical_rate(self) -> int:
        critical_rate = self.main_wps.crt_
        critical_rate += self.stat_.ski_ * 2
        # crit_rate += support_bonus
        if isinstance(self, (Swordmaster, Berserker)):
            critical_rate += 15
        if self.main_wps.rank_ == 6:
            critical_rate += 5
        return critical_rate

    def critical_evade(self) -> int:
        critical_evade = self.stat_.lck_
        # critical_evade += support_bonus
        # critical_evade += tactician bonus
        return critical_evade

    def speed_advantage(self, other:"Character"):
        att_spd1 = self.stat_.att_spd(self.main_wps)
        att_spd2 = other.stat_.att_spd(other.main_wps)
        if att_spd1 - att_spd2 >= 4:
            res = 1
        elif att_spd2 - att_spd1 >= 4:
            res = -1
        else:
            res = 0
        return res

    def in_range(self, other:"Character"):
        pass

class LordLyn(Character):
    def __init__(self, *args):
        super(LordLyn, self).__init__(*args)
        self.group = Group.FOOT
        self.wps_type.append(WeaponsType.SWORD)


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
    a = Civilian("jorissen", 1, 16, 4, 7, 9, 5, 2, 0, 5, 5)
    print(isinstance(a, Character))
