import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QCalendarWidget,
    QTimeEdit,
    QLineEdit,
    QPushButton,
    QListWidget,
)
from PyQt6.QtCore import QDateTime


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 400)
        self.setWindowTitle("Простой ежедневник")

        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.setGeometry(20, 20, 250, 200)
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setGeometry(20, 230, 100, 30)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Название события")
        self.lineEdit.setGeometry(130, 230, 160, 30)
        self.addEventBtn = QPushButton("Добавить", self)
        self.addEventBtn.setGeometry(300, 230, 100, 30)
        self.addEventBtn.clicked.connect(self.add_event)
        self.eventList = QListWidget(self)
        self.eventList.setGeometry(20, 270, 460, 110)

        self.events = []

    def add_event(self):
        name = self.lineEdit.text().strip()
        if not name:
            return
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        dt = QDateTime(date, time)
        self.events.append((dt, name))
        self.events.sort(key=lambda x: x[0])
        self.eventList.clear()
        for e_dt, e_name in self.events:
            item_text = f"{e_dt.toString('yyyy-MM-dd HH:mm:ss')} - {e_name}"
            self.eventList.addItem(item_text)
        self.lineEdit.clear()
        self.lineEdit.setFocus()


def main():
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
