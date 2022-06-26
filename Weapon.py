from dataclasses import dataclass, field
from WeaponAttrsEffect import WeaponAttrsEffect
from const import *
import abc
from Item import Item


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
        all_effect = {}
        for phrase in self.pre_effect_.split(","):
            pass
            if "Effective against" in phrase:
                pass


    @abc.abstractmethod
    def _weapon_triangle(self, other):
        pass

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


a = Sword("SlimSword", "E", 1, 2, 3, 100, 5, 30, 480, 1, "-")
b = Lance("SlimSword", "D", 1, 2, 3, 100, 5, 30, 480, 1, "-")
c = Axe("SlimSword", "Prf", 1, 2, 3, 100, 5, 30, 480, 1, "-")
print(a)
