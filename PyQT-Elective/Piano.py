import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
import pygame


class PianoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initSounds()

    def initUI(self):
        self.setWindowTitle("Фортепиано")
        self.setGeometry(100, 100, 600, 200)
        self.notes = ["C", "D", "E", "F", "G", "A", "B"]
        self.buttons = []
        layout = QHBoxLayout()
        for note in self.notes:
            button = QPushButton(note, self)
            button.clicked.connect(self.playNote)
            layout.addWidget(button)
            self.buttons.append(button)
        self.setLayout(layout)

    def initSounds(self):
        pygame.mixer.init()
        self.sounds = {
            note: pygame.mixer.Sound(f"sounds/{note}.wav") for note in self.notes
        }

    def playNote(self):
        note = self.sender().text()
        self.sounds[note].play()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.sounds["C"].play()
        elif key == Qt.Key_S:
            self.sounds["D"].play()
        elif key == Qt.Key_D:
            self.sounds["E"].play()
        elif key == Qt.Key_F:
            self.sounds["F"].play()
        elif key == Qt.Key_G:
            self.sounds["G"].play()
        elif key == Qt.Key_H:
            self.sounds["A"].play()
        elif key == Qt.Key_J:
            self.sounds["B"].play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    piano = PianoApp()
    piano.show()
    sys.exit(app.exec_())
