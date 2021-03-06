from dataclasses import dataclass, field
from const import *


@dataclass(kw_only=True)
class WeaponAttrsEffect:
    inflict_status_effect: StatusEffect or None
    healer_bonus_effect: HealerEffect or None
    weapon_series: WeaponsSeries or None
    movement_modification: MovementModification or None
    map_interaction: MapInteraction or None
    groups_effectiveness: Group or ClassSpecificity or list[Group] or list[ClassSpecificity] or None
    user_condition: list[str] or None
    stat_bonus: list[tuple[str, int]]
    attack_bonus: AttackBonus
