from dataclasses import dataclass, field
from const import *


@dataclass
class Weapon:
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


@dataclass
class Sword(Weapon):
    Wps_type:str = SWORD

    def __gt__(self, other):
        match other.Wps_type:
            case "Axe":
                res = 1
            case "Lance":
                res = -1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res

    def __lt__(self, other):
        match other.Wps_type:
            case "Axe":
                res = -1
            case "Lance":
                res = 1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res


@dataclass
class Axe(Weapon):
    Wps_type: str = AXE

    def __gt__(self, other):
        match other.Wps_type:
            case "Lance":
                res = 1
            case "Sword":
                res = -1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res

    def __lt__(self, other):
        match other.Wps_type:
            case "Lance":
                res = -1
            case "Sword":
                res = 1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res


@dataclass
class Lance(Weapon):
    Wps_type: str = LANCE

    def __gt__(self, other):
        match other.Wps_type:
            case "Sword":
                res = 1
            case "Axe":
                res = -1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res

    def __lt__(self, other):
        match other.Wps_type:
            case "Sword":
                res = -1
            case "Axe":
                res = 1
            case _:
                res = 0
        if self.name_ in REAVER_SERIES or other.name_ in REAVER_SERIES:
            res *= -1
        return res


a = Sword("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
b = Lance("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
c = Axe("SlimSword", 1, 1, 2, 3, 100, 5, 30, 480, 1, "-")
print(a>b, a<b)
print(b>c, b<c)
print(c>a, c<a)
