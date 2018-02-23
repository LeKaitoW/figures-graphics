import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from PyQt5.QtGui import *

import body
import part


class Figures(QWidget):
    def __init__(self, part, parent=None):
        super(Figures, self).__init__(parent)
        self.part = part
        self.setWindowTitle("Figures generator")
        # self.setFixedSize(640, 480)
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.save_layout = QHBoxLayout()
        self.save_layout.addStretch(1)
        self.save_button = QPushButton("Save")
        self.save_layout.addWidget(self.save_button)
        self.svg_painter = DisplayWidget()
        self.svg_painter.setMinimumSize(self.width() // 2, self.height() * 8 // 9)
        self.tabs = Tabs()
        self.h_layout.addWidget(self.tabs)
        self.h_layout.addWidget(self.svg_painter)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.save_layout)
        self.setLayout(self.v_layout)
        self.size = [self.width() // 2, self.height() * 8 // 9,
                     self.window().tabs.bodiesPage.elevation_slider.value() * 0.01]


class Tabs(QTabWidget):
    def __init__(self, parent=None):
        super(Tabs, self).__init__(parent)
        tab_names = ["Тела", "Полость", "Окно"]
        self.bodiesPage = BodiesTab(self)
        self.insertTab(0, self.bodiesPage, tab_names[0])
        self.hollowPage = HollowTab(self)
        self.insertTab(1, self.hollowPage, tab_names[1])
        self.setTabEnabled(1, False)
        self.insertTab(2, WindowTab(self), tab_names[2])


