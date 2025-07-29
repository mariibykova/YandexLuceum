import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Вычисление выражений")

        self.first_value = QLineEdit(self)
        self.first_value.move(20, 130)

        self.second_value = QLineEdit(self)
        self.second_value.move(260, 130)

        self.trick_button = QPushButton("->", self)
        self.second_value.move(200, 130)

        self.trick_button.clicked.connect(self.on_trick_button_clicked)

    def on_trick_button_clicked(self):

        expr = self.first_value.text()
        try:
            result = eval(expr)
            self.second_value.setText(str(result))
        except Exception:
            self.second_value.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Evaluator()
    window.show()
    sys.exit(app.exec())
