# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 650)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStatusTip("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(590, 370, 75, 23))
        self.startButton.setObjectName("startButton")
        self.timeDiv_dial = QtWidgets.QDial(self.centralwidget)
        self.timeDiv_dial.setGeometry(QtCore.QRect(500, 430, 50, 64))
        self.timeDiv_dial.setMaximum(9)
        self.timeDiv_dial.setProperty("value", 4)
        self.timeDiv_dial.setInvertedAppearance(False)
        self.timeDiv_dial.setWrapping(False)
        self.timeDiv_dial.setNotchesVisible(True)
        self.timeDiv_dial.setObjectName("timeDiv_dial")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 410, 47, 13))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 510, 161, 111))
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.trigger_edge = QtWidgets.QComboBox(self.groupBox)
        self.trigger_edge.setGeometry(QtCore.QRect(70, 80, 81, 22))
        self.trigger_edge.setObjectName("trigger_edge")
        self.trigger_edge.addItem("")
        self.trigger_edge.addItem("")
        self.trigger_source = QtWidgets.QComboBox(self.groupBox)
        self.trigger_source.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.trigger_source.setObjectName("trigger_source")
        self.trigger_source.addItem("")
        self.trigger_source.addItem("")
        self.trigger_source.addItem("")
        self.trigger_source.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.tirgger_level_dial = QtWidgets.QDial(self.groupBox)
        self.tirgger_level_dial.setGeometry(QtCore.QRect(10, 40, 50, 64))
        self.tirgger_level_dial.setMaximum(8)
        self.tirgger_level_dial.setWrapping(True)
        self.tirgger_level_dial.setNotchesVisible(True)
        self.tirgger_level_dial.setObjectName("tirgger_level_dial")
        self.ch1_vDiv_dial = QtWidgets.QDial(self.centralwidget)
        self.ch1_vDiv_dial.setGeometry(QtCore.QRect(10, 530, 50, 64))
        self.ch1_vDiv_dial.setMaximum(5)
        self.ch1_vDiv_dial.setPageStep(1)
        self.ch1_vDiv_dial.setProperty("value", 3)
        self.ch1_vDiv_dial.setWrapping(False)
        self.ch1_vDiv_dial.setNotchesVisible(True)
        self.ch1_vDiv_dial.setObjectName("ch1_vDiv_dial")
        self.ch1_vertical_dial = QtWidgets.QDial(self.centralwidget)
        self.ch1_vertical_dial.setGeometry(QtCore.QRect(10, 410, 50, 64))
        self.ch1_vertical_dial.setMaximum(8)
        self.ch1_vertical_dial.setPageStep(1)
        self.ch1_vertical_dial.setWrapping(True)
        self.ch1_vertical_dial.setNotchTarget(3.7)
        self.ch1_vertical_dial.setNotchesVisible(True)
        self.ch1_vertical_dial.setObjectName("ch1_vertical_dial")
        self.ch1_coupling = QtWidgets.QComboBox(self.centralwidget)
        self.ch1_coupling.setGeometry(QtCore.QRect(10, 620, 51, 22))
        self.ch1_coupling.setObjectName("ch1_coupling")
        self.ch1_coupling.addItem("")
        self.ch1_coupling.addItem("")
        self.ch1_coupling.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 520, 47, 13))
        self.label_6.setObjectName("label_6")
        self.ch1_enable_button = QtWidgets.QPushButton(self.centralwidget)
        self.ch1_enable_button.setGeometry(QtCore.QRect(0, 480, 75, 23))
        self.ch1_enable_button.setObjectName("ch1_enable_button")
        self.ch2_vDiv_dial = QtWidgets.QDial(self.centralwidget)
        self.ch2_vDiv_dial.setGeometry(QtCore.QRect(130, 530, 50, 64))
        self.ch2_vDiv_dial.setMaximum(5)
        self.ch2_vDiv_dial.setPageStep(1)
        self.ch2_vDiv_dial.setProperty("value", 3)
        self.ch2_vDiv_dial.setWrapping(False)
        self.ch2_vDiv_dial.setNotchesVisible(True)
        self.ch2_vDiv_dial.setObjectName("ch2_vDiv_dial")
        self.ch2_enable_button = QtWidgets.QPushButton(self.centralwidget)
        self.ch2_enable_button.setGeometry(QtCore.QRect(120, 480, 75, 23))
        self.ch2_enable_button.setObjectName("ch2_enable_button")
        self.ch2_coupling = QtWidgets.QComboBox(self.centralwidget)
        self.ch2_coupling.setGeometry(QtCore.QRect(130, 620, 51, 22))
        self.ch2_coupling.setObjectName("ch2_coupling")
        self.ch2_coupling.addItem("")
        self.ch2_coupling.addItem("")
        self.ch2_coupling.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 520, 47, 13))
        self.label_7.setObjectName("label_7")
        self.ch2_vertical_dial = QtWidgets.QDial(self.centralwidget)
        self.ch2_vertical_dial.setGeometry(QtCore.QRect(130, 410, 50, 64))
        self.ch2_vertical_dial.setMaximum(8)
        self.ch2_vertical_dial.setPageStep(1)
        self.ch2_vertical_dial.setWrapping(True)
        self.ch2_vertical_dial.setNotchTarget(3.7)
        self.ch2_vertical_dial.setNotchesVisible(True)
        self.ch2_vertical_dial.setObjectName("ch2_vertical_dial")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 400, 47, 13))
        self.label_8.setObjectName("label_8")
        self.ch3_vDiv_dial = QtWidgets.QDial(self.centralwidget)
        self.ch3_vDiv_dial.setGeometry(QtCore.QRect(250, 530, 50, 64))
        self.ch3_vDiv_dial.setMaximum(5)
        self.ch3_vDiv_dial.setPageStep(1)
        self.ch3_vDiv_dial.setProperty("value", 3)
        self.ch3_vDiv_dial.setWrapping(False)
        self.ch3_vDiv_dial.setNotchesVisible(True)
        self.ch3_vDiv_dial.setObjectName("ch3_vDiv_dial")
        self.ch3_enable_button = QtWidgets.QPushButton(self.centralwidget)
        self.ch3_enable_button.setGeometry(QtCore.QRect(240, 480, 75, 23))
        self.ch3_enable_button.setObjectName("ch3_enable_button")
        self.ch3_coupling = QtWidgets.QComboBox(self.centralwidget)
        self.ch3_coupling.setGeometry(QtCore.QRect(250, 620, 51, 22))
        self.ch3_coupling.setObjectName("ch3_coupling")
        self.ch3_coupling.addItem("")
        self.ch3_coupling.addItem("")
        self.ch3_coupling.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 520, 47, 13))
        self.label_9.setObjectName("label_9")
        self.ch3_vertical_dial = QtWidgets.QDial(self.centralwidget)
        self.ch3_vertical_dial.setGeometry(QtCore.QRect(250, 410, 50, 64))
        self.ch3_vertical_dial.setMaximum(8)
        self.ch3_vertical_dial.setPageStep(1)
        self.ch3_vertical_dial.setWrapping(True)
        self.ch3_vertical_dial.setNotchTarget(3.7)
        self.ch3_vertical_dial.setNotchesVisible(True)
        self.ch3_vertical_dial.setObjectName("ch3_vertical_dial")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 400, 47, 13))
        self.label_10.setObjectName("label_10")
        self.ch4_vDiv_dial = QtWidgets.QDial(self.centralwidget)
        self.ch4_vDiv_dial.setGeometry(QtCore.QRect(370, 530, 50, 64))
        self.ch4_vDiv_dial.setMaximum(5)
        self.ch4_vDiv_dial.setPageStep(1)
        self.ch4_vDiv_dial.setProperty("value", 3)
        self.ch4_vDiv_dial.setWrapping(False)
        self.ch4_vDiv_dial.setNotchesVisible(True)
        self.ch4_vDiv_dial.setObjectName("ch4_vDiv_dial")
        self.ch4_enable_button = QtWidgets.QPushButton(self.centralwidget)
        self.ch4_enable_button.setGeometry(QtCore.QRect(360, 480, 75, 23))
        self.ch4_enable_button.setObjectName("ch4_enable_button")
        self.ch4_coupling = QtWidgets.QComboBox(self.centralwidget)
        self.ch4_coupling.setGeometry(QtCore.QRect(370, 620, 51, 22))
        self.ch4_coupling.setObjectName("ch4_coupling")
        self.ch4_coupling.addItem("")
        self.ch4_coupling.addItem("")
        self.ch4_coupling.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 520, 47, 13))
        self.label_11.setObjectName("label_11")
        self.ch4_vertical_dial = QtWidgets.QDial(self.centralwidget)
        self.ch4_vertical_dial.setGeometry(QtCore.QRect(370, 410, 50, 64))
        self.ch4_vertical_dial.setMaximum(8)
        self.ch4_vertical_dial.setPageStep(1)
        self.ch4_vertical_dial.setWrapping(True)
        self.ch4_vertical_dial.setNotchTarget(3.7)
        self.ch4_vertical_dial.setNotchesVisible(True)
        self.ch4_vertical_dial.setObjectName("ch4_vertical_dial")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(370, 400, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 370, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(130, 370, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(250, 370, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(370, 370, 47, 13))
        self.label_16.setObjectName("label_16")
        self.timeDiv_label = QtWidgets.QLabel(self.centralwidget)
        self.timeDiv_label.setGeometry(QtCore.QRect(570, 450, 81, 16))
        self.timeDiv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timeDiv_label.setObjectName("timeDiv_label")
        self.ch1_vDiv_label = QtWidgets.QLabel(self.centralwidget)
        self.ch1_vDiv_label.setGeometry(QtCore.QRect(10, 600, 61, 16))
        self.ch1_vDiv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_vDiv_label.setObjectName("ch1_vDiv_label")
        self.ch2_vDiv_label = QtWidgets.QLabel(self.centralwidget)
        self.ch2_vDiv_label.setGeometry(QtCore.QRect(130, 600, 61, 16))
        self.ch2_vDiv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_vDiv_label.setObjectName("ch2_vDiv_label")
        self.ch3_vDiv_label = QtWidgets.QLabel(self.centralwidget)
        self.ch3_vDiv_label.setGeometry(QtCore.QRect(250, 600, 61, 16))
        self.ch3_vDiv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_vDiv_label.setObjectName("ch3_vDiv_label")
        self.ch4_vDiv_label = QtWidgets.QLabel(self.centralwidget)
        self.ch4_vDiv_label.setGeometry(QtCore.QRect(370, 600, 61, 16))
        self.ch4_vDiv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_vDiv_label.setObjectName("ch4_vDiv_label")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(590, 400, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 651, 351))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.trigger_edge.setCurrentIndex(1)
        self.ch1_coupling.setCurrentIndex(1)
        self.ch2_coupling.setCurrentIndex(1)
        self.ch3_coupling.setCurrentIndex(1)
        self.ch4_coupling.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DSO"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Time/DIV"))
        self.groupBox.setTitle(_translate("MainWindow", "Trigger"))
        self.label_4.setText(_translate("MainWindow", "Trigger edge"))
        self.label_3.setText(_translate("MainWindow", "Trigger source"))
        self.trigger_edge.setItemText(0, _translate("MainWindow", "Falling"))
        self.trigger_edge.setItemText(1, _translate("MainWindow", "Rising"))
        self.trigger_source.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.trigger_source.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.trigger_source.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.trigger_source.setItemText(3, _translate("MainWindow", "Channel 4"))
        self.label_2.setText(_translate("MainWindow", "Level"))
        self.ch1_coupling.setItemText(0, _translate("MainWindow", "GND"))
        self.ch1_coupling.setItemText(1, _translate("MainWindow", "DC"))
        self.ch1_coupling.setItemText(2, _translate("MainWindow", "AC"))
        self.label_5.setText(_translate("MainWindow", "Vertical"))
        self.label_6.setText(_translate("MainWindow", "Volts/DIV"))
        self.ch1_enable_button.setText(_translate("MainWindow", "Enable"))
        self.ch2_enable_button.setText(_translate("MainWindow", "Enable"))
        self.ch2_coupling.setItemText(0, _translate("MainWindow", "GND"))
        self.ch2_coupling.setItemText(1, _translate("MainWindow", "DC"))
        self.ch2_coupling.setItemText(2, _translate("MainWindow", "AC"))
        self.label_7.setText(_translate("MainWindow", "Volts/DIV"))
        self.label_8.setText(_translate("MainWindow", "Vertical"))
        self.ch3_enable_button.setText(_translate("MainWindow", "Enable"))
        self.ch3_coupling.setItemText(0, _translate("MainWindow", "GND"))
        self.ch3_coupling.setItemText(1, _translate("MainWindow", "DC"))
        self.ch3_coupling.setItemText(2, _translate("MainWindow", "AC"))
        self.label_9.setText(_translate("MainWindow", "Volts/DIV"))
        self.label_10.setText(_translate("MainWindow", "Vertical"))
        self.ch4_enable_button.setText(_translate("MainWindow", "Enable"))
        self.ch4_coupling.setItemText(0, _translate("MainWindow", "GND"))
        self.ch4_coupling.setItemText(1, _translate("MainWindow", "DC"))
        self.ch4_coupling.setItemText(2, _translate("MainWindow", "AC"))
        self.label_11.setText(_translate("MainWindow", "Volts/DIV"))
        self.label_12.setText(_translate("MainWindow", "Vertical"))
        self.label_13.setText(_translate("MainWindow", "Channel 1"))
        self.label_14.setText(_translate("MainWindow", "Channel 2"))
        self.label_15.setText(_translate("MainWindow", "Channel3"))
        self.label_16.setText(_translate("MainWindow", "Channel4"))
        self.timeDiv_label.setText(_translate("MainWindow", "50 us"))
        self.ch1_vDiv_label.setText(_translate("MainWindow", "1V"))
        self.ch2_vDiv_label.setText(_translate("MainWindow", "1V"))
        self.ch3_vDiv_label.setText(_translate("MainWindow", "1V"))
        self.ch4_vDiv_label.setText(_translate("MainWindow", "1V"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

from pyqtgraph import PlotWidget
