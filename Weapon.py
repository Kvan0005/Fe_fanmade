from dataclasses import dataclass, field


@dataclass(frozen=True)
class Weapon:
    name_: str
    rank_: int   # dont know for now
    rng_: list
    wt_: int
    mt_: int
    crt_: int
    uses: int
    worth_: int = field(repr=False)
    wex_: int = field(repr=False)
    effect_: str

    def property(self): pass
