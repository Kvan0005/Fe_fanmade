
from dataclasses import dataclass, field
from const import *


@dataclass(match_args=True)
class WeaponAttrsEffect:
    inflict_status_effect: StatusEffect or None
    healer_bonus_effect: HealerEffect or None
    weapon_series: WeaponsSeries or None
    movement_modification: MovementModification or None
    map_interaction: MapInteraction or None
    groups_effectiveness: Group or ClassSpecificity or None
    user_condition: "Character" or None
