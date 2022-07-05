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

    def alive(self) -> bool:
        """ check is a unit is alive """
        return self.stat_.alive()

    def fight(self, other: "Character") -> None:
        """
        this is when 2 unit actually deal damage to each other by attacking the heal_bar stat (stat_.hp) and all
        outer thing that could during the exchange
        """

        def attacking(unit1: "Character", unit2: "Character") -> None:
            unit2.take_damage(unit1.launch_attack(unit2))

        attacking(self, other)  # first attack

        if other.alive() and other.repostable(self):  # repost (if possible)
            attacking(other, self)

        if self.alive() and other.alive():  # 2nd attack if one can do it (bug: cannot report can do a repost here)
            attacker, defender = self.speed_advantage(other)
            if attacker is not None and attacker.repostable(defender):
                attacking(attacker, defender)

        if isinstance(self.main_wps, Weapon) and self.is_selfdamaging(self.main_wps):  # backslash of "devil axe"
            if PERCENT(31 - self.stat_.lck_):
                self_damage = self.attack(self) - self.defence()
                self.take_damage(self_damage)

    def launch_attack(self, other: "Character") -> int or None:
        """
        this function utilise all needed parameter for a attack included all probability of succeeding or fail
        :return None if a attack has miss the target or a integer if that attack has hit/crit/one hit ko his opponent
        """
        tot_dmg = self.attack(other) - other.defence()
        if PERCENT(self.battle_accuracy(other)):
            if PERCENT(self.battle_critical_rate(other)):
                if isinstance(self, Assassin):
                    if PERCENT(50):
                        return other.stat_.hp  # one hit ko
                tot_dmg *= 3
            return tot_dmg
        return None

    def attack(self, other: "Character") -> int:
        """
        give the amount of damage if a unit_1 hit a unit_2
        """
        dmg = self.stat_.att_
        if self.is_runesword(self.main_wps):
            dmg //= 2
        dmg += self.wp_dmg_calculation(self.main_wps, other.main_wps) * self.wp_vs_class_coef(self.main_wps, other)
        # dmg += self.support_dmg_bonus
        return dmg

    @staticmethod
    def wp_dmg_calculation(wp_1: Weapon, wp_2: Weapon) -> int:
        """
        damage that a weapon can deal and also including if a weapon is advantageous against a another one
        """
        wp_dmg = wp_1.mt_
        wp_dmg += wp_1.weapon_triangle(wp_2)
        return wp_dmg

    @classmethod
    def wp_vs_class_coef(cls, wp: Weapon, unit: "Character") -> int:
        """
        a coefficient that tell if a weapon has a increase efficiency against a Character specificity
        """
        return 2 if unit.group in wp.effect_.groups_effectiveness or f"{cls}" in wp.effect_.groups_effectiveness else 1

    def is_runesword(self, wps: Weapon) -> bool:
        """ if weapons in RUNE_SERIES"""
        return WeaponsSeries.RUNE_SERIE in wps.effect_.weapon_series

    def is_selfdamaging(self, wps: Weapon) -> bool:
        """ if weapons has SELFDEMAGE"""
        return StatusEffect.SELFDEMAGE in wps.effect_.inflict_status_effect

    @property
    def main_wps(self) -> Weapon:
        """
        extract the main weapons of a unit
        """
        return self.inv_.main_wps

    def lv_up(self):
        pass

    def defence(self) -> int:
        """
        give the amount of damage that a unit can absorb
        """
        deff = self.stat_.def_
        # connect to terrain stat >?
        # support bonus
        return deff

    def battle_accuracy(self, other: "Character") -> int:
        """ the in-fight accuracy of a certain unit [0-100] """
        assert (self.main_wps, Weapon)
        precision = self.accuracy(other) - other.avoid()
        if not (0 <= precision <= 100):
            precision = 0 if precision <= 0 else 100
        return precision

    def accuracy(self, other: "Character") -> int:
        """ the value of a unit precision (no size limit) """
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
        """ this can be assimilate to a dodge rate (no size limit)"""
        if isinstance(self.main_wps, Staff):
            return (self.stat_.res_ * 5) + 1  # enemy distance * 2 todo
        avoid = self.stat_.spd_ * 2
        avoid += self.stat_.lck_
        # avoid += support_bonus
        # avoid += terrain bonus
        # avoid += tactician bonus
        return avoid

    def battle_critical_rate(self, other: "Character") -> int:
        """ the probability of a crit in-battle """
        assert (self.main_wps, Weapon)
        if self.is_runesword(self.main_wps):
            return 0
        return self.critical_rate() - other.critical_evade()

    def critical_rate(self) -> int:
        """ the crit rate """
        critical_rate = self.main_wps.crt_
        critical_rate += self.stat_.ski_ * 2
        # crit_rate += support_bonus
        if isinstance(self, (Swordmaster, Berserker)):
            critical_rate += 15
        if self.main_wps.rank_ == 6:
            critical_rate += 5
        return critical_rate

    def critical_evade(self) -> int:
        """ the rate of dodging a crit """
        critical_evade = self.stat_.lck_
        # critical_evade += support_bonus
        # critical_evade += tactician bonus
        return critical_evade

    def speed_advantage(self, other: "Character") -> list["Character"] or None:
        """
        calculation of the possibility of a speed advantage (aka double attack) on the opponent if None,None the no
        advantage for either of them
        first element of the tuple is attacker second one is the defender
        """
        att_spd1 = self.stat_.att_spd(self.main_wps)
        att_spd2 = other.stat_.att_spd(other.main_wps)
        if att_spd1 - att_spd2 >= 4:
            return self, other
        elif att_spd2 - att_spd1 >= 4:
            return other, self
        return None, None

    def repostable(self, other: "Character"):
        """
        check if a unit has what is needed to do a repost
        """
        pass

    def take_damage(self, damage: int) -> None:
        """ reduce a unit health_bar(stat_.hp) by a amount"""
        self.stat_.take_damage(damage)


class LordLyn(Character):
    def __init__(self, *args, **kwargs):
        super(LordLyn, self).__init__(*args, **kwargs)
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
