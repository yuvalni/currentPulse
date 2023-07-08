# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(852, 797)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionconnect = QAction(MainWindow)
        self.actionconnect.setObjectName(u"actionconnect")
        self.actionDisconect = QAction(MainWindow)
        self.actionDisconect.setObjectName(u"actionDisconect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        self.groupBox.setFont(font)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.line_2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_9.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.SB_pulseMax = QDoubleSpinBox(self.groupBox)
        self.SB_pulseMax.setObjectName(u"SB_pulseMax")
        self.SB_pulseMax.setDecimals(4)
        self.SB_pulseMax.setMinimum(-9999.000000000000000)
        self.SB_pulseMax.setMaximum(99999.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.SB_pulseMax)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.SB_tbm = QDoubleSpinBox(self.groupBox)
        self.SB_tbm.setObjectName(u"SB_tbm")
        self.SB_tbm.setMaximum(99999.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.SB_tbm)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.SB_voltag_comp = QSpinBox(self.groupBox)
        self.SB_voltag_comp.setObjectName(u"SB_voltag_comp")
        self.SB_voltag_comp.setMaximum(999)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.SB_voltag_comp)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.line)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(89, 16777215))
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.label_5.setFont(font2)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_8)

        self.SP_measCurrent = QDoubleSpinBox(self.groupBox)
        self.SP_measCurrent.setObjectName(u"SP_measCurrent")
        self.SP_measCurrent.setDecimals(4)
        self.SP_measCurrent.setMinimum(-9999.000000000000000)
        self.SP_measCurrent.setMaximum(9999.000000000000000)
        self.SP_measCurrent.setValue(0.001000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.SP_measCurrent)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_7)

        self.SB_measAVG = QSpinBox(self.groupBox)
        self.SB_measAVG.setObjectName(u"SB_measAVG")
        self.SB_measAVG.setMaximum(9999)
        self.SB_measAVG.setValue(5)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.SB_measAVG)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_10)

        self.fileName = QLineEdit(self.groupBox)
        self.fileName.setObjectName(u"fileName")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.fileName)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(17, QFormLayout.SpanningRole, self.line_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(18, QFormLayout.SpanningRole, self.verticalSpacer)

        self.SB_pulseMin = QDoubleSpinBox(self.groupBox)
        self.SB_pulseMin.setObjectName(u"SB_pulseMin")
        self.SB_pulseMin.setDecimals(4)
        self.SB_pulseMin.setMinimum(-9999.000000000000000)
        self.SB_pulseMin.setMaximum(9999.000000000000000)
        self.SB_pulseMin.setValue(0.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.SB_pulseMin)

        self.SB_NPLC = QDoubleSpinBox(self.groupBox)
        self.SB_NPLC.setObjectName(u"SB_NPLC")
        self.SB_NPLC.setDecimals(4)
        self.SB_NPLC.setMaximum(9999.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.SB_NPLC)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_11)

        self.SB_waitBFmeas = QDoubleSpinBox(self.groupBox)
        self.SB_waitBFmeas.setObjectName(u"SB_waitBFmeas")
        self.SB_waitBFmeas.setMaximum(99999.000000000000000)
        self.SB_waitBFmeas.setValue(50.000000000000000)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.SB_waitBFmeas)

        self.KeithleyConnected = QRadioButton(self.groupBox)
        self.KeithleyConnected.setObjectName(u"KeithleyConnected")
        self.KeithleyConnected.setEnabled(False)
        self.KeithleyConnected.setStyleSheet(u"QRadioButton::indicator {\n"
"    width:                  20px;\n"
"    height:                 20px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(85, 255, 0);\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgb(255, 0, 0);\n"
"    border:                 2px solid black;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.KeithleyConnected)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)


        self.verticalLayout.addWidget(self.groupBox)

        self.PB_pulse = QPushButton(self.centralwidget)
        self.PB_pulse.setObjectName(u"PB_pulse")

        self.verticalLayout.addWidget(self.PB_pulse)

        self.PB_measureRes = QPushButton(self.centralwidget)
        self.PB_measureRes.setObjectName(u"PB_measureRes")

        self.verticalLayout.addWidget(self.PB_measureRes)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.resistancePlot = PlotWidget(self.centralwidget)
        self.resistancePlot.setObjectName(u"resistancePlot")
        self.resistancePlot.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resistancePlot.sizePolicy().hasHeightForWidth())
        self.resistancePlot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.resistancePlot, 2, 0, 1, 2)

        self.currentPlot = PlotWidget(self.centralwidget)
        self.currentPlot.setObjectName(u"currentPlot")
        sizePolicy2.setHeightForWidth(self.currentPlot.sizePolicy().hasHeightForWidth())
        self.currentPlot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.currentPlot, 0, 1, 1, 1)

        self.PB_cooldwon = QProgressBar(self.centralwidget)
        self.PB_cooldwon.setObjectName(u"PB_cooldwon")
        self.PB_cooldwon.setStyleSheet(u"")
        self.PB_cooldwon.setMaximum(100)
        self.PB_cooldwon.setValue(0)
        self.PB_cooldwon.setTextVisible(True)
        self.PB_cooldwon.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.PB_cooldwon, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 852, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menufile.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionconnect)
        self.menufile.addAction(self.actionDisconect)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Current pulse", None))
        self.actionconnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionDisconect.setText(QCoreApplication.translate("MainWindow", u"Disconect", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pulse settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pulse max", None))
        self.SB_pulseMax.setSuffix(QCoreApplication.translate("MainWindow", u" mA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pulse min", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NPLC", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"tbm", None))
        self.SB_tbm.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Voltage compliance", None))
        self.SB_voltag_comp.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Measure settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Measure Current", None))
        self.SP_measCurrent.setPrefix("")
        self.SP_measCurrent.setSuffix(QCoreApplication.translate("MainWindow", u" mA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AVG num.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.SB_pulseMin.setSuffix(QCoreApplication.translate("MainWindow", u" mA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wait before measure", None))
        self.SB_waitBFmeas.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.KeithleyConnected.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Keithley status", None))
        self.PB_pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.PB_measureRes.setText(QCoreApplication.translate("MainWindow", u"Measure resistance", None))
        self.PB_cooldwon.setFormat(QCoreApplication.translate("MainWindow", u"Cooldown", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

