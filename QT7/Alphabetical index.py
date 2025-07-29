import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1120</width>
    <height>586</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1120</width>
    <height>0</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1120</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>А</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Б</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>В</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Г</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Д</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Е</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ё</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ж</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_9">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>З</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_10">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>И</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_11">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Й</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_12">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>К</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_13">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Л</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_14">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>М</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_15">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Н</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_16">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>О</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_17">
    <property name="geometry">
     <rect>
      <x>590</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>П</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_18">
    <property name="geometry">
     <rect>
      <x>630</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Р</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_19">
    <property name="geometry">
     <rect>
      <x>660</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>С</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_20">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Т</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_21">
    <property name="geometry">
     <rect>
      <x>720</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>У</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_22">
    <property name="geometry">
     <rect>
      <x>750</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ф</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_23">
    <property name="geometry">
     <rect>
      <x>780</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Х</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_24">
    <property name="geometry">
     <rect>
      <x>810</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ц</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_25">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ч</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_26">
    <property name="geometry">
     <rect>
      <x>880</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ш</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_27">
    <property name="geometry">
     <rect>
      <x>910</x>
      <y>0</y>
      <width>41</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Щ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_28">
    <property name="geometry">
     <rect>
      <x>950</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ь</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_29">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_30">
    <property name="geometry">
     <rect>
      <x>1010</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ъ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_31">
    <property name="geometry">
     <rect>
      <x>1040</x>
      <y>0</y>
      <width>21</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Э</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_32">
    <property name="geometry">
     <rect>
      <x>1060</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Ю</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_33">
    <property name="geometry">
     <rect>
      <x>1090</x>
      <y>0</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Я</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>50</y>
      <width>1120</width>
      <height>481</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1120</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.buttons = [
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5,
            self.pushButton_6,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9,
            self.pushButton_10,
            self.pushButton_11,
            self.pushButton_12,
            self.pushButton_13,
            self.pushButton_14,
            self.pushButton_15,
            self.pushButton_16,
            self.pushButton_17,
            self.pushButton_18,
            self.pushButton_19,
            self.pushButton_20,
            self.pushButton_21,
            self.pushButton_22,
            self.pushButton_23,
            self.pushButton_24,
            self.pushButton_25,
            self.pushButton_26,
            self.pushButton_27,
            self.pushButton_28,
            self.pushButton_29,
            self.pushButton_30,
            self.pushButton_31,
            self.pushButton_32,
            self.pushButton_33
        ]

        for i in range(len(self.buttons)):
            self.buttons[i].clicked.connect(self.act)

    def act(self):
        # Подключение к БД
        con = sqlite3.connect('films_db.sqlite')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        res = cur.execute("""SELECT * FROM films WHERE title LIKE ?""",
                          (self.sender().text() + '%',)).fetchall()
        con.close()
        if res:
            self.statusbar.showMessage(f"Нашлось {len(res)} записей")
        else:
            self.statusbar.showMessage(f"К сожалению, ничего не нашлось")

        # Заполним размеры таблицы
        header_labels = ['ID', 'Название', 'Год', 'Жанр', 'Продолжительность']  # Замените на ваши заголовки
        self.tableWidget.setColumnCount(len(header_labels))  # Установите количество столбцов
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        self.tableWidget.setRowCount(len(res))
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())