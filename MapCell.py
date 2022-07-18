class MapCell:
    def __init__(self, field:int, unit: "Character" = None):
        self.field = field
        self.unit = unit

    def has_unit(self) -> bool:
        return self.unit is not None


