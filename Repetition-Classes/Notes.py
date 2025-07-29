class Note:
    notes = {"до", "ре", "ми", "фа", "соль", "ля", "си"}

    def __init__(self, pitch: str):
        if pitch not in self.notes:
            raise ValueError(f"Недопустимая высота ноты: {pitch}")
        self.pitch = pitch

    def play(self):
        print(self.pitch)