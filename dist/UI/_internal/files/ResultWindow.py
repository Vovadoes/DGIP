# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/ResultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 210)
        Form.setMinimumSize(QtCore.QSize(900, 210))
        Form.setMaximumSize(QtCore.QSize(900, 210))
        Form.setStyleSheet("")
        self.gridLayout_8 = QtWidgets.QGridLayout(Form)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(-999999999.0)
        self.doubleSpinBox_2.setMaximum(999999999.0)
        self.doubleSpinBox_2.setSingleStep(1.0)
        self.doubleSpinBox_2.setProperty("value", 0.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_3.setEnabled(False)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_3.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox_3.setDecimals(0)
        self.doubleSpinBox_3.setMinimum(-999999999.0)
        self.doubleSpinBox_3.setMaximum(999999999.0)
        self.doubleSpinBox_3.setSingleStep(1.0)
        self.doubleSpinBox_3.setProperty("value", 0.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_4.addWidget(self.doubleSpinBox_3, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_4.setEnabled(False)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_4.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox_4.setDecimals(0)
        self.doubleSpinBox_4.setMinimum(-999999999.0)
        self.doubleSpinBox_4.setMaximum(999999999.0)
        self.doubleSpinBox_4.setSingleStep(1.0)
        self.doubleSpinBox_4.setProperty("value", 0.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_4.addWidget(self.doubleSpinBox_4, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox.setDecimals(7)
        self.doubleSpinBox.setMinimum(-999999999.0)
        self.doubleSpinBox.setMaximum(999999999.0)
        self.doubleSpinBox.setSingleStep(0.0)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_7.setRowStretch(0, 3)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Определение зараженности зерен вредителями"))
        self.label_5.setText(_translate("Form", "проверенных зерен,"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Вероятность того, что из </span><span style=\" font-size:14pt; font-style:italic;\">n</span><span style=\" font-size:14pt;\"> =</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p>зараженных зерен будет от <span style=\" font-style:italic;\">k</span><span style=\" font-style:italic; vertical-align:sub;\">1</span> =</p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p>до <span style=\" font-style:italic;\">k</span><span style=\" font-style:italic; vertical-align:sub;\">2</span> =</p></body></html>"))
        self.label_10.setText(_translate("Form", "единицу, равна:"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>p</p></body></html>"))
        self.label_3.setText(_translate("Form", "="))
        self.pushButton.setText(_translate("Form", "ОК"))
