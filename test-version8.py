# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
 
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class MyWindow(QMainWindow):
   def __init__(self):
       super().__init__()
 
       self.setWindowIcon(QIcon('usb.png'))
       self.setWindowTitle("암/복호화 선택")
       self.resize(420, 430)
 
       self.btn1 = QPushButton("파일 암호화", self)
       self.btn1.setGeometry(85, 50, 250, 50)
       self.btn1.clicked.connect(self.check1)
     
       self.btn2 = QPushButton("파일 복호화", self)
       self.btn2.setGeometry(85, 120, 250, 50)
       self.btn2.clicked.connect(self.pwcheck2)
 
       self.btn14 = QPushButton("디렉터리 암호화", self)
       self.btn14.setGeometry(85, 190, 250, 50)
       self.btn14.clicked.connect(self.check2)
     
       self.btn15 = QPushButton("디렉터리 복호화", self)
       self.btn15.setGeometry(85, 260, 250, 50)
       self.btn15.clicked.connect(self.dpwcheck2)
 
       self.btn3 = QPushButton("프로그램 종료", self)
       self.btn3.setGeometry(85, 330, 250, 50)
       self.btn3.clicked.connect(self.cancel)
 
   def password(self):
       dialog = Password(self)
       dialog.show()
 
   def pwcheck(self):
       dialog = Pwcheck(self)
       dialog.show()
 
   def pwcheck2(self):
       dialog = Pwcheck2(self)
       dialog.show()
 
   def dpwcheck2(self):
       dialog = dPwcheck2(self)
       dialog.show()
 
   def dpwcheck(self):
       dialog = dPwcheck(self)
       dialog.show()
 
   def cancel(self):
       self.reject()
 
   def check1(self):
       if os.path.isfile('data.txt.enc'):
           self.pwcheck()
 
       else:
           self.password()
 
   def check2(self):
       if os.path.isfile('data.txt.enc'):
           self.dpwcheck()
 
       else:
           self.password()
 
