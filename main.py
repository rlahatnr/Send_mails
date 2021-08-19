from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread
from main_ui import Ui_MainWindow
import sys
import os
import random

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# from apscheduler.schedulers.background import BackgroundScheduler
#
# def job():
#     print('I am working...')
#
# sched = BackgroundScheduler()
# sched.start()
#
# sched.add_job(job, 'cron', day_of_week= 3, hour= 10, minute=40, id = 'test')
# count = 0
# while True:
#     time.sleep(1)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('이메일 대량 전송')
        self.pushButton_5.clicked.connect(self.send_mails)
        self.pushButton_3.clicked.connect(self.open_file)
        self.pushButton_4.clicked.connect(self.get_mails)

        self.pushButton_7.clicked.connect(self.get_accounts)
        self.pushButton_8.clicked.connect(self.send_DMs)

    def send_DMs(self):
        driver = webdriver.Chrome()
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "username")))
        uid = 'contact@crowdparti.com'
        pwd = 'eoqkr2020$!'
        driver.find_element_by_name('username').send_keys(uid)
        driver_pwd = driver.find_element_by_name('password')
        driver_pwd.send_keys(pwd)
        driver_pwd.send_keys(Keys.ENTER)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Instagram']")))

        insta = pd.read_excel(accounts[0])
        for i in insta.iloc[:, 0]:
            content = self.plainTextEdit_2.toPlainText().replace('${이름}', i)
            try:
                driver.get('https://www.instagram.com/direct/inbox/')
                try:
                    WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='나중에 하기']"))).click()
                except:
                    pass
                driver.find_element_by_xpath("//button[text()='메시지 보내기']").click()
                driver.find_element_by_xpath('//input[@placeholder="검색..."]').send_keys(i)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='선택 여부 변경']")))
                driver.find_elements_by_xpath('//span[@aria-label="선택 여부 변경"]')[0].click()
                time.sleep(1)
                driver.find_element_by_xpath('//div[text()="다음"]').click()
                time.sleep(3)
                driver.find_element_by_xpath("//input[@type='file']").send_keys(
                    r'C:\Users\crowdparti\Downloads\크라우드파티 취급 제품 (1) (2).png')
                for part in content.split('\n'):
                    inputs = driver.find_element_by_xpath('//textarea[@placeholder="메시지 입력..."]')
                    inputs.send_keys(part)
                    inputs.send_keys("\n")
                    time.sleep(random.random()+0.3)

                print(f'{i}님께 성공적으로 DM을 전송했습니다.')

            except Exception as e:
                print(e)
                print(f'{i}님 DM 전송에 실패했습니다.')
                pass

        msg = QMessageBox()
        msg.setText('전송 완료하였습니다.')
        msg.exec_()


    def get_accounts(self):
        global accounts
        accounts=QFileDialog.getOpenFileName(self, 'Open File')
        self.label_9.setText(accounts[0])


    def get_mails(self):
        global mails
        mails = QFileDialog.getOpenFileName(self, 'Open File')
        self.label_5.setText(mails[0])


    def open_file(self):
        global attachs
        attachs = QFileDialog.getOpenFileNames(self,'Open File')
        for i in attachs[0]:
            exist = self.textEdit_3.toPlainText()
            self.textEdit_3.setText(exist+i+'\n')

    def send_mails(self):
        global name
        file = pd.read_excel(mails[0])
        try:
            for name, mail in file.values:
                send_id = 'crowdparti@naver.com'
                send_pwd = 'eoqkr2021$!$!'
                context = self.plainTextEdit.toPlainText().replace('${이름}', name)

                smtp = smtplib.SMTP('smtp.naver.com', 587)
                smtp.set_debuglevel(True)
                smtp.starttls()
                smtp.login(send_id, send_pwd)

                msg = MIMEMultipart('alternative')
                msg.set_charset('utf-8')
                msg['From'] = send_id
                msg['To'] = mail
                msg['Subject'] = self.lineEdit_3.text().replace('${이름}', name)

                bodyPart = MIMEText(context, 'plain', 'utf-8')
                msg.attach(bodyPart)
                if len(self.textEdit_3.toPlainText()) > 0:
                    print(self.textEdit_3.toPlainText())

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

                smtp.sendmail(send_id, mail, msg.as_string())
                time.sleep(7)
                print(f'{name}님께 성공적으로 메일을 전송했습니다.')
        except Exception as e:
            print(e)
            print(f'{name}님 메일 전송에 실패했습니다.')
            time.sleep(2)
            pass

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
