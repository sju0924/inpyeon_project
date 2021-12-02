#-*- coding:utf-8 -*- 
import sys
from PyQt5.QtWidgets import (QDialog,QMessageBox,QRadioButton,QApplication, QWidget, QGridLayout, QLabel, QLineEdit,QPushButton,QTextEdit,QDesktopWidget)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from src.Client.Client import Client 
from src.ui.MusicUI import MyUIApp
from src.ui.ModifyUI import MyModifyApp

class MyApp(QWidget):
# 내용
    
    def __init__(self):
        super().__init__()
        self.is_over = 0
        self.siteID = 'last2'
        self.mode = 'normal'
        self.letterseq = ""
        self.password =  ""

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

        pal = QPalette() 
        pal.setColor(QPalette.Background,QColor(250,250,250)) 
        self.setAutoFillBackground(True) 
        self.setPalette(pal)

        # 종료 버튼
        self.btn = QPushButton('종료', self)
        self.btn.setStyleSheet('QPushButton {background-color: rgb(80, 120, 200, 0.3);color:black;}')
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.box_content.textChanged.connect(lambda:self.countContentLen())
        #제출 버튼
        self.btn_submit = QPushButton('제출', self)
        self.btn_submit.clicked.connect(lambda:self.submitButtonclick())
        self.btn_submit.setStyleSheet('QPushButton {background-color: rgb(80, 120, 200, 0.3);color:black;}')

        #음악 
        self.btn_music = QPushButton('음악 검색', self)
        self.btn_music.clicked.connect(self.dialog_open)
        self.btn_music.setStyleSheet('QPushButton {background-color: rgb(150, 120, 200, 0.2);color:black;}')

        #수정
        self.btn_modify = QPushButton('목록 보기', self)
        self.btn_modify.clicked.connect(self.dialog_open2)
        self.btn_modify.setStyleSheet('QPushButton {background-color: rgb(150, 120, 200, 0.2);color:black;}')

        # 부대 설정
        self.rbtn1 = QRadioButton('기초군사훈련단', self)    
        self.rbtn1.setChecked(True)
        self.rbtn1.clicked.connect(self.groupboxRadFunction)

        self.rbtn2 = QRadioButton(self)        
        self.rbtn2.setText('특기학교')
        self.rbtn2.clicked.connect(self.groupboxRadFunction)

        


        #그리드 설정
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('공군 인편 작성기'), 0, 0)
        grid.addWidget(self.rbtn1, 0, 1)
        grid.addWidget(self.rbtn2, 0, 2)
        grid.addWidget(QLabel('도구'), 1, 0,1,2)
        grid.addWidget(self.btn_music,1,2)
        grid.addWidget(self.btn_modify,1,3)
        grid.addWidget(QLabel('작성자'), 2, 0)
        grid.addWidget(self.box_author, 2, 1)
        grid.addWidget(QLabel('관계'), 2, 2)
        grid.addWidget(self.box_relation, 2, 3)
        grid.addWidget(QLabel('주소'), 3, 0)
        grid.addWidget(self.box_Addr1, 3, 1,1,4)
        grid.addWidget(QLabel('상세주소'), 4, 0)
        grid.addWidget(self.box_Addr2, 4, 1)
        grid.addWidget(QLabel('우편번호'), 4, 2)
        grid.addWidget(self.box_postnum, 4, 3)
        grid.addWidget(QLabel('제목'),5, 0)
        grid.addWidget(self.box_title, 6, 0,1,4)
        grid.addWidget(QLabel('내용'), 7,0,1,4)
        grid.addWidget(self.box_content, 8,0,1,4)
        grid.addWidget(QLabel('비밀번호'),9, 0)
        grid.addWidget(self.box_password, 9, 1,1,3)
        grid.addWidget(self.label_count,10,3)
        grid.addWidget(self.btn, 11,0,1,2)
        grid.addWidget(self.btn_submit, 11,2,1,2)
        
        


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
        print(len(new_content))
        if(self.is_over==1):           
            new_content = new_content[:1200]

        print('송신자: ',self.SenderName, self.relation,self.Addr1,self.Addr2,self.postnum)
        print('내용 : ',self.title,new_content)

        self.client.Sender(self.Addr1,self.Addr2,self.postnum,self.SenderName,self.relation,self.password)
        #수정/일반 전송으로 분리
        if(self.mode == 'modify' and self.letterseq != "" and self.password != ""):
            res = self.client.ModifyContent(self.title,new_content,self.siteID,self.letterseq,self.password)  
            self.mode = 'normal'            
            self.letterseq = ""
            self.password = ""
            self.btn_submit.setText('제출')
        else:
            res = self.client.WriteContent(self.title,new_content,self.siteID)      
        
        
        if(res == 400):
             QMessageBox.information(self,'오류','전송에 실패했습니다.')
        
        
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

    def dialog_open2(self):
        self.win = MyModifyApp(self.siteID)
        self.win.command.connect(self.anyfunction2)

    def anyfunction(self, msg):
        self.box_content.setText(msg)

    def anyfunction2(self, msg):
        self.mode = 'modify'
        self.btn_submit.setText('수정')
        self.box_content.setText(msg['content'])
        self.box_author.setText(msg['author'])
        self.box_relation.setText(msg['relation'])
        self.box_Addr1.setText(msg['addr1'])
        self.box_Addr2.setText(msg['addr2'])
        self.box_postnum.setText(msg['postalcode'])
        self.box_password.setText(msg['password'])
        self.box_title.setText(msg['title'])
        self.letterseq = msg['letterseq']
        self.password = msg['password']

    def groupboxRadFunction(self) :
        if self.rbtn1.isChecked() : self.siteID = 'last2'
        elif self.rbtn2.isChecked() : self.siteID = 'haengjeong'

        print(self.siteID)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())