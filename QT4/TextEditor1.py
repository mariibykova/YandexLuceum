import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QPlainTextEdit,
)
from PyQt6.QtCore import QRect


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Notebook")
        self.setGeometry(100, 100, 600, 400)
        self.new_button = QPushButton("Создать новый", self)
        self.new_button.setGeometry(QRect(20, 20, 100, 30))
        self.save_button = QPushButton("Сохранить файл", self)
        self.save_button.setGeometry(QRect(20, 60, 100, 30))
        self.open_button = QPushButton("Открыть файл", self)
        self.open_button.setGeometry(QRect(20, 100, 100, 30))
        self.filename_edit = QLineEdit(self)
        self.filename_edit.setGeometry(QRect(140, 20, 200, 30))
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setGeometry(QRect(140, 60, 450, 330))
        self.new_button.clicked.connect(self.create_new)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def create_new(self):
        self.filename_edit.clear()
        self.text_edit.clear()

    def save_file(self):
        filename = self.filename_edit.text().strip()
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())

    def open_file(self):
        filename = self.filename_edit.text().strip()
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.text_edit.setPlainText(f.read())


def main():
    app = QApplication(sys.argv)
    window = Notebook()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