class Password(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 생성")
       self.resize(507, 207)
 
       self.label = QLabel("비밀번호 생성", self)
       self.label.move(30, 51)
 
       self.label2 = QLabel("비밀번호 확인", self)
       self.label2.move(30, 100)      
 
       self.textEdit = QTextEdit("", self)
       self.textEdit.setGeometry(200, 49, 250, 30)
 
       self.textEdit2 = QTextEdit("", self)
       self.textEdit2.setGeometry(200, 98, 250, 30)
 
       self.btn4 = QPushButton("확인", self)
       self.btn4.setGeometry(320, 150, 60, 35)
       self.btn4.clicked.connect(self.passwordcheck)
 
       self.btn5 = QPushButton("취소", self)
       self.btn5.setGeometry(420, 150, 60, 35)
       self.btn5.clicked.connect(self.cancel)
 
 
   def passwordcheck(self):
       if (self.textEdit.toPlainText() == self.textEdit2.toPlainText()):
           f = open("data.txt", "w+")
           f.write(self.textEdit.toPlainText())
           f.close()
           enc.encrypt_file("data.txt")
           self.success()
           self.accept()
           
       else:
           self.fail()
 
   def cancel(self):
       self.reject()
 
   def success(self):
       dialog = Success(self)
       dialog.show()
 
   def fail(self):
       dialog = Fail(self)
       dialog.show()
 
class Pwcheck(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 입력")
       self.resize(410, 164)
 
       self.label2 = QLabel("비밀번호를 입력하세요.", self)
       self.label2.move(25, 20)      
 
       self.textEdit3 = QTextEdit("", self)
       self.textEdit3.setGeometry(25, 55, 350, 30)
 
       self.btn6 = QPushButton("확인", self)
       self.btn6.setGeometry(230, 100, 60, 35)
       self.btn6.clicked.connect(self.passwordcheck2)
 
       self.btn7 = QPushButton("취소", self)
       self.btn7.setGeometry(320, 100, 60, 35)
       self.btn7.clicked.connect(self.cancel)
 
 
   
   def passwordcheck2(self):
       password=self.textEdit3.toPlainText()
       p = ''
       enc.decrypt_file("data.txt.enc")
       self.accept()
       
       with open("data.txt", "r") as f:
           p = f.readlines()
           
       if password == p[0]:
           enc.encrypt_file("data.txt")
           self.enc()
       elif password !=p[0]:
           enc.encrypt_file("data.txt")
           self.error()
##        elif (password !=p[0])&(count==5):
##            enc.encrypt_file("data.txt")
##            sys.exit()
 
   def cancel(self):
       self.reject()
 
   def enc(self):
       dialog = Enc(self)
       dialog.show()
 
   def error(self):
       dialog = Error(self)
       dialog.show()
 
class Error(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 오류")
       self.resize(410, 164)
 
       self.label10 = QLabel("비밀번호가 틀렸습니다.", self)
       self.label10.move(80,51)
       
       self.btn20 = QPushButton("확인", self)
       self.btn20.setGeometry(260, 100, 60, 35)
       self.btn20.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
class dPwcheck(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 입력")
       self.resize(410, 164)
 
       self.label8 = QLabel("비밀번호를 입력하세요.", self)
       self.label8.move(25, 20)      
 
       self.textEdit7 = QTextEdit("", self)
       self.textEdit7.setGeometry(25, 55, 350, 30)
 
       self.btn16 = QPushButton("확인", self)
       self.btn16.setGeometry(230, 100, 60, 35)
       self.btn16.clicked.connect(self.passwordcheck4)
 
       self.btn17 = QPushButton("취소", self)
       self.btn17.setGeometry(320, 100, 60, 35)
       self.btn17.clicked.connect(self.cancel)
   
   def passwordcheck4(self):
       password=self.textEdit7.toPlainText()
       p = ''
       enc.decrypt_file("data.txt.enc")
       
       
       with open("data.txt", "r") as f:
           p = f.readlines()
           
       if password == p[0]:
           enc.encrypt_file("data.txt")
           enc.encrypt_all_files()
           self.what()
           self.accept()
           
       elif password !=p[0]:
           enc.encrypt_file("data.txt")
           self.error()
               
   def cancel(self):
       self.reject()
 
   def error(self):
       dialog = Error(self)
       dialog.show()
 
   def what(self):
       dialog = What(self)
       dialog.show()
 
class What(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("디렉터리 암호화")
       self.resize(507, 207)
 
       self.label11 = QLabel("디렉터리를 암호화 했습니다.\n확인을 눌러주세요.", self)
       self.label11.move(100,51)
 
       self.btn21 = QPushButton("확인", self)
       self.btn21.setGeometry(320, 150, 60, 35)
       self.btn21.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
class Pwcheck2(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 입력")
       self.resize(410, 164)
 
       self.label6 = QLabel("비밀번호를 입력하세요.", self)
       self.label6.move(25, 20)      
 
       self.textEdit4 = QTextEdit("", self)
       self.textEdit4.setGeometry(25, 55, 350, 30)
 
       self.btn11 = QPushButton("확인", self)
       self.btn11.setGeometry(230, 100, 60, 35)
       self.btn11.clicked.connect(self.passwordcheck3)
 
       self.btn12 = QPushButton("취소", self)
       self.btn12.setGeometry(320, 100, 60, 35)
       self.btn12.clicked.connect(self.cancel)
   
   def passwordcheck3(self):
       password=self.textEdit4.toPlainText()
       p = ''
       enc.decrypt_file("data.txt.enc")
       self.accept()
       
       with open("data.txt", "r") as f:
           p = f.readlines()
           
       if password == p[0]:
           enc.encrypt_file("data.txt")
           self.dec()
               
   def cancel(self):
       self.reject()
     
   def success(self):
       dialog = Success(self)
       dialog.show()
 
   def fail(self):
       dialog = Fail(self)
       dialog.show()
 
   def dec(self):
       dialog = Dec(self)
       dialog.show()
 
class dPwcheck2(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 입력")
       self.resize(410, 164)
 
       self.label9 = QLabel("비밀번호를 입력하세요.", self)
       self.label9.move(25, 20)      
 
       self.textEdit8 = QTextEdit("", self)
       self.textEdit8.setGeometry(25, 55, 350, 30)
 
       self.btn18 = QPushButton("확인", self)
       self.btn18.setGeometry(230, 100, 60, 35)
       self.btn18.clicked.connect(self.passwordcheck5)
 
       self.btn19 = QPushButton("취소", self)
       self.btn19.setGeometry(320, 100, 60, 35)
       self.btn19.clicked.connect(self.cancel)
   
   def passwordcheck5(self):
       password=self.textEdit8.toPlainText()
       p = ''
       enc.decrypt_file("data.txt.enc")
 
       
       
       with open("data.txt", "r") as f:
           p = f.readlines()
           
       if password == p[0]:
           enc.encrypt_file("data.txt")
           enc.decrypt_all_files()
           self.what2()
           self.accept()
 
       elif password !=p[0]:
           enc.encrypt_file("data.txt")
           self.error()
               
   def cancel(self):
       self.reject()
 
   def error(self):
       dialog = Error(self)
       dialog.show()
 
   def what2(self):
       dialog = What2(self)
       dialog.show()
       
class What2(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("디렉터리 복호화")
       self.resize(507, 207)
 
       self.label12 = QLabel("디렉터리를 복호화 했습니다.\n확인을 눌러주세요.", self)
       self.label12.move(100,51)
 
       self.btn22 = QPushButton("확인", self)
       self.btn22.setGeometry(320, 150, 60, 35)
       self.btn22.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
class Success(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 확인")
       self.resize(507, 207)
 
       self.label3 = QLabel("비밀번호가 생성되었습니다.\n확인을 눌러주세요.", self)
       self.label3.move(100,51)
 
       self.btn8 = QPushButton("확인", self)
       self.btn8.setGeometry(320, 150, 60, 35)
       self.btn8.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
 
class Fail(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("비밀번호 확인")
       self.resize(507, 207)
 
       self.label4 = QLabel("비밀번호가 일치하지 않습니다.\n다시 시도해주세요.", self)
       self.label4.move(100,51)
 
       self.btn9 = QPushButton("확인", self)
       self.btn9.setGeometry(320, 150, 60, 35)
       self.btn9.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
class Enc(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("파일 암호화")
       self.resize(410, 200)
 
       self.num = 0
       self.label5 = QLabel("암호화할 파일을 선택하세요.", self)
       self.label5.move(25, 10)
 
 
       self.btnfile = QPushButton("파일선택", self)
       self.btnfile.setGeometry(150, 80, 100, 35)
       self.btnfile.clicked.connect(self.OpenDocument)
 
       self.label50 = QLabel()
       self.label50.move(100,51)
 
       layout = QVBoxLayout()
       layout.addWidget(self.btnfile)
       layout.addWidget(self.label50)
 
       self.setLayout(layout)
 
       self.btn10 = QPushButton("확인", self)
       self.btn10.setGeometry(320, 150, 60, 35)
       self.btn10.clicked.connect(self.encgo)
 
   def OpenDocument(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label50.setText(fname[0])
 
   def encgo(self):
       enc.encrypt_file(self.label50.text())
       self.what3()
       self.accept()
       
   def what3(self):
       dialog = What3(self)
       dialog.show()
 
class What3(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("파일 암호화")
       self.resize(507, 207)
 
       self.label13 = QLabel("파일을 암호화 했습니다.\n확인을 눌러주세요.", self)
       self.label13.move(100,51)
 
       self.btn23 = QPushButton("확인", self)
       self.btn23.setGeometry(320, 150, 60, 35)
       self.btn23.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
 
class Dec(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("파일 복호화")
       self.resize(410, 200)
 
       self.label7 = QLabel("복호화할 파일을 선택하세요.", self)
       self.label7.move(25, 10)      
 
       self.btnfile2 = QPushButton("파일선택", self)
       self.btnfile2.setGeometry(150, 80, 100, 35)
       self.btnfile2.clicked.connect(self.OpenDocument2)
 
       self.label51 = QLabel()
       self.label51.move(100,51)
 
       layout = QVBoxLayout()
       layout.addWidget(self.btnfile2)
       layout.addWidget(self.label51)
 
       self.setLayout(layout)
 
       self.btn13 = QPushButton("확인", self)
       self.btn13.setGeometry(320, 150, 60, 35)
       self.btn13.clicked.connect(self.decgo)
 
   def OpenDocument2(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label51.setText(fname[0])
 
 
   def decgo(self):
       enc.decrypt_file(self.label51.text())
       self.what4()
       self.accept()
 
   def what4(self):
       dialog = What4(self)
       dialog.show()
 
class What4(QDialog):
   def __init__(self, parent = None):
       super().__init__(parent)
       self.setWindowTitle("파일 복호화")
       self.resize(507, 207)
 
       self.label14 = QLabel("파일을 복호화 했습니다.\n확인을 눌러주세요.", self)
       self.label14.move(100,51)
 
       self.btn24 = QPushButton("확인", self)
       self.btn24.setGeometry(320, 150, 60, 35)
       self.btn24.clicked.connect(self.cancel)
 
   def cancel(self):
       self.reject()
 
 
class Encryptor:
   def __init__(self, key):
       self.key = key
 
   def pad(self, s):
       return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
 
   def encrypt(self, message, key, key_size=256):
       message = self.pad(message)
       iv = Random.new().read(AES.block_size)
       cipher = AES.new(key, AES.MODE_CBC, iv)
       return iv + cipher.encrypt(message)
 
   def encrypt_file(self, file_name):
       with open(file_name, 'rb') as fo:
           plaintext = fo.read()
       enc = self.encrypt(plaintext, self.key)
       with open(file_name + ".enc", 'wb') as fo:
           fo.write(enc)
       os.remove(file_name)
 
   def decrypt(self, ciphertext, key):
       iv = ciphertext[:AES.block_size]
       cipher = AES.new(key, AES.MODE_CBC, iv)
       plaintext = cipher.decrypt(ciphertext[AES.block_size:])
       return plaintext.rstrip(b"\0")
 
   def decrypt_file(self, file_name):
       with open(file_name, 'rb') as fo:
           ciphertext = fo.read()
       dec = self.decrypt(ciphertext, self.key)
       with open(file_name[:-4], 'wb') as fo:
           fo.write(dec)
       os.remove(file_name)
 
   def getAllFiles(self):
       dir_path = os.path.dirname(os.path.realpath(__file__))
       dirs = []
       for dirName, subdirList, fileList in os.walk(dir_path):
           for fname in fileList:
               if (fname != 'script.py' and fname != 'data.txt.enc'):
                   dirs.append(dirName + "\\" + fname)
       return dirs
 
   def encrypt_all_files(self):
       dirs = self.getAllFiles()
       for file_name in dirs:
           self.encrypt_file(file_name)
 
   def decrypt_all_files(self):
       dirs = self.getAllFiles()
       for file_name in dirs:
           self.decrypt_file(file_name)
 
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
global count
count=1
 
if __name__ == "__main__" :
   app = QApplication(sys.argv)
   window = MyWindow()
   window.show()
   app.exec_()
