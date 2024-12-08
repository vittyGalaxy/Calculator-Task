import sys
from gui.calculator import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from parser_lib import evaluate_expression
from root_calculator import RootCalculator


class GuiCalculator(QMainWindow):
    def __init__(self):
        super(GuiCalculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Roots
        self.root_calculator = RootCalculator()

        # Operations
        self.operations = {"+", "-", "*", "/"}
        self.number_insert = False

        # Equation
        self.equation = []
        self.fake_equation = []

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
        self.ui.btn_plus.clicked.connect(lambda: self.gui_op("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.gui_op("-"))
        self.ui.btn_mult.clicked.connect(lambda: self.gui_op("*"))
        self.ui.btn_div.clicked.connect(lambda: self.gui_op("/"))
        self.ui.btn_open_parenthesis.clicked.connect(lambda: self.gui_numbers("("))
        self.ui.btn_close_parenthesis.clicked.connect(lambda: self.gui_numbers(")"))
        self.ui.btn_comma.clicked.connect(lambda: self.gui_numbers(","))
        self.ui.btn_sqrt.clicked.connect(self.root_numbers)
        self.ui.btn_absolute.clicked.connect(self.exp_numbers)
        self.ui.btn_del.clicked.connect(self.del_numbers)
        self.ui.btn_CE.clicked.connect(self.ce_numbers)
        self.ui.btn_equal.clicked.connect(self.gui_equal)

    def reset_equation(self):
        self.fake_equation.clear()
        self.equation.clear()
        self.root_calculator.disable()
    
    def exp_numbers(self):
        self.equation.append("**")
        self.fake_equation.append("^")
        return self.ui.display.setText("".join(self.fake_equation))
    
    def root_numbers(self):
        print(self.equation)
        self.fake_equation.append("√")
        self.root_calculator.enable()
        if(self.equation[-1] not in self.operations) : 
            self.root_calculator.update_index(self.equation[-1])
        else:
            self.root_calculator.update_index(str(2))
        return self.ui.display.setText("".join(self.fake_equation))

    def ce_numbers(self):
        self.reset_equation()
        return self.ui.display.clear()

    def del_numbers(self):
        self.fake_equation = self.fake_equation[:-1]
        self.equation = self.equation[:-1]
        return self.ui.display.setText("".join(self.fake_equation))

    def gui_numbers(self, number):
        self.fake_equation.append(str(number))
        if(self.root_calculator.is_enabled()):
           self.equation = self.equation[:-1]
           self.root_calculator.update_radicand(str(number))
        else:
           self.equation.append(str(number))
        return self.ui.display.setText("".join(self.fake_equation))
    
    def gui_op(self, op):
        self.fake_equation.append(op)
        if(self.root_calculator.is_enabled()):
            self.equation.append(self.root_calculator.get_string())
            self.root_calculator.disable()
        self.equation.append(op)
        return self.ui.display.setText("".join(self.fake_equation))


    def gui_equal(self):
        if(self.root_calculator.is_enabled()):
            self.equation.append(self.root_calculator.get_string())
            self.root_calculator.disable()

        print(self.equation)
        result = evaluate_expression("".join(self.equation))
        self.fake_equation = list(str(result))
        self.equation = list(str(result))
        return self.ui.display.setText("".join(self.fake_equation))


def main():
    app = QApplication(sys.argv)
    window = GuiCalculator()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()