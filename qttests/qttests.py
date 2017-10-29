import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QCheckBox
from PyQt5.QtCore import QCoreApplication, Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def up_figures_sphere(self, text):
        if (str(self.up_figures_combo.currentText()) == str(self.figures_names[2])):
            self.sphere_check_box.show()
        else:
            self.sphere_check_box.hide()

    def change_hole_title(self, state):
        if (state == Qt.Checked):
            self.hole_place_combo.show()
            self.hole_shape_combo.show()
            self.hole_shape_label.show()
            self.hole_place_label.show()
        else:
            self.hole_place_combo.hide()
            self.hole_shape_combo.hide()
            self.hole_shape_label.hide()
            self.hole_place_label.hide()


    def initUI(self):

        self.setFixedSize(500, 400)
        self.setWindowTitle('Icon')

        self.figures_names = ["Пирамида", "Призма", "Сфера", "Цилиндр", "Конус"]
        places = ["Верх", "Низ", "Центр"]

        self.sphere_check_box = QCheckBox("Полусфера", self)
        self.sphere_check_box.move(150, 50)
        self.sphere_check_box.hide()

        self.up_figures_combo = QComboBox(self)
        self.up_figures_combo.addItems(self.figures_names)
        self.up_figures_combo.move(50, 50)
        self.up_figures_combo.activated[str].connect(self.up_figures_sphere)

        down_figures_combo = QComboBox(self)
        down_figures_combo.addItems(self.figures_names)
        down_figures_combo.move(50, 100)

        self.hole_place_combo = QComboBox(self)
        self.hole_place_combo.addItems(places)
        self.hole_place_combo.move(50, 280)
        self.hole_place_combo.hide()

        self.hole_shape_combo = QComboBox(self)
        self.hole_shape_combo.addItems(["Цилиндр", "Сфера"])
        self.hole_shape_combo.move(50, 230)
        self.hole_shape_combo.hide()

        window_place_combo = QComboBox(self)
        window_place_combo.addItems(places)
        window_place_combo.move(50, 150)

        self.hole_check_box = QCheckBox("Наличие полости", self)
        self.hole_check_box.move(50, 180)
        self.hole_check_box.stateChanged.connect(self.change_hole_title)

        up_label = QLabel("Верх", self)
        up_label.move(50, 30)

        self.down_label = QLabel("Низ", self)
        self.down_label.move(50, 80)

        self.hole_place_label = QLabel("Расположение полости", self)
        self.hole_place_label.move(50, 260)
        self.hole_place_label.hide()

        self.hole_shape_label = QLabel("Форма полости", self)
        self.hole_shape_label.move(50, 210)
        self.hole_shape_label.hide()

        window_label = QLabel("Расположение окна", self)
        window_label.move(50, 130)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())