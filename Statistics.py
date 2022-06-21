import inspect
from dataclasses import dataclass, field
from pprint import pprint


@dataclass
class Statistics:
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
        self.hp = self.m_hp_


"""
def main():
    my = Statistics(1,16,4,7,9,5,2,0,5,5)
    print(my)
    pprint(inspect.getmembers(Statistics, inspect.isfunction))

if __name__ == '__main__':
    main()"""
