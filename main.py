import sys
from gui.calculator import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from parser_lib import evaluate_expression


class GuiCalculator(QMainWindow):
    def __init__(self):
        super(GuiCalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Equation
        # self.equation = ""
        self.equation = []
        self.rad = []
        self.fake_equation = ""

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
        self.ui.btn_sqrt.clicked.connect(lambda: self.exp_numbers("√", True))
        self.ui.btn_exponent.clicked.connect(lambda: self.exp_numbers("^", False))
        self.ui.btn_del.clicked.connect(self.del_numbers)
        self.ui.btn_CE.clicked.connect(self.ce_numbers)
        self.ui.btn_equal.clicked.connect(self.gui_equal)

    # def sq_numbers(self):
    #     self.equation.append(number)
    #     self.fake_equation = self.fake_equation + str(number)
    #     return self.ui.display.setText(self.fake_equation)

    def exp_numbers(self, symbol, flag):
        self.equation.append("**")
        if (flag):
            self.equation.append(f" / {self.rad[0]} ")

        self.fake_equation = self.fake_equation + symbol
        return self.ui.display.setText(self.fake_equation)

    def ce_numbers(self):
        # self.equation = ""
        self.equation = []
        self.fake_equation = ""
        return self.ui.display.setText(self.fake_equation)

    def del_numbers(self):
        # self.equation.
        self.fake_equation = self.fake_equation[:-1]
        return self.ui.display.setText(self.fake_equation)

    def gui_numbers(self, number):
        self.equation.append(str(number))
        self.rad.append(str(number))
        if (number == "+" or number == "-" or number == "*" or number == "/"):
            self.rad = self.rad[:-2]
        self.fake_equation = self.fake_equation + str(number)
        return self.ui.display.setText(self.fake_equation)

    def gui_equal(self):
        print(self.equation)
        result = evaluate_expression("".join(self.equation))
        self.fake_equation = str(result)
        self.ui.display.setText(self.fake_equation)


def main():
    app = QApplication(sys.argv)
    window = GuiCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
