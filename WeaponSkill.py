from const import *
from dataclasses import dataclass, field


@dataclass(match_args=True)
class WeaponSkill:
    sword_: int = field(default=0)
    lance_: int = field(default=0)
    axe_: int = field(default=0)
    bow_: int = field(default=0)
    staff_: int = field(default=0)
    anima_: int = field(default=0)
    light_: int = field(default=0)
    dark_: int = field(default=0)

    def wp_rk_up(self, weapon: str):
        match weapon:
            case WeaponsType.SWORD.value:
                self.sword_ += 1
            case WeaponsType.LANCE.value:
                self.lance_ += 1
            case WeaponsType.AXE.value:
                self.axe_ += 1
            case WeaponsType.BOW.value:
                self.bow_ += 1
            case WeaponsType.STAFF.value:
                self.staff_ += 1
            case WeaponsType.ANIMA.value:
                self.anima_ += 1
            case WeaponsType.LIGHT.value:
                self.light_ += 1
            case WeaponsType.DARK.value:
                self.dark_ += 1
            case _:
                raise Exception(f"oe kevin tu sais que l'arme: {weapon} n'exite pas alors fk it !")

    def __str__(self):
        return f"sword:{self.sword_}\n" \
               f"lance:{self.lance_}\n" \
               f"axe:{self.axe_}\n" \
               f"bow:{self.bow_}\n" \
               f"staff:{self.staff_}\n" \
               f"anima:{self.anima_}\n" \
               f"light:{self.light_}\n" \
               f"dark:{self.dark_}\n"
def temp_main():
    ar = "sword"
    my_skill = WeaponSkill()
    print(my_skill)
    my_skill.wp_rk_up(WeaponsType.SWORD.value)
    print(my_skill)


"""
utiliser cette idée
b = {'x':42, 'y':None}
function(1, **b) # equal to function(1, x=42, y=None)
"""
