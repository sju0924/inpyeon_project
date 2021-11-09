import sys
from PyQt5.QtWidgets import (QDialog,QApplication, QWidget, QGridLayout, QLabel, QLineEdit,QPushButton,QTextEdit,QDesktopWidget)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from src.Client.Client import Client 
from MusicUI import MyUIApp

class MyApp(QWidget):
    
# 내용
    
    def __init__(self):
        super().__init__()
        self.is_over = 0

        #내용 textbox
        self.box_title = QLineEdit()
        self.box_content = QTextEdit()

        # 작성자 textbox
        self.box_author = QLineEdit()
        self.box_relation = QLineEdit()
        self.box_Addr1 = QLineEdit()


        self.box_Addr2 = QLineEdit()
        self.box_postnum = QLineEdit()
        self.box_password = QLineEdit()
        self.label_count = QLabel()
        self.label_count.setText('0/1200자')

        self.initUI()
        self.client = Client()
        self.dialog = QDialog()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        # 종료 버튼
        self.btn = QPushButton('종료', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.box_content.textChanged.connect(lambda:self.countContentLen())
        #제출 버튼
        self.btn_submit = QPushButton('제출', self)
        self.btn_submit.clicked.connect(lambda:self.submitButtonclick())

        #음악 
        self.btn_music = QPushButton('음악 검색', self)
        self.btn_music.clicked.connect(self.dialog_open)

        #그리드 설정
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('공군 인편 작성기'), 0, 0,1,2)
        grid.addWidget(self.btn_music,0,3)
        grid.addWidget(QLabel('작성자'), 1, 0)
        grid.addWidget(self.box_author, 1, 1)
        grid.addWidget(QLabel('관계'), 1, 2)
        grid.addWidget(self.box_relation, 1, 3)
        grid.addWidget(QLabel('주소'), 2, 0)
        grid.addWidget(self.box_Addr1, 2, 1,1,4)
        grid.addWidget(QLabel('상세주소'), 3, 0)
        grid.addWidget(self.box_Addr2, 3, 1)
        grid.addWidget(QLabel('우편번호'), 3, 2)
        grid.addWidget(self.box_postnum, 3, 3)
        grid.addWidget(QLabel('제목'),4, 0)
        grid.addWidget(self.box_title, 5, 0,1,4)
        grid.addWidget(QLabel('내용'), 6,0,1,4)
        grid.addWidget(self.box_content, 7,0,1,4)
        grid.addWidget(QLabel('비밀번호'),8, 0)
        grid.addWidget(self.box_password, 8, 1,1,3)
        grid.addWidget(self.label_count,9,3)
        grid.addWidget(self.btn, 10,0,1,2)
        grid.addWidget(self.btn_submit, 10,2,1,2)
        
        


        self.setWindowTitle('인편 전송기 ver0.0.1')
        self.setWindowIcon(QIcon('asset\캡처ss.PNG'))
        self.center()
        self.resize(600, 400)
        self.show()

    def clearBox(self):
        

        if(self.is_over == 1):
            self.box_content.setText(self.content[1200:])
        else:
            self.box_content.setText("")
            self.box_author.setText("")
            self.box_relation.setText("")
            self.box_Addr1.setText("")
            self.box_Addr2.setText("")
            self.box_postnum.setText("")
            self.box_password.setText("")
            self.box_title.setText("")

    def getBox(self):
        self.SenderName = self.box_author.text()
        self.relation = self.box_relation.text()
        self.Addr1 = self.box_Addr1.text()
        self.Addr2 = self.box_Addr2.text()
        self.postnum = self.box_postnum.text()
        self.password = self.box_password.text()

        self.title = self.box_title.text()
        self.content = self.box_content.toPlainText()

        return self.content

    def submitButtonclick(self):
        
        new_content = self.getBox()
        if(self.is_over == 1):
            new_content = new_content[:1200]
            self.box_content

        print('송신자: ',self.SenderName, self.relation,self.Addr1,self.Addr2,self.postnum)
        print('내용 : ',self.title,new_content)
        self.client.Sender(self.Addr1,self.Addr2,self.postnum,self.SenderName,self.relation,self.password)
        self.client.WriteContent(self.title,new_content)

        self.clearBox()


    def countContentLen(self):
        length = len(self.box_content.toPlainText())
        self.label_count.setText(str(length)+ '/1200자')
        if(length>1200):
            self.is_over = 1
            self.btn_submit.setText('제출(1200자)')
        elif(length<=1200 and self.is_over == 1):
            self.btn_submit.setText('제출')
            self.is_over = 0

    def dialog_open(self):
        self.win = MyUIApp()
        self.win.command.connect(self.anyfunction)

    def anyfunction(self, msg):
        self.box_content.setText(msg)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())