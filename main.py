from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
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
import chromedriver_autoinstaller

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

        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.lineEdit_7.setEchoMode(self.lineEdit_7.Password)

    # 인스타 dm 보내는 코드
    def send_DMs(self):
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "username")))

        # gui 상의 아이디와 비밀번호를 받는다.
        uid = self.lineEdit_6.text()
        pwd = self.lineEdit_7.text()
        driver.find_element_by_name('username').send_keys(uid)
        driver_pwd = driver.find_element_by_name('password')
        driver_pwd.send_keys(pwd)
        driver_pwd.send_keys(Keys.ENTER)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Instagram']")))

        # 첨부한 계정 목록 파일 [인스타그램 id]에 따라 계정을 검색하고 gui 상의 dm내용을 전송함
        # 해당 아이디가 없다면 (수정 등의 이유로) 가장 비슷한 아이디를 찾아 전송한다.
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
                time.sleep(3)
                sub_window = driver.find_element_by_xpath("//div[@aria-label='새로운 메시지']")
                sub_window.find_elements_by_tag_name('button')[2].click()
                time.sleep(1)
                driver.find_element_by_xpath('//div[text()="다음"]').click()
                time.sleep(3)
                '''
                사진 첨부 코드: 아래의 코드를 활성화 하면 사진 첨부 가능하지만 
                묶어보내기 기능이 없으므로 여러 사진을 보내야한다면 아래 코드를 for문으로 돌린다.
                '''
                # driver.find_element_by_xpath("//input[@type='file']").send_keys(
                #     r'첨부파일/경로/파일명.png')
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


    # 메일을 전송하는 코드
    def send_mails(self):
        global name
        file = pd.read_excel(mails[0])
        try:
            # 첨부파일에서 아이디(닉네임)과 메일 가져옴
            for name, mail in file.values:
                # gui상 아이디와 비밀번호, 메일 내용 가져옴
                send_id = self.lineEdit.text()
                send_pwd = self.lineEdit_2.text()
                context = self.plainTextEdit.toPlainText()

                # 메일 대량전송 코드(구글의 경우 보안이 심해 네이버로 작성)
                smtp = smtplib.SMTP('smtp.naver.com', 587)
                smtp.set_debuglevel(True)
                smtp.starttls()
                smtp.login(send_id, send_pwd)

                msg = MIMEMultipart('alternative')
                msg.set_charset('utf-8')
                msg['From'] = send_id
                msg['To'] = mail
                msg['Subject'] = self.lineEdit_3.text()

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
                time.sleep(10)
                print(f'{name}님께 성공적으로 메일을 전송했습니다.')
        except Exception as e:
            print(e)
            print(f'{name}님 메일 전송에 실패했습니다.')
            time.sleep(2)
            pass
        
        # 여러건 모두 전송이 끝나면 종료
        finally:
            if smtp is not None:
                smtp.quit()

                msg = QMessageBox()
                msg.setText('전송 완료하였습니다.')
                msg.exec_()

    # 첨부파일에서 인스타 계정 가져옴
    def get_accounts(self):
        global accounts
        accounts=QFileDialog.getOpenFileName(self, 'Open File')
        self.label_9.setText(accounts[0])

    # 첨부파일에서 이메일을 가져옴
    def get_mails(self):
        global mails
        mails = QFileDialog.getOpenFileName(self, 'Open File')
        self.label_5.setText(mails[0])

    # 첨부파일을 첨부하는 코드
    def open_file(self):
        global attachs
        attachs = QFileDialog.getOpenFileNames(self,'Open File')
        for i in attachs[0]:
            exist = self.textEdit_3.toPlainText()
            self.textEdit_3.setText(exist+i+'\n')

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
