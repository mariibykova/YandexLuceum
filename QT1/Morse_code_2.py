import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morse Code")
        self.setGeometry(100, 100, 600, 300)
        self.morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        self.result = QLineEdit(self)
        self.result.setObjectName(
            "result"
        )  # чтобы соответствовать условию, имя поля result
        self.result.setGeometry(50, 20, 500, 30)
        self.alphabet_buttons = {}

        x_start, y_start = 50, 70
        button_width, button_height = 40, 40
        spacing = 10
        columns = 10
        x_current, y_current = x_start, y_start

        for index, letter in enumerate(self.morse_dict.keys()):
            button = QPushButton(letter.upper(), self)
            button.setGeometry(x_current, y_current, button_width, button_height)
            self.alphabet_buttons[letter] = button
            button.clicked.connect(lambda _, kkk=letter: self.append_morse(kkk))

            if (index + 1) % columns == 0:
                x_current = x_start
                y_current += button_height + spacing
            else:
                x_current += button_width + spacing

    def append_morse(self, letter: str):
        self.result.insert(self.morse_dict[letter])


def main():
    app = QApplication(sys.argv)
    window = MorseCode()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
