# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import XO_Classification_Adaline_TwoOutput as xo

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(935, 611)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 674, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy)
        self.Button_0.setAutoFillBackground(False)
        self.Button_0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_0.setText("")
        self.Button_0.setCheckable(True)
        self.Button_0.setObjectName("Button_0")
        self.gridLayout.addWidget(self.Button_0, 0, 0, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        self.Button_1.setAutoFillBackground(False)
        self.Button_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_1.setText("")
        self.Button_1.setCheckable(True)
        self.Button_1.setObjectName("Button_1")
        self.gridLayout.addWidget(self.Button_1, 0, 1, 1, 1)
        self.Button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy)
        self.Button_4.setAutoFillBackground(False)
        self.Button_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_4.setText("")
        self.Button_4.setCheckable(True)
        self.Button_4.setObjectName("Button_4")
        self.gridLayout.addWidget(self.Button_4, 0, 4, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        self.Button_3.setAutoFillBackground(False)
        self.Button_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_3.setText("")
        self.Button_3.setCheckable(True)
        self.Button_3.setObjectName("Button_3")
        self.gridLayout.addWidget(self.Button_3, 0, 3, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        self.Button_2.setAutoFillBackground(False)
        self.Button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_2.setText("")
        self.Button_2.setCheckable(True)
        self.Button_2.setObjectName("Button_2")
        self.gridLayout.addWidget(self.Button_2, 0, 2, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy)
        self.Button_5.setAutoFillBackground(False)
        self.Button_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_5.setText("")
        self.Button_5.setCheckable(True)
        self.Button_5.setObjectName("Button_5")
        self.gridLayout.addWidget(self.Button_5, 1, 0, 1, 1)
        self.Button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy)
        self.Button_6.setAutoFillBackground(False)
        self.Button_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_6.setText("")
        self.Button_6.setCheckable(True)
        self.Button_6.setObjectName("Button_6")
        self.gridLayout.addWidget(self.Button_6, 1, 1, 1, 1)
        self.Button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy)
        self.Button_9.setAutoFillBackground(False)
        self.Button_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_9.setText("")
        self.Button_9.setCheckable(True)
        self.Button_9.setObjectName("Button_9")
        self.gridLayout.addWidget(self.Button_9, 1, 4, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy)
        self.Button_8.setAutoFillBackground(False)
        self.Button_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_8.setText("")
        self.Button_8.setCheckable(True)
        self.Button_8.setObjectName("Button_8")
        self.gridLayout.addWidget(self.Button_8, 1, 3, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy)
        self.Button_7.setAutoFillBackground(False)
        self.Button_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_7.setText("")
        self.Button_7.setCheckable(True)
        self.Button_7.setObjectName("Button_7")
        self.gridLayout.addWidget(self.Button_7, 1, 2, 1, 1)
        self.Button_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_10.sizePolicy().hasHeightForWidth())
        self.Button_10.setSizePolicy(sizePolicy)
        self.Button_10.setAutoFillBackground(False)
        self.Button_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_10.setText("")
        self.Button_10.setCheckable(True)
        self.Button_10.setObjectName("Button_10")
        self.gridLayout.addWidget(self.Button_10, 2, 0, 1, 1)
        self.Button_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_14.sizePolicy().hasHeightForWidth())
        self.Button_14.setSizePolicy(sizePolicy)
        self.Button_14.setAutoFillBackground(False)
        self.Button_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_14.setText("")
        self.Button_14.setCheckable(True)
        self.Button_14.setObjectName("Button_14")
        self.gridLayout.addWidget(self.Button_14, 2, 4, 1, 1)
        self.Button_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_13.sizePolicy().hasHeightForWidth())
        self.Button_13.setSizePolicy(sizePolicy)
        self.Button_13.setAutoFillBackground(False)
        self.Button_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_13.setText("")
        self.Button_13.setCheckable(True)
        self.Button_13.setObjectName("Button_13")
        self.gridLayout.addWidget(self.Button_13, 2, 3, 1, 1)
        self.Button_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_12.sizePolicy().hasHeightForWidth())
        self.Button_12.setSizePolicy(sizePolicy)
        self.Button_12.setAutoFillBackground(False)
        self.Button_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_12.setText("")
        self.Button_12.setCheckable(True)
        self.Button_12.setObjectName("Button_12")
        self.gridLayout.addWidget(self.Button_12, 2, 2, 1, 1)
        self.Button_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_11.sizePolicy().hasHeightForWidth())
        self.Button_11.setSizePolicy(sizePolicy)
        self.Button_11.setAutoFillBackground(False)
        self.Button_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_11.setText("")
        self.Button_11.setCheckable(True)
        self.Button_11.setObjectName("Button_11")
        self.gridLayout.addWidget(self.Button_11, 2, 1, 1, 1)
        self.Button_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_15.sizePolicy().hasHeightForWidth())
        self.Button_15.setSizePolicy(sizePolicy)
        self.Button_15.setAutoFillBackground(False)
        self.Button_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_15.setText("")
        self.Button_15.setCheckable(True)
        self.Button_15.setObjectName("Button_15")
        self.gridLayout.addWidget(self.Button_15, 3, 0, 1, 1)
        self.Button_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_20.sizePolicy().hasHeightForWidth())
        self.Button_20.setSizePolicy(sizePolicy)
        self.Button_20.setAutoFillBackground(False)
        self.Button_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_20.setText("")
        self.Button_20.setCheckable(True)
        self.Button_20.setObjectName("Button_20")
        self.gridLayout.addWidget(self.Button_20, 5, 0, 1, 1)
        self.Button_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_22.sizePolicy().hasHeightForWidth())
        self.Button_22.setSizePolicy(sizePolicy)
        self.Button_22.setAutoFillBackground(False)
        self.Button_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_22.setText("")
        self.Button_22.setCheckable(True)
        self.Button_22.setObjectName("Button_22")
        self.gridLayout.addWidget(self.Button_22, 5, 2, 1, 1)
        self.Button_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_23.sizePolicy().hasHeightForWidth())
        self.Button_23.setSizePolicy(sizePolicy)
        self.Button_23.setAutoFillBackground(False)
        self.Button_23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_23.setText("")
        self.Button_23.setCheckable(True)
        self.Button_23.setObjectName("Button_23")
        self.gridLayout.addWidget(self.Button_23, 5, 3, 1, 1)
        self.Button_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_24.sizePolicy().hasHeightForWidth())
        self.Button_24.setSizePolicy(sizePolicy)
        self.Button_24.setAutoFillBackground(False)
        self.Button_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_24.setText("")
        self.Button_24.setCheckable(True)
        self.Button_24.setObjectName("Button_24")
        self.gridLayout.addWidget(self.Button_24, 5, 4, 1, 1)
        self.Button_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_19.sizePolicy().hasHeightForWidth())
        self.Button_19.setSizePolicy(sizePolicy)
        self.Button_19.setAutoFillBackground(False)
        self.Button_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_19.setText("")
        self.Button_19.setCheckable(True)
        self.Button_19.setObjectName("Button_19")
        self.gridLayout.addWidget(self.Button_19, 3, 4, 1, 1)
        self.Button_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_18.sizePolicy().hasHeightForWidth())
        self.Button_18.setSizePolicy(sizePolicy)
        self.Button_18.setAutoFillBackground(False)
        self.Button_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_18.setText("")
        self.Button_18.setCheckable(True)
        self.Button_18.setObjectName("Button_18")
        self.gridLayout.addWidget(self.Button_18, 3, 3, 1, 1)
        self.Button_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_17.sizePolicy().hasHeightForWidth())
        self.Button_17.setSizePolicy(sizePolicy)
        self.Button_17.setAutoFillBackground(False)
        self.Button_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_17.setText("")
        self.Button_17.setCheckable(True)
        self.Button_17.setObjectName("Button_17")
        self.gridLayout.addWidget(self.Button_17, 3, 2, 1, 1)
        self.Button_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_16.sizePolicy().hasHeightForWidth())
        self.Button_16.setSizePolicy(sizePolicy)
        self.Button_16.setAutoFillBackground(False)
        self.Button_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_16.setText("")
        self.Button_16.setCheckable(True)
        self.Button_16.setObjectName("Button_16")
        self.gridLayout.addWidget(self.Button_16, 3, 1, 1, 1)
        self.Button_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_21.sizePolicy().hasHeightForWidth())
        self.Button_21.setSizePolicy(sizePolicy)
        self.Button_21.setAutoFillBackground(False)
        self.Button_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_21.setText("")
        self.Button_21.setCheckable(True)
        self.Button_21.setObjectName("Button_21")
        self.gridLayout.addWidget(self.Button_21, 5, 1, 1, 1)
        self.resultButton = QtWidgets.QPushButton(Dialog)
        self.resultButton.setGeometry(QtCore.QRect(760, 150, 121, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.resultButton.setFont(font)
        self.resultButton.setStyleSheet("background-color: rgb(186, 189, 182); color: rgb(0, 0, 0)")
        self.resultButton.setObjectName("resultButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(740, 290, 171, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(760, 210, 121, 41))
        font = QtGui.QFont()
        font.setItalic(True) 
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color: rgb(186, 189, 182); color: rgb(0, 0, 0)")
        self.resetButton.setObjectName("resetButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.Button_0.clicked.connect(lambda x: self.Button_0.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_0.styleSheet().__contains__('255') else self.Button_0.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_1.clicked.connect(lambda x: self.Button_1.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_1.styleSheet().__contains__('255') else self.Button_1.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_2.clicked.connect(lambda x: self.Button_2.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_2.styleSheet().__contains__('255') else self.Button_2.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_3.clicked.connect(lambda x: self.Button_3.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_3.styleSheet().__contains__('255') else self.Button_3.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_4.clicked.connect(lambda x: self.Button_4.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_4.styleSheet().__contains__('255') else self.Button_4.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_5.clicked.connect(lambda x: self.Button_5.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_5.styleSheet().__contains__('255') else self.Button_5.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_6.clicked.connect(lambda x: self.Button_6.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_6.styleSheet().__contains__('255') else self.Button_6.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_7.clicked.connect(lambda x: self.Button_7.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_7.styleSheet().__contains__('255') else self.Button_7.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_8.clicked.connect(lambda x: self.Button_8.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_8.styleSheet().__contains__('255') else self.Button_8.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_9.clicked.connect(lambda x: self.Button_9.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_9.styleSheet().__contains__('255') else self.Button_9.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_10.clicked.connect(lambda x: self.Button_10.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_10.styleSheet().__contains__('255') else self.Button_10.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_11.clicked.connect(lambda x: self.Button_11.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_11.styleSheet().__contains__('255') else self.Button_11.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_12.clicked.connect(lambda x: self.Button_12.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_12.styleSheet().__contains__('255') else self.Button_12.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_13.clicked.connect(lambda x: self.Button_13.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_13.styleSheet().__contains__('255') else self.Button_13.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_14.clicked.connect(lambda x: self.Button_14.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_14.styleSheet().__contains__('255') else self.Button_14.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_15.clicked.connect(lambda x: self.Button_15.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_15.styleSheet().__contains__('255') else self.Button_15.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_16.clicked.connect(lambda x: self.Button_16.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_16.styleSheet().__contains__('255') else self.Button_16.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_17.clicked.connect(lambda x: self.Button_17.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_17.styleSheet().__contains__('255') else self.Button_17.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_18.clicked.connect(lambda x: self.Button_18.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_18.styleSheet().__contains__('255') else self.Button_18.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_19.clicked.connect(lambda x: self.Button_19.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_19.styleSheet().__contains__('255') else self.Button_19.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_20.clicked.connect(lambda x: self.Button_20.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_20.styleSheet().__contains__('255') else self.Button_20.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_21.clicked.connect(lambda x: self.Button_21.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_21.styleSheet().__contains__('255') else self.Button_21.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_22.clicked.connect(lambda x: self.Button_22.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_22.styleSheet().__contains__('255') else self.Button_22.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_23.clicked.connect(lambda x: self.Button_23.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_23.styleSheet().__contains__('255') else self.Button_23.setStyleSheet('background-color: rgb(255,255,255)'))
        self.Button_24.clicked.connect(lambda x: self.Button_24.setStyleSheet('background-color: rgb(0,0,0)') if self.Button_24.styleSheet().__contains__('255') else self.Button_24.setStyleSheet('background-color: rgb(255,255,255)'))
        self.resultButton.clicked.connect(self.getResult)
        self.resetButton.clicked.connect(self.restart)


    def getResult(self):

        grid = [[-1 for _ in range(5)] for _ in range(5)]

        if self.Button_0.styleSheet().__contains__("0"): grid[0][0] = 1
        else: grid[0][0] = -1
        if self.Button_1.styleSheet().__contains__("0"): grid[0][1] = 1
        else: grid[0][1] = -1
        if self.Button_2.styleSheet().__contains__("0"): grid[0][2] = 1
        else: grid[0][2] = -1
        if self.Button_3.styleSheet().__contains__("0"): grid[0][3] = 1
        else: grid[0][3] = -1
        if self.Button_4.styleSheet().__contains__("0"): grid[0][4] = 1
        else: grid[0][4] = -1
        if self.Button_5.styleSheet().__contains__("0"): grid[1][0] = 1
        else: grid[1][0] = -1
        if self.Button_6.styleSheet().__contains__("0"): grid[1][1] = 1
        else: grid[1][1] = -1
        if self.Button_7.styleSheet().__contains__("0"): grid[1][2] = 1
        else: grid[1][2] = -1
        if self.Button_8.styleSheet().__contains__("0"): grid[1][3] = 1
        else: grid[1][3] = -1
        if self.Button_9.styleSheet().__contains__("0"): grid[1][4] = 1
        else: grid[1][4] = -1
        if self.Button_10.styleSheet().__contains__("0"): grid[2][0] = 1
        else: grid[2][0] = -1
        if self.Button_11.styleSheet().__contains__("0"): grid[2][1] = 1
        else: grid[2][1] = -1
        if self.Button_12.styleSheet().__contains__("0"): grid[2][2] = 1
        else: grid[2][2] = -1
        if self.Button_13.styleSheet().__contains__("0"): grid[2][3] = 1
        else: grid[2][3] = -1
        if self.Button_14.styleSheet().__contains__("0"): grid[2][4] = 1
        else: grid[2][4] = -1
        if self.Button_15.styleSheet().__contains__("0"): grid[3][0] = 1
        else: grid[3][0] = -1
        if self.Button_16.styleSheet().__contains__("0"): grid[3][1] = 1
        else: grid[3][1] = -1
        if self.Button_17.styleSheet().__contains__("0"): grid[3][2] = 1
        else: grid[3][2] = -1
        if self.Button_18.styleSheet().__contains__("0"): grid[3][3] = 1
        else: grid[3][3] = -1
        if self.Button_19.styleSheet().__contains__("0"): grid[3][4] = 1
        else: grid[3][4] = -1
        if self.Button_20.styleSheet().__contains__("0"): grid[4][0] = 1
        else: grid[4][0] = -1
        if self.Button_21.styleSheet().__contains__("0"): grid[4][1] = 1
        else: grid[4][1] = -1
        if self.Button_22.styleSheet().__contains__("0"): grid[4][2] = 1
        else: grid[4][2] = -1
        if self.Button_23.styleSheet().__contains__("0"): grid[4][3] = 1
        else: grid[4][3] = -1
        if self.Button_24.styleSheet().__contains__("0"): grid[4][4] = 1
        else: grid[4][4] = -1

        x_test = xo.converter(grid)
        result = xo.test(x_test)
        if result == [1, -1]:
            print('X')
            self.label.setText(" It is an X")
        else:
            print('O')
            self.label.setText(" It is an O")


    def restart(self):
        self.label.setText("Result will appear here")
        self.Button_0.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_1.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_2.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_3.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_4.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_5.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_6.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_7.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_8.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_9.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_10.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_11.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_12.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_13.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_14.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_15.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_16.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_17.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_18.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_19.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_20.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_21.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_22.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_23.setStyleSheet('background-color: rgb(255,255,255)')
        self.Button_24.setStyleSheet('background-color: rgb(255,255,255)')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.resultButton.setText(_translate("Dialog", "Get the result"))
        self.label.setText(_translate("Dialog", "Result will appear here"))
        self.resetButton.setText(_translate("Dialog", "Reset"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
