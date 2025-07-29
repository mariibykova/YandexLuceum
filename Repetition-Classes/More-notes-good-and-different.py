PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
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
        if pitch not in PITCHES:
            raise ValueError(f"Недопустимая высота ноты: {pitch}")

        self.pitch = pitch
        self.is_long = is_long

    def __str__(self) -> str:
        return self.long[self.pitch] if self.is_long else self.pitch


class LoudNote(Note):
    def __str__(self) -> str:
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, pitch: str = None, is_long: bool = False):
        if pitch is None:
            pitch = "до"
        super().__init__(pitch, is_long=is_long)


class NoteWithOctave(Note):
    def __init__(self, pitch: str, octave: str, is_long: bool = False):
        super().__init__(pitch, is_long=is_long)
        self.octave = octave

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.octave})"
