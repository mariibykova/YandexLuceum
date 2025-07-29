class Note:
    notes = {"до", "ре", "ми", "фа", "соль", "ля", "си"}

    def __init__(self, pitch: str):
        if pitch not in self.notes:
            raise ValueError(f"Недопустимая высота ноты: {pitch}")
        self.pitch = pitch

    def play(self):
        print(self.pitch)

    long = {
        "до": "до-о",
        "ре": "ре-э",
        "ми": "ми-и",
        "фа": "фа-а",
        "соль": "со-оль",
        "ля": "ля-а",
        "си": "си-и",
    }

    def __init__(self, pitch: str, is_long: bool = False):
        if pitch not in self.notes:
            raise ValueError(f"Недопустимая высота ноты: {pitch}")
        self.pitch = pitch
        self.is_long = is_long

    def __str__(self) -> str:
        return self.long[self.pitch] if self.is_long else self.pitch
