import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit,QPushButton,QTextEdit,QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication,Qt
from Client import Client 

class MyApp(QWidget):

# 내용
    
    def __init__(self):
        super().__init__()
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

        self.initUI()
        self.client = Client()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        # 종료 버튼
        self.btn = QPushButton('Quit', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)
        self.box_content.textChanged.connect(lambda:self.countContentLen())
        #제출 버튼
        self.btn_submit = QPushButton('제출', self)
        self.btn_submit.clicked.connect(lambda:self.submitButtonclick())
        
        #그리드 설정
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('공군 인편 작성기'), 0, 0,1,4)
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

    def submitButtonclick(self):
        self.SenderName = self.box_author.text()
        self.relation = self.box_relation.text()
        self.Addr1 = self.box_Addr1.text()
        self.Addr2 = self.box_Addr2.text()
        self.postnum = self.box_postnum.text()
        self.password = self.box_password.text()

        self.title = self.box_title.text()
        self.content = self.box_content.toPlainText()

        print('송신자: ',self.SenderName, self.relation,self.Addr1,self.Addr2,self.postnum)
        print('내용 : ',self.title,self.content)
        self.client.Sender(self.Addr1,self.Addr2,self.postnum,self.SenderName,self.relation,self.password)
        self.client.WriteContent(self.title,self.content)

        self.box_author.setText("")
        self.relation = self.box_relation.setText("")
        self.Addr1 = self.box_Addr1.setText("")
        self.Addr2 = self.box_Addr2.setText("")
        self.postnum = self.box_postnum.setText("")
        self.password = self.box_password.setText("")

        self.title = self.box_title.setText("")
        self.content = self.box_content.setText("")

    def countContentLen(self):
        self.label_count.setText(str(len(self.box_content.toPlainText()))+ '/1200자')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())