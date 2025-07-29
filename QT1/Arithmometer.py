import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class Arifmometr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(430, 60)
        self.setWindowTitle("Арифмометр")
        self.first_value = QLineEdit("0", self)
        self.first_value.setGeometry(10, 15, 80, 30)

        self.second_value = QLineEdit("0", self)
        self.second_value.setGeometry(250, 15, 80, 30)

        self.result = QLineEdit("0", self)
        self.result.setGeometry(340, 15, 80, 30)
        self.result.setReadOnly(True)
        self.result.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.add_button = QPushButton("+", self)
        self.add_button.setGeometry(100, 15, 40, 30)

        self.substract_button = QPushButton("-", self)
        self.substract_button.setGeometry(150, 15, 40, 30)

        self.multiply_button = QPushButton("*", self)
        self.multiply_button.setGeometry(200, 15, 40, 30)
        self.add_button.clicked.connect(self.on_add_clicked)
        self.substract_button.clicked.connect(self.on_sub_clicked)
        self.multiply_button.clicked.connect(self.on_mul_clicked)

    def on_add_clicked(self):
        self.calculate(lambda x, y: x + y)

    def on_sub_clicked(self):
        self.calculate(lambda x, y: x - y)

    def on_mul_clicked(self):
        self.calculate(lambda x, y: x * y)

    def calculate(self, operation):
        try:
            a = int(self.first_value.text())
            b = int(self.second_value.text())
            res = operation(a, b)
            self.result.setText(str(res))
        except ValueError:
            self.result.setText("Error")


def main():
    app = QApplication(sys.argv)
    window = Arifmometr()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
