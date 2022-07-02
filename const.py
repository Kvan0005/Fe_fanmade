import enum
import random


class NoValue(enum.Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


# weapons type
class WeaponsType(NoValue):
    SWORD = "Sword"
    LANCE = "Lance"
    AXE = "Axe"
    BOW = "Bow"
    STAFF = "Staff"
    ANIMA = "Anima"
    LIGHT = "Light"
    DARK = "Dark"


# special weapons
class WeaponsSeries(NoValue):
    REAVER_SERIES = ["Lancereaver", "Swordreaver", "Axereaver"]
    RUNE_SERIES = ["Runesword", "Light Brand", "Wind Sword"]


# caracter mouvement class specificity
class Group(NoValue):
    FOOT = "Foot"
    ARMOURS = "Armours"
    KNIGHTS_1 = "Knights 1"
    KNIGHTS_2 = "Knights 2"
    NOMADS = "Nomads"
    NOMAD_TROOPERS = "Nomad Troopers"
    FIGHTERS = "Fighters"
    BANDITS = "Bandits"
    MAGES = "Mages"
    FLIERS = "Fliers"


# character specificity
class ClassSpecificity(NoValue):
    HORSEBACK = "horseback"
    ARMOURED = "armoured"
    FLYING = "flying"
    DRAGON = "dragon"
    MOUNTED = "mounted"
    MOUNTAIN = "Can cross mountains"
    SEA = "Can cross seas"
    BALLISTIC = "Can use ballistae"  # for archer/sniper class


# type of status effect
class StatusEffect(NoValue):
    POISONED = "poisoned"
    SLEEPING = "sleeping"
    BERSERK = "berserk"
    SILENCE = "silences"
    SELFDEMAGE = "may damage user"
    NOEFFECT = "Nothing"


class HealerEffect(NoValue):
    NOEFFECT = "Nothing"
    pass


class MovementModification(NoValue):
    TELEPORT = "teleports"
    RESCUE = "rescue"
    NOEFFECT = "Nothing"


class MapInteraction(NoValue):
    TORCH = "light up"
    OPEN = "open door"
    NOEFFECT = "Nothing"


class AttackBonus(NoValue):
    DOUBLEATT = 'Allows 2 consecutive hits'
    NOCOUNTER = 'Cannot be countered'


# basic thing

class Terrain(NoValue):
    pass


INVENTORY_SIZE = 6  # set the inventory size here


def PERCENT():
    return random.randint(0, 100)
