N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

dict = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и",
}


class Note:
    def __init__(self, note, is_long=False):
        self.N = 7
        self.PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
        self.INTERVALS = [
            "прима",
            "секунда",
            "терция",
            "кварта",
            "квинта",
            "секста",
            "септима",
        ]
        self.note = note
        self.dict = {
            "до": "до-о",
            "ре": "ре-э",
            "ми": "ми-и",
            "фа": "фа-а",
            "соль": "со-оль",
            "ля": "ля-а",
            "си": "си-и",
        }
        self.long = is_long

    def __str__(self):
        if self.long:
            return self.dict[self.note]
        else:
            return self.note

    def get_index(self):
        return self.PITCHES.index(self.note)

    def __eq__(self, other):
        return self.note == other.note

    def __ne__(self, other):
        return self.note != other.note

    def __lt__(self, other):
        return self.PITCHES.index(self.note) < other.PITCHES.index(other.note)

    def __gt__(self, other):
        return self.PITCHES.index(self.note) > other.PITCHES.index(other.note)

    def __le__(self, other):
        return self.PITCHES.index(self.note) <= other.PITCHES.index(other.note)

    def __ge__(self, other):
        return self.PITCHES.index(self.note) >= other.PITCHES.index(other.note)

    def __lshift__(self, other):
        index = self.PITCHES.index(self.note)
        for _ in range(other):
            if index == 0:
                index = len(self.PITCHES) - 1
            else:
                index -= 1
        return Note(self.PITCHES[index], is_long=self.long)

    def __rshift__(self, other):
        index = self.PITCHES.index(self.note)
        for _ in range(other):
            if index == len(self.PITCHES) - 1:
                index = 0
            else:
                index += 1
        return Note(self.PITCHES[index], is_long=self.long)

    def get_interval(self, other):
        return self.INTERVALS[
            abs(self.PITCHES.index(self.note) - other.PITCHES.index(other.note))
        ]


class Melody:
    def __init__(self, PITCHES=None):
        if PITCHES is None:
            PITCHES = []
        self.PITCHES = PITCHES

    def __str__(self):
        return ", ".join([str(i) for i in self.PITCHES]).capitalize()

    def append(self, note):
        self.PITCHES.append(note)

    def replace_last(self, note):
        if len(self.PITCHES) > 0:
            self.PITCHES = self.PITCHES[:-1] + [note]
            return None
        self.PITCHES = [note]

    def remove_last(self):
        if len(self.PITCHES) > 0:
            self.PITCHES = self.PITCHES[:-1]

    def clear(self):
        self.PITCHES.clear()

    def __len__(self):
        return len(self.PITCHES)

    def __rshift__(self, other):
        output = []
        for k in self.PITCHES:
            if k.get_index() + other > 6:
                return Melody(self.PITCHES)
        for i in self.PITCHES:
            output.append(i >> other)
        return Melody(output)

    def __lshift__(self, other):
        output = []
        for k in self.PITCHES:
            if k.get_index() - other < 0:
                return Melody(self.PITCHES)
        for i in self.PITCHES:
            output.append(i << other)
        return Melody(output)


class LoudNote(Note):
    def __init__(self, note, is_long=False):
        super().__init__(note, is_long=is_long)

    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, note="до", is_long=False):
        super().__init__(note, is_long=is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        self.octave = octave
        super().__init__(note, is_long=is_long)

    def __str__(self):
        return f"{super().__str__()} ({self.octave})"
