import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser
from PyQt6.QtCore import QRect


class Suffle(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Suffle")
        self.setGeometry(100, 100, 600, 400)
        self.button = QPushButton("Shuffle", self)
        self.button.setGeometry(QRect(20, 20, 80, 30))
        self.text_field = QTextBrowser(self)
        self.text_field.setGeometry(QRect(120, 20, 450, 350))
        self.button.clicked.connect(self.shuffle_lines)

    def shuffle_lines(self):
        try:
            with open("lines.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.text_field.setText("Файл lines.txt не найден!")
            return

        even_lines = []
        odd_lines = []
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:
                even_lines.append(line.strip())
            else:
                odd_lines.append(line.strip())
        combined = even_lines + odd_lines
        self.text_field.setText("\n".join(combined))


def main():
    app = QApplication(sys.argv)
    window = Suffle()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
