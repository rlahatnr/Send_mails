# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 1117)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_9.addWidget(self.plainTextEdit, 10, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_9.addWidget(self.pushButton_5, 11, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 46))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 1, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 46))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 46))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 140))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_3.addWidget(self.textEdit_3, 1, 0, 1, 5)
        self.gridLayout_9.addLayout(self.gridLayout_3, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 9, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_9.addWidget(self.lineEdit_3, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 7, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 46))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 46))
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 1, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_6.addWidget(self.pushButton_8, 4, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_6.addWidget(self.plainTextEdit_2, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "메일 전송"))
        self.label_5.setText(_translate("MainWindow", "파일 없음"))
        self.pushButton_4.setText(_translate("MainWindow", "이메일 목록 가져오기"))
        self.pushButton_3.setText(_translate("MainWindow", "첨부파일"))
        self.label_3.setText(_translate("MainWindow", "메일 내용"))
        self.label_6.setText(_translate("MainWindow", "메일 제목"))
        self.groupBox.setTitle(_translate("MainWindow", "계정정보"))
        self.label.setText(_translate("MainWindow", "네이버 이메일"))
        self.label_2.setText(_translate("MainWindow", "비밀번호"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "메일"))
        self.pushButton_7.setText(_translate("MainWindow", "계정 목록 가져오기"))
        self.label_9.setText(_translate("MainWindow", "파일 없음"))
        self.label_8.setText(_translate("MainWindow", "DM 내용"))
        self.pushButton_8.setText(_translate("MainWindow", "DM 전송"))
        self.groupBox_3.setTitle(_translate("MainWindow", "계정정보"))
        self.label_10.setText(_translate("MainWindow", "인스타 아이디"))
        self.label_11.setText(_translate("MainWindow", "비밀번호"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "인스타DM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
