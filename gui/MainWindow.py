# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 816)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Layout_map = QtWidgets.QVBoxLayout()
        self.Layout_map.setObjectName("Layout_map")
        self.horizontalLayout.addLayout(self.Layout_map)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_gps = QtWidgets.QLabel(MainWindow)
        self.label_gps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gps.setObjectName("label_gps")
        self.verticalLayout_2.addWidget(self.label_gps)
        self.label_speed = QtWidgets.QLabel(MainWindow)
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.verticalLayout_2.addWidget(self.label_speed)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_draw = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_draw.sizePolicy().hasHeightForWidth())
        self.pushButton_draw.setSizePolicy(sizePolicy)
        self.pushButton_draw.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_draw.setMaximumSize(QtCore.QSize(16777210, 16777210))
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.horizontalLayout_2.addWidget(self.pushButton_draw)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mainwindow"))
        self.label_gps.setText(_translate("MainWindow", "GPS"))
        self.label_speed.setText(_translate("MainWindow", "SPEED"))
        self.pushButton_draw.setText(_translate("MainWindow", "Draw"))
