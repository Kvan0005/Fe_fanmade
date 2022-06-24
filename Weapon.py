from dataclasses import dataclass, field
from const import *
import abc
from Item import Item


@dataclass
class Weapon(metaclass=abc.ABCMeta):
    name_: str
    rank_: int  # dont know for now
    rng_: list or int
    wt_: int
    mt_: int
    hit_: int
    crt_: int
    uses: int
    worth_: int = field(repr=False)
    wex_: int = field(repr=False)
    effect_: str

    @abc.abstractmethod
    def _weapon_triangle(self, other):
        pass

    def weapon_triangle(self,other):
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
        if self.name_ in WeaponsSeries.REAVER_SERIES.value or other.name_ in WeaponsSeries.REAVER_SERIES.value :
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


a = Sword("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
b = Lance("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
c = Axe("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
print(a)
