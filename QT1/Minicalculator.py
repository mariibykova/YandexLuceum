import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Миникалькулятор")
        self.setGeometry(300, 300, 400, 400)
        self.number_1 = QLineEdit(self)

        self.number_2 = QLineEdit(self)
        self.calculate_button = QPushButton("->", self)
        self.result_sum = QLCDNumber(self)
        self.result_sub = QLCDNumber(self)
        self.result_mul = QLCDNumber(self)
        self.result_div = QLCDNumber(self)
        self.calculate_button.clicked.connect(self.on_calculate_button_clicked)

    def on_calculate_button_clicked(self):
        try:
            num1 = int(self.number_1.text())
            num2 = int(self.number_2.text())
            sum_result = num1 + num2
            sub_result = num1 - num2
            mul_result = num1 * num2
            div_result = "Error" if num2 == 0 else round(num1 / num2, 3)
            self.result_sum.display(sum_result)
            self.result_sub.display(sub_result)
            self.result_mul.display(mul_result)
            if div_result == "Error":
                self.result_div.display("Error")
            else:
                self.result_div.display(div_result)

        except ValueError:
            self.result_sum.display("Error")
            self.result_sub.display("Error")
            self.result_mul.display("Error")
            self.result_div.display("Error")


def main():
    app = QApplication(sys.argv)
    window = MiniCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
