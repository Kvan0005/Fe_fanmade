import inspect
from dataclasses import dataclass, field
from pprint import pprint
from Weapon import Weapon


@dataclass(frozen=True)
class Statistics:  # j'ai mis un _ a la fin pour les attributes que considère privé et juste 'hp' qui pourra etre changer a exterior
    lv_: int
    m_hp_: int
    hp: int = field(init=False)
    att_: int
    ski_: int
    spd_: int
    lck_: int
    def_: int
    res_: int
    con_: int
    mov_: int

    def __post_init__(self):
        object.__setattr__(self, 'hp', self.m_hp_)

    def att_spd(self, main_weapons: Weapon):
        if main_weapons is None:
            return 0
        wp_mass = main_weapons.wt_ - self.con_  # main_weapons est aussi dataclass comme celui-ci
        return self.spd_ - (wp_mass if wp_mass > 0 else 0)


def main():
    my = Statistics(1, 16, 4, 7, 9, 5, 2, 0, 5, 5)
    print(my)
    pprint(inspect.getmembers(Statistics, inspect.isfunction))


if __name__ == '__main__':
    main()
