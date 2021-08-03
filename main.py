from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from main_ui import Ui_MainWindow
import sys
import os
import pandas as pd

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('이메일 대량 전송')
        self.pushButton_3.clicked.connect(self.send_mails)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton.clicked.connect(self.get_mails)

    def get_mails(self):
        global mails
        mails = QFileDialog.getOpenFileName(self, 'Open File')
        self.label_4.setText(mails[0])

    def open_file(self):
        global attachs
        attachs = QFileDialog.getOpenFileNames(self,'Open File')
        for i in attachs[0]:
            exist = self.textEdit_2.toPlainText()
            self.textEdit_2.setText(exist+i+'\n')

    def send_mails(self):
        file = pd.read_excel(mails[0])
        try:
            for val in file.mails:
                send_id = 'crowdparti@naver.com'
                send_pwd = 'eoqkr2021$!$!'
                context = self.plainTextEdit.toPlainText()

                smtp = smtplib.SMTP('smtp.naver.com', 587)
                smtp.set_debuglevel(True)
                smtp.starttls()
                smtp.login(send_id, send_pwd)

                msg = MIMEMultipart('alternative')
                msg.set_charset('utf-8')
                msg['From'] = send_id
                msg['To'] = val
                msg['Subject'] = self.lineEdit_3.text()

                bodyPart = MIMEText(context, 'plain', 'utf-8')
                msg.attach(bodyPart)

                if len(attachs) > 0:
                    attachments = list(attachs[0])

                    for attachment in attachments:
                        attach_binary = MIMEBase("application", "octect-stream")
                        try:
                            binary = open(attachment, "rb").read()

                            attach_binary.set_payload(binary)
                            encoders.encode_base64(attach_binary)

                            filename = os.path.basename(attachment)
                            attach_binary.add_header("Content-Disposition", 'attachment',
                                                     filename=('utf-8', '', filename))

                            msg.attach(attach_binary)
                        except Exception as e:
                            print(e)

                smtp.sendmail(send_id, val, msg.as_string())
                print('Successfully sent the mail')
        except Exception as e:
            print(e)
        finally:
            if smtp is not None:
                smtp.quit()


                msg = QMessageBox()
                msg.setText('전송 완료하였습니다.')
                msg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())