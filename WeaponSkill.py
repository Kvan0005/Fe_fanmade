from const import *


class WeaponSkill:
    def __init__(self, sword=0, lance=0, axe=0, bow=0, staff=0, anima=0, light=0, dark=0):
        self.sword = sword
        self.lance = lance
        self.axe = axe
        self.bow = bow
        self.staff = staff
        self.anima = anima
        self.light = light
        self.dark = dark

    def wp_rk_up(self, weapon:str):
        match weapon:
            case "sword":
                self.sword += 1
            case "lance":
                self.lance += 1
            case "axe":
                self.axe += 1
            case "bow":
                self.bow += 1
            case "staff":
                self.staff += 1
            case "anima":
                self.anima += 1
            case "light":
                self.light += 1
            case "dark":
                self.dark += 1
            case _:
                raise Exception(f"oe kevin tu sais que l'arme: {weapon} n'exite pas alors fk it !")

    def __str__(self):
        return f"sword:{self.sword}\n" \
               f"lance:{self.lance}\n" \
               f"axe:{self.axe}\n" \
               f"bow:{self.bow}\n" \
               f"staff:{self.staff}\n" \
               f"anima:{self.anima}\n" \
               f"light:{self.light}\n" \
               f"dark:{self.dark}\n"


my_skill = WeaponSkill()
print(my_skill)
my_skill.wp_rk_up(SWORD)
print(my_skill)

