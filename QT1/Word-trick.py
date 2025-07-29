import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Фокус со словами")

        self.first_value = QLineEdit(self)
        self.first_value.move(20, 130)
        self.second_value = QLineEdit(self)
        self.second_value.move(160, 130)

        self.trick_button = QPushButton("->", self)
        self.trick_button.clicked.connect(self.on_trick_button_clicked)
        self.trick_button.move(100, 130)

    def on_trick_button_clicked(self):
        if self.trick_button.text() == "->":
            self.second_value.setText(self.first_value.text())
            self.first_value.clear()
            self.trick_button.setText("<-")
        else:
            self.first_value.setText(self.second_value.text())
            self.second_value.clear()
            self.trick_button.setText("->")


def main():

    app = QApplication(sys.argv)

    window = WordTrick()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
