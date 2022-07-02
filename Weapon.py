from dataclasses import dataclass, field
from WeaponAttrsEffect import WeaponAttrsEffect
from const import *
import abc
from Item import Item
import re

@dataclass
class Weapon(metaclass=abc.ABCMeta):
    name_: str
    pre_rank_: str = field(repr=False)
    rank_: int = field(init=False)
    rng_: list or int
    wt_: int
    mt_: int
    hit_: int
    crt_: int
    uses: int
    worth_: int = field(repr=False)
    wex_: int = field(repr=False)
    pre_effect_: str
    effect_: WeaponAttrsEffect = field(init=False, repr=False)

    def __post_init__(self):
        match self.pre_rank_:
            case "E" | "D" | "C" | "B" | "A":
                self.rank_ = abs(ord(self.pre_rank_) - ord("F"))
            case "Prf":
                self.rank_ = 0
            case "S":
                self.rank_ = 6
            case _:
                raise Exception(f'Weapons rank not in the standard ! : {self.pre_rank_}')

        # need to rework but let not do it now
        all_effect = {}

        temps = re.match(r".ffective against (\.+) units",self.pre_effect_)
        if temps:
            all_effect["groups_effectiveness"] = []
            for group in ClassSpecificity:
                if group.value in temps.group(1):
                    all_effect["groups_effectiveness"].append(group)

        for statusEffect in StatusEffect:
            if re.match(statusEffect.value, self.pre_effect_.lower()):
                all_effect["inflict_status_effect"] = statusEffect
                break

        temps = re.match(r"(.+) only", self.pre_effect_)
        if temps:
            temps = temps.group(1).split("/")
            all_effect["user_condition"] = temps

        if re.match(r".ood against \w+, bad against \w+",self.pre_effect_):
            all_effect["weapon_series"] = WeaponsSeries.REAVER_SERIES

        if self.name_ in WeaponsSeries.RUNE_SERIES.value:
            all_effect["weapon_series"] = WeaponsSeries.RUNE_SERIES

        temps = re.findall(r"(\w+) [+](\d*)", self.pre_effect_)
        if temps:
            all_effect["stat_bonus"] = temps

        if self.pre_effect_ in (AttackBonus.DOUBLEATT.value, AttackBonus.NOCOUNTER.value) :
            all_effect["attack_bonus"] = AttackBonus(self.pre_effect_)

        self.effect_ = WeaponAttrsEffect(**all_effect)

    @abc.abstractmethod
    def _weapon_triangle(self, other):
        return 0

    def weapon_triangle(self, other):
        assert not isinstance(other, Item)
        return self._weapon_triangle(other)

    def property(self):
        pass


@dataclass
class Sword(Weapon):

    def _weapon_triangle(self, other):
        if isinstance(other, Axe):
            res = 1
        elif isinstance(other, Lance):
            res = -1
        else:
            res = 0
        if self.name_ in WeaponsSeries.REAVER_SERIES.value or other.name_ in WeaponsSeries.REAVER_SERIES.value:
            res *= -1
        return res


@dataclass
class Axe(Weapon):

    def _weapon_triangle(self, other):
        if isinstance(other, Lance):
            res = 1
        elif isinstance(other, Sword):
            res = -1
        else:
            res = 0
        if self.name_ in WeaponsSeries.REAVER_SERIES.value or other.name_ in WeaponsSeries.REAVER_SERIES.value:
            res *= -1
        return res


@dataclass
class Lance(Weapon):

    def _weapon_triangle(self, other):
        if isinstance(other, Sword):
            res = 1
        elif isinstance(other, Axe):
            res = -1
        else:
            res = 0
        if self.name_ in WeaponsSeries.REAVER_SERIES.value or other.name_ in WeaponsSeries.REAVER_SERIES.value:
            res *= -1
        return res


@dataclass
class Staff(Weapon):
  pass

a = Sword("SlimSword", "E", 1, 2, 3, 100, 5, 30, 480, 1, "-")
b = Lance("SlimSword", "D", 1, 2, 3, 100, 5, 30, 480, 1, "-")
c = Axe("SlimSword", "Prf", 1, 2, 3, 100, 5, 30, 480, 1, "-")
d = "Res +14"
    #for i in range(len(temps.group()) // 3):
    #    v.append((temps.group(1 + (3 * i)), int(temps.group(2 + (3 * i)))))
    #print(v)
print(AttackBonus("Allows 2 consecutive hits"))
"""
cv = re.match(r"(.+) only", d)
if cv:
    cv = map(lambda x: eval(x), cv.group(1).split("/"))
    print(list(cv))
"""

