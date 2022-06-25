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


# caracter job specificity
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


# type of status effect
class StatusEffect(NoValue):
    POISONED = "poisoned"
    SLEEPING = "Sleeping"
    BERSERK = "Berserk"
    SILENCE = "Silences"


class HealerEffect(NoValue):
    pass


class MovementModification(NoValue):
    TELEPORT = "Teleports"
    RESCUE = "Rescue"


class MapInteraction(NoValue):
    TORCH = "Light up"
    OPEN = "Open door"


# basic thing
INVENTORY_SIZE = 6  # set the inventory size here
