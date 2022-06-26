import enum


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
    RUNE_SERIE = ["Runesword", "Light Brand (indirect)"]


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
class ClassSpecificity:
    HORSEBACK = "Horseback"
    ARMOURED = "Armoured"
    FLYING = "Flying"
    DRAGON = "Dragon"

    MOUNTAIN = "Can cross mountains"
    SEA = "Can cross seas"
    BALLISTIC = "Can use ballistae"  # for archer/sniper class


# type of status effect
class StatusEffect(NoValue):
    POISONED = "poisoned"
    SLEEPING = "Sleeping"
    BERSERK = "Berserk"
    SILENCE = "Silences"
    NOEFFECT = "Nothing"


class HealerEffect(NoValue):
    NOEFFECT = "Nothing"
    pass


class MovementModification(NoValue):
    TELEPORT = "Teleports"
    RESCUE = "Rescue"
    NOEFFECT = "Nothing"


class MapInteraction(NoValue):
    TORCH = "Light up"
    OPEN = "Open door"
    NOEFFECT = "Nothing"


# basic thing
INVENTORY_SIZE = 6  # set the inventory size here
