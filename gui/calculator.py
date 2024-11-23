# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 300)
        MainWindow.setMinimumSize(QSize(566, 300))
        MainWindow.setMaximumSize(QSize(566, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 3, 511, 252))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_9 = QFrame(self.gridLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 3, 4, 1, 1)

        self.btn_mult = QPushButton(self.gridLayoutWidget)
        self.btn_mult.setObjectName(u"btn_mult")

        self.gridLayout.addWidget(self.btn_mult, 5, 7, 1, 1)

        self.btn_sub = QPushButton(self.gridLayoutWidget)
        self.btn_sub.setObjectName(u"btn_sub")

        self.gridLayout.addWidget(self.btn_sub, 7, 7, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 5, 3, 1, 1)

        self.btn_sqrt = QPushButton(self.gridLayoutWidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")

        self.gridLayout.addWidget(self.btn_sqrt, 3, 1, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 5, 5, 1, 1)

        self.btn_div = QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName(u"btn_div")

        self.gridLayout.addWidget(self.btn_div, 3, 7, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 7, 3, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 9, 3, 1, 1)

        self.btn_absolute = QPushButton(self.gridLayoutWidget)
        self.btn_absolute.setObjectName(u"btn_absolute")

        self.gridLayout.addWidget(self.btn_absolute, 11, 1, 1, 1)

        self.line_32 = QFrame(self.gridLayoutWidget)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_32, 13, 1, 1, 1)

        self.line_29 = QFrame(self.gridLayoutWidget)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.HLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_29, 10, 3, 1, 1)

        self.line_34 = QFrame(self.gridLayoutWidget)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.HLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_34, 13, 5, 1, 1)

        self.line_26 = QFrame(self.gridLayoutWidget)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_26, 8, 5, 1, 1)

        self.line_27 = QFrame(self.gridLayoutWidget)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_27, 8, 7, 1, 1)

        self.line_22 = QFrame(self.gridLayoutWidget)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_22, 4, 5, 1, 1)

        self.line_21 = QFrame(self.gridLayoutWidget)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_21, 4, 3, 1, 1)

        self.line_18 = QFrame(self.gridLayoutWidget)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_18, 2, 5, 1, 1)

        self.line_20 = QFrame(self.gridLayoutWidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_20, 4, 1, 1, 1)

        self.line_16 = QFrame(self.gridLayoutWidget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_16, 2, 1, 1, 1)

        self.line_28 = QFrame(self.gridLayoutWidget)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_28, 10, 1, 1, 1)

        self.line_24 = QFrame(self.gridLayoutWidget)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_24, 8, 1, 1, 1)

        self.line_15 = QFrame(self.gridLayoutWidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_15, 11, 2, 1, 1)

        self.line_48 = QFrame(self.gridLayoutWidget)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.Shape.HLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_48, 6, 7, 1, 1)

        self.line_49 = QFrame(self.gridLayoutWidget)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_49, 1, 0, 1, 1)

        self.line_47 = QFrame(self.gridLayoutWidget)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_47, 6, 5, 1, 1)

        self.line_45 = QFrame(self.gridLayoutWidget)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.Shape.HLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_45, 6, 1, 1, 1)

        self.btn_close_parenthesis = QPushButton(self.gridLayoutWidget)
        self.btn_close_parenthesis.setObjectName(u"btn_close_parenthesis")

        self.gridLayout.addWidget(self.btn_close_parenthesis, 3, 5, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 7, 5, 1, 1)

        self.btn_open_parenthesis = QPushButton(self.gridLayoutWidget)
        self.btn_open_parenthesis.setObjectName(u"btn_open_parenthesis")

        self.gridLayout.addWidget(self.btn_open_parenthesis, 3, 3, 1, 1)

        self.line_17 = QFrame(self.gridLayoutWidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_17, 2, 3, 1, 1)

        self.line_23 = QFrame(self.gridLayoutWidget)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_23, 4, 7, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 7, 1, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")

        self.gridLayout.addWidget(self.btn_0, 11, 3, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 5, 1, 1, 1)

        self.btn_comma = QPushButton(self.gridLayoutWidget)
        self.btn_comma.setObjectName(u"btn_comma")

        self.gridLayout.addWidget(self.btn_comma, 11, 5, 1, 1)

        self.btn_equal = QPushButton(self.gridLayoutWidget)
        self.btn_equal.setObjectName(u"btn_equal")

        self.gridLayout.addWidget(self.btn_equal, 11, 7, 1, 1)

        self.line_13 = QFrame(self.gridLayoutWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_13, 5, 2, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 9, 5, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 9, 1, 1, 1)

        self.line_11 = QFrame(self.gridLayoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_11, 9, 2, 1, 1)

        self.btn_plus = QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName(u"btn_plus")

        self.gridLayout.addWidget(self.btn_plus, 9, 7, 1, 1)

        self.display = QLabel(self.gridLayoutWidget)
        self.display.setObjectName(u"display")

        self.gridLayout.addWidget(self.display, 1, 1, 1, 7)

        self.line_14 = QFrame(self.gridLayoutWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_14, 3, 2, 1, 1)

        self.line_12 = QFrame(self.gridLayoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_12, 7, 2, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 7, 6, 1, 1)

        self.line_5 = QFrame(self.gridLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 11, 6, 1, 1)

        self.line_8 = QFrame(self.gridLayoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_8, 5, 4, 1, 1)

        self.line_10 = QFrame(self.gridLayoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 11, 4, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 9, 6, 1, 1)

        self.line_31 = QFrame(self.gridLayoutWidget)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.HLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_31, 10, 7, 1, 1)

        self.line_44 = QFrame(self.gridLayoutWidget)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.Shape.VLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_44, 11, 8, 1, 1)

        self.line_50 = QFrame(self.gridLayoutWidget)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_50, 1, 8, 1, 1)

        self.line_38 = QFrame(self.gridLayoutWidget)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_38, 9, 0, 1, 1)

        self.line_43 = QFrame(self.gridLayoutWidget)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_43, 9, 8, 1, 1)

        self.line_51 = QFrame(self.gridLayoutWidget)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_51, 0, 1, 1, 7)

        self.line_35 = QFrame(self.gridLayoutWidget)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.HLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_35, 13, 7, 1, 1)

        self.line_37 = QFrame(self.gridLayoutWidget)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_37, 7, 0, 1, 1)

        self.line_39 = QFrame(self.gridLayoutWidget)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_39, 11, 0, 1, 1)

        self.line_30 = QFrame(self.gridLayoutWidget)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.HLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_30, 10, 5, 1, 1)

        self.line_42 = QFrame(self.gridLayoutWidget)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_42, 7, 8, 1, 1)

        self.line_33 = QFrame(self.gridLayoutWidget)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_33, 13, 3, 1, 1)

        self.line_36 = QFrame(self.gridLayoutWidget)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_36, 5, 0, 1, 1)

        self.line_40 = QFrame(self.gridLayoutWidget)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_40, 3, 8, 1, 1)

        self.line_41 = QFrame(self.gridLayoutWidget)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_41, 5, 8, 1, 1)

        self.line_25 = QFrame(self.gridLayoutWidget)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_25, 8, 3, 1, 1)

        self.line_7 = QFrame(self.gridLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 7, 4, 1, 1)

        self.line_19 = QFrame(self.gridLayoutWidget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_19, 2, 7, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 6, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 9, 4, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 6, 1, 1)

        self.line_46 = QFrame(self.gridLayoutWidget)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_46, 6, 3, 1, 1)

        self.btn_del = QPushButton(self.gridLayoutWidget)
        self.btn_del.setObjectName(u"btn_del")

        self.gridLayout.addWidget(self.btn_del, 12, 3, 1, 1)

        self.btn_CE = QPushButton(self.gridLayoutWidget)
        self.btn_CE.setObjectName(u"btn_CE")

        self.gridLayout.addWidget(self.btn_CE, 12, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 566, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_mult.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"n\u221ax", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_absolute.setText(QCoreApplication.translate("MainWindow", u"x^n", None))
        self.btn_close_parenthesis.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_open_parenthesis.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_comma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.display.setText(QCoreApplication.translate("MainWindow", u"display", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"del", None))
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"C.E.", None))
    # retranslateUi