class DisplayWidget(QWidget):
    def __init__(self, parent=None):
        super(DisplayWidget, self).__init__(parent)
        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)
        self.paint()
        self.painter.end()

    def paint(self):
        self.painter.fillRect(0, 0, self.width(), self.height(), QColor(255, 255, 255))
        self.painter.drawRect(0, 0, self.width() - 1, self.height() - 1)
        self.painter.drawLine(0, self.height() * 2 // 3, self.width() - 1, self.height() * 2 // 3)
        self.window().part.redraw(self.painter, *self.window().size)


class BasicTab(QWidget):
    def __init__(self, parent=None):
        super(BasicTab, self).__init__(parent)
        self.figures_names = {"": None, "Пирамида": body.Pyramid, "Призма": body.Prism, "Сфера": body.Sphere,
                              "Цилиндр": body.Cylinder, "Конус": body.Cone}
        self.windows_one = ["Прямоугольник", "Треугольник", "Окружность"]
        self.windows_two = ["Прямоугольник + прямоугольник", "Треугольник + Прямоугольник"]
        self.windows_three = ["Прямоугольник + Прямоугольник + Прямоугольник"]
        self.places = ["Верх", "Низ", "Центр"]
        self.hollows = ["Цилиндр", "Сфера"]
        self.tab_layout = QVBoxLayout()


class BodiesTab(BasicTab):
    def __init__(self, parent=None):
        super(BodiesTab, self).__init__(parent)

        self.max_width = self.window().height() * 8 // 9 // 3
        self.up_group = QGroupBox("Верх:")
        self.up_layout = QVBoxLayout()
        self.up_figures_combo = QComboBox()
        self.up_figures_combo.addItems(self.figures_names.keys())
        self.up_figures_combo.activated[str].connect(
            lambda: self.figures_checks(self.max_width * self.up_slider.value() // 100,
                                        self.up_figures_combo.currentText(), self.up_group, 'set_up'))
        self.up_layout.addWidget(self.up_figures_combo)
        self.up_group.setLayout(self.up_layout)

        self.down_group = QGroupBox("Низ:")
        self.down_layout = QVBoxLayout()
        self.down_figures_combo = QComboBox()
        self.down_figures_combo.addItems(self.figures_names.keys())
        # TODO set text "Выберите фигуру"
        self.down_figures_combo.activated[str].connect(
            lambda: self.figures_checks(self.max_width * self.down_slider.value() // 100,
                                        self.down_figures_combo.currentText(), self.down_group, 'set_down'))
        self.down_layout.addWidget(self.down_figures_combo)
        self.down_group.setLayout(self.down_layout)

        self.size_group = QGroupBox("Размеры:")
        self.size_layout = QVBoxLayout()
        self.elevation_layout = QHBoxLayout()
        self.elevation_slider = QSlider(Qt.Horizontal, self)
        self.elevation_slider.setMinimum(0)
        self.elevation_slider.setMaximum(100)
        self.elevation_slider.setValue(50)
        self.size_layout.addWidget(QLabel("Соотношение высот:"))
        self.elevation_layout.addWidget(self.elevation_slider)
        self.elevation_value = QLineEdit(str(self.elevation_slider.value()))
        self.elevation_value.setMaxLength(3)
        self.elevation_layout.addWidget(self.elevation_value)
        self.size_layout.addLayout(self.elevation_layout)
        self.size_layout.addWidget(QLabel("Ширина верха:"))
        self.up_slider = QSlider(Qt.Horizontal, self)
        self.up_slider.setMinimum(0)
        self.up_slider.setMaximum(100)
        self.up_slider.setValue(50)
        self.up_value = QLineEdit(str(self.up_slider.value()))
        self.up_value.setMaxLength(3)
        self.size_layout.addWidget(self.up_slider)
        self.size_layout.addWidget(QLabel("Ширина низа:"))
        self.down_slider = QSlider(Qt.Horizontal, self)
        self.down_slider.setMinimum(0)
        self.down_slider.setMaximum(100)
        self.down_slider.setValue(50)
        self.down_value = QLineEdit(str(self.down_slider.value()))
        self.down_value.setMaxLength(3)
        self.size_layout.addWidget(self.down_slider)
        self.size_group.setLayout(self.size_layout)
        self.elevation_value.setFixedWidth(self.window().width() // 25)
        self.elevation_slider.valueChanged.connect(lambda: self.elevation(self.elevation_value, self.elevation_slider))
        self.elevation_slider.valueChanged.connect(lambda: self.elevation_change(self.elevation_slider))
        self.elevation_value.textChanged.connect(lambda: self.elevation(self.elevation_slider, self.elevation_value))
        self.elevation_value.setValidator(QIntValidator(0, 100))
        self.up_slider.valueChanged.connect(lambda: self.width_change(self.up_slider, self.window().part.up))
        self.down_slider.valueChanged.connect(lambda: self.width_change(self.down_slider, self.window().part.down))

        self.hole_check_box = QCheckBox("Наличие полости", self)
        self.hole_check_box.stateChanged.connect(self.change_hole_title)

        self.tab_layout.addWidget(self.up_group)
        self.tab_layout.addWidget(self.down_group)
        self.tab_layout.addWidget(self.size_group)
        self.tab_layout.addWidget(self.hole_check_box)
        self.setLayout(self.tab_layout)
        self.figures_checks(self.max_width * self.up_slider.value() // 100, self.up_figures_combo.currentText(),
                            self.up_group, 'set_up')
        self.figures_checks(self.max_width * self.down_slider.value() // 100, self.down_figures_combo.currentText(),
                            self.down_group, 'set_down')

    def figures_checks(self, width, text, widget, method):
        assert method in ['set_up', 'set_down']
        args = []
        for i in range(widget.layout().count() - 1):
            widget.layout().itemAt(1).widget().setParent(None)
        if text == "Конус":
            checkbox = QCheckBox()
            checkbox.setText("Усеченный")
            widget.layout().addWidget(checkbox)
            args.append(width)
        elif text == "Сфера":
            checkbox = QCheckBox("Полусфера")
            widget.layout().addWidget(checkbox)
            args.append(width)
        elif text == "Цилиндр":
            args.append(width)
        elif text == "Призма" or text == "Пирамида":
            corners = QSpinBox()
            corners.setRange(3, 6)
            widget.layout().addWidget(corners)
            args.extend((corners.value(), 100))
        else:
            pass
        if self.window():
            getattr(self.window().part, method)(self.figures_names.get(text)(*args))
            self.window().svg_painter.update()

    def change_hole_title(self, state):
        if state == Qt.Checked:
            window = self.window()
            window.tabs.setTabEnabled(1, True)
        else:
            self.window().tabs.setTabEnabled(1, False)

    def elevation(self, targetWidget, sourceWidget):
        if type(targetWidget) is QLineEdit and type(sourceWidget) is QSlider:
            targetWidget.setText(str(sourceWidget.value()))
        elif type(targetWidget) is QSlider and type(sourceWidget) is QLineEdit:
            if not sourceWidget.text():
                sourceWidget.setText('0')
            targetWidget.setValue(int(sourceWidget.text()))

    def elevation_change(self, widget):
        self.window().size[2] = widget.value() * 0.01
        self.window().svg_painter.update()

    def width_change(self, slider, body):
        body.set_width(self.max_width * slider.value() * 0.01)
        self.window().svg_painter.update()


class HollowTab(BasicTab):
    def __init__(self, parent=None):
        super(HollowTab, self).__init__(parent)

        self.hollow_shape_label = QLabel("Форма полости:", self)
        self.tab_layout.addWidget(self.hollow_shape_label)

        self.hollow_shape_combo = QComboBox(self)
        self.hollow_shape_combo.addItems(self.hollows)
        self.tab_layout.addWidget(self.hollow_shape_combo)

        self.hollow_place_label = QLabel("Расположение полости:", self)
        self.tab_layout.addWidget(self.hollow_place_label)

        self.hollow_place_combo = QComboBox(self)
        self.hollow_place_combo.addItems(self.places)
        self.tab_layout.addWidget(self.hollow_place_combo)

        self.setLayout(self.tab_layout)


class WindowTab(BasicTab):
    def __init__(self, parent=None):
        super(WindowTab, self).__init__(parent)
        self.windows_parts_num = QComboBox(self)
        self.windows_parts_num.addItems(["", "1", "2", "3"])
        self.tab_layout.addWidget(self.windows_parts_num)
        # windows_parts_num.activated[str].connect(self.chose_windows_parts)

        self.windows_parts = QComboBox(self)
        self.windows_parts.addItems([""])
        self.tab_layout.addWidget(self.windows_parts)

        self.window_place_combo = QComboBox(self)
        self.window_place_combo.addItems(self.places)
        self.tab_layout.addWidget(self.window_place_combo)

        self.tab_layout.addWidget(QLabel("Расположение окна:", self))
        self.tab_layout.addWidget(QLabel("Количество составляющих в окне:", self))
        self.tab_layout.addWidget(QLabel("Составляющие окна:"))
        self.setLayout(self.tab_layout)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def chose_windows_parts(self, state):
        self.windows_parts.clear()
        if state == "1":
            self.windows_parts.addItems(self.windows_one)
        if state == "2":
            self.windows_parts.addItems(self.windows_two)
        if state == "3":
            self.windows_parts.addItems(self.windows_three)

    def initUI(self):

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wizard = Figures(part.Part())
    wizard.show()
    sys.exit(app.exec_())
