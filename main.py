import sys
from gui.calculator import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class GuiCalculator(QMainWindow):
    def __init__(self):
        super(GuiCalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Equation
        self.equation = ""

        # GUI
        self.ui.btn_0.clicked.connect(lambda: self.gui_numbers(0))
        self.ui.btn_1.clicked.connect(lambda: self.gui_numbers(1))
        self.ui.btn_2.clicked.connect(lambda: self.gui_numbers(2))
        self.ui.btn_3.clicked.connect(lambda: self.gui_numbers(3))
        self.ui.btn_4.clicked.connect(lambda: self.gui_numbers(4))
        self.ui.btn_5.clicked.connect(lambda: self.gui_numbers(5))
        self.ui.btn_6.clicked.connect(lambda: self.gui_numbers(6))
        self.ui.btn_7.clicked.connect(lambda: self.gui_numbers(7))
        self.ui.btn_8.clicked.connect(lambda: self.gui_numbers(8))
        self.ui.btn_9.clicked.connect(lambda: self.gui_numbers(9))
        self.ui.btn_plus.clicked.connect(lambda: self.gui_numbers("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.gui_numbers("-"))
        self.ui.btn_mult.clicked.connect(lambda: self.gui_numbers("*"))
        self.ui.btn_div.clicked.connect(lambda: self.gui_numbers("/"))
        self.ui.btn_open_parenthesis.clicked.connect(lambda: self.gui_numbers("("))
        self.ui.btn_close_parenthesis.clicked.connect(lambda: self.gui_numbers(")"))
        self.ui.btn_comma.clicked.connect(lambda: self.gui_numbers(","))
        self.ui.btn_sqrt.clicked.connect(lambda: self.gui_numbers(","))
        self.ui.btn_equal.clicked.connect(self.gui_equal)

    def gui_numbers(self, number):
        self.equation = self.equation + str(number)
        return self.ui.display.setText(self.equation)

    def gui_equal(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = GuiCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
