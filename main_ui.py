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
        MainWindow.resize(900, 939)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_9.addWidget(self.plainTextEdit, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
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
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_9.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_9.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_6.addWidget(self.pushButton_8, 3, 0, 1, 1)
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
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_6.addWidget(self.plainTextEdit_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "${이름}님 안녕하세요.\n"
"\n"
"당사는 아빠스 수제 파스타 및 화덕 피자, 한상궁 시즈닝김 4종세트, 곰표 국수, 곰표 국물다시팩, 효천영농조합 장뇌삼, 해향유통 추석선물세트 등의\n"
"다양한 브랜드 상품의 소셜 마케팅을 주관하고 있는 크라우드파티(주)입니다.\n"
"자세한 내용은 첨부한 사진을 확인해주세요.\n"
"\n"
"현재 당사에서는 블로그 공구를 진행할 인플루언서를 모집하고 있습니다.\n"
"현재 진행하려는 메인 제품은 아빠스의 수제 파스타 3종 (로제 파스타, 풍기크림 파스타, 볼로네제 파스타)입니다.\n"
"아이들 간식 및 캠핑 밀키트 타겟이며, 진행중인 상품은 https://bit.ly/3rSidSy 쿠팡 링크에서 확인 가능합니다.\n"
"\n"
"아빠스 수제 파스타 외 제품 중에 공구를 진행하고 싶으신분들은 말씀해주시면 협의 가능합니다.\n"
"(한상궁 시즈닝김 4종세트, 곰표 국수, 곰표 국물다시팩, 효천영농조합 장뇌삼, 해향유통 추석선물세트 등)\n"
"기타 제품이 궁금하시다면 https://bit.ly/3fuTejo 당사 스마트스토어 링크를 확인해주세요.\n"
"\n"
"${이름}님께서 관심 있으시다면 좋은 조건으로 모시고자 합니다.\n"
"당사와의 협업에 관심이 있으시다면,\n"
"김진수 팀장 / 070-7761-7035(월~목 10:00~18:00) / contact@crowdparti.com로 문의주시면\n"
"언제든지 제안서와 함께 답변 드리겠습니다. 감사합니다!⠀\n"
"\n"
"**실제 공구 진행은 정확한 실적 파악을 위해 자사몰을 사용할 수 있습니다."))
        self.label_6.setText(_translate("MainWindow", "메일 제목"))
        self.label_5.setText(_translate("MainWindow", "파일 없음"))
        self.pushButton_4.setText(_translate("MainWindow", "이메일 목록 가져오기"))
        self.pushButton_3.setText(_translate("MainWindow", "첨부파일"))
        self.pushButton_5.setText(_translate("MainWindow", "메일 전송"))
        self.lineEdit_3.setText(_translate("MainWindow", "${이름}님 안녕하세요. 공구 제안드립니다."))
        self.label_3.setText(_translate("MainWindow", "메일 내용"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "메일"))
        self.pushButton_8.setText(_translate("MainWindow", "DM 전송"))
        self.pushButton_7.setText(_translate("MainWindow", "계정 목록 가져오기"))
        self.label_9.setText(_translate("MainWindow", "파일 없음"))
        self.label_8.setText(_translate("MainWindow", "DM 내용"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "${이름}님 안녕하세요.\n"
"\n"
"당사는 아빠스 수제 파스타 및 화덕 피자, 한상궁 시즈닝김 4종세트, 곰표 국수, 곰표 국물다시팩, 효천영농조합 장뇌삼, 해향유통 추석선물세트 등의 다양한 브랜드 상품의 소셜 마케팅을 주관하고 있는 크라우드파티(주)입니다. 자세한 내용은 첨부한 사진을 확인해주세요.\n"
"\n"
"현재 당사에서는 인스타 공구를 진행할 인플루언서를 모집하고 있습니다. 현재 진행하려는 메인 제품은 아빠스의 수제 파스타 3종 (로제 파스타, 풍기크림 파스타, 볼로네제 파스타)입니다. 아이들 간식 및 캠핑 밀키트 타겟이며, 진행중인 상품은 https://bit.ly/3rSidSy 쿠팡 링크에서 확인 가능합니다.\n"
"\n"
"아빠스 수제 파스타 외 제품 중에 공구를 진행하고 싶으신분들은 말씀해주시면 협의 가능합니다.(한상궁 시즈닝김 4종세트, 곰표 국수, 곰표 국물다시팩, 효천영농조합 장뇌삼, 해향유통 추석선물세트 등) 기타 제품이 궁금하시다면 https://bit.ly/3fuTejo 당사 스마트스토어 링크를 확인해주세요.\n"
"\n"
"${이름}님께서 관심 있으시다면 좋은 조건으로 모시고자 합니다. 당사와의 협업에 관심이 있으시다면, 김진수 팀장 / 070-7761-7035(월~목 10:00~18:00) / contact@crowdparti.com로 문의주시면 언제든지 제안서와 함께 답변 드리겠습니다. 감사합니다!⠀\n"
"**실제 공구 진행은 정확한 실적 파악을 위해 자사몰을 사용할 수 있습니다."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "인스타DM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
