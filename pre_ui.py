# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1060, 717)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 1021, 561))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 25, 121, 31))
        self.label_4.setObjectName("label_4")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(100, 670, 171, 20))
        self.status.setObjectName("status")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 670, 71, 16))
        self.label_6.setObjectName("label_6")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(780, 660, 271, 41))
        self.start.setObjectName("start")
        self.cctv = QtWidgets.QPushButton(Dialog)
        self.cctv.setGeometry(QtCore.QRect(370, 670, 80, 26))
        self.cctv.setObjectName("cctv")
        self.lidar = QtWidgets.QPushButton(Dialog)
        self.lidar.setGeometry(QtCore.QRect(460, 670, 80, 26))
        self.lidar.setObjectName("lidar")
        self.dual = QtWidgets.QPushButton(Dialog)
        self.dual.setGeometry(QtCore.QRect(550, 670, 80, 26))
        self.dual.setObjectName("dual")
        self.distance = QtWidgets.QPushButton(Dialog)
        self.distance.setGeometry(QtCore.QRect(640, 670, 80, 26))
        self.distance.setObjectName("distance")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Camera View"))
        self.label_4.setText(_translate("Dialog", "Camera View"))
        self.status.setText(_translate("Dialog", "정지 중"))
        self.label_6.setText(_translate("Dialog", "상태 알림 : "))
        self.start.setText(_translate("Dialog", "S T A R T / S T O P"))
        self.cctv.setText(_translate("Dialog", "CCTV"))
        self.lidar.setText(_translate("Dialog", "LIDAR"))
        self.dual.setText(_translate("Dialog", "DUAL"))
        self.distance.setText(_translate("Dialog", "Distance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

