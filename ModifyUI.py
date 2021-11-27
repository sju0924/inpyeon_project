import sys
from PyQt5.QtWidgets import (QApplication, QSpinBox,QListWidget, QWidget, QGridLayout, QLabel, QLineEdit,QPushButton,QTextEdit,QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from src.Client.ListClient import ListClient
from src.Client.Client import Client

class MyModifyApp(QWidget):
    
# 내용
    command = QtCore.pyqtSignal(dict)
    def __init__(self,siteId):
        super().__init__()
        self.is_over = 0
        self.lst_code =[]
        self.lst_title =[]
        self.lst_author =[]
        self.siteId = siteId
        self.page = 1
        #Listbox
        self.item=0
        self.client = ListClient()
        self.client2 = Client()
    
        self.initUI()
        


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        # 종료 버튼
        self.btn = QPushButton('종료', self)
        self.btn.clicked.connect(self.close)
        
        # 인편 리스트
        self.LetterList =QListWidget()
        self.LetterList.itemDoubleClicked.connect(self.List_Clicked)

        # 페이지 검색
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.searchLetter)

        # 비밀번호 입력 후 수정
        self.passwordbar = QLineEdit()
        self.btn_submit = QPushButton('조회', self)
        self.btn_submit.clicked.connect(self.submit)

        # 삭제
        self.btn_delete = QPushButton('삭제', self)
        self.btn_delete.clicked.connect(self.delete)

        #그리드 설정
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('인편 검색'), 0, 0,1,4)
        grid.addWidget(self.LetterList, 1,0,1,4)
        grid.addWidget(self.btn, 1,3)

        grid.addWidget(QLabel('페이지'), 2, 0)
        grid.addWidget(self.spinbox, 2,1)
        
        grid.addWidget(QLabel('비밀번호'), 3, 0)
        grid.addWidget(self.passwordbar, 3,1)
        grid.addWidget(self.btn_submit, 3,2)
        grid.addWidget(self.btn_delete, 3,3)

    

        self.setWindowTitle('인편 전송기 ver0.0.1')
        self.setWindowIcon(QIcon('asset\캡처ss.PNG'))
        self.center()
        self.resize(600, 400)
        self.show()

    def searchLetter(self):
        self.client.clear()
        self.LetterList.clear()
        self.lst_code =[]
        self.lst_title =[]
        self.lst_author =[]
        self.lst_relation =[]
        
        data = self.client.searchletter(self.siteId,self.spinbox.value())

        for i in range(len(data[0])):
            self.LetterList.insertItem(i, data[1][i]+'-'+data[2][i]+" | "+data[3][i])

        self.lst_code = data[0]
        self.lst_title = data[1]
        self.lst_author = data[2]
        self.lst_relation = data[4]

    def List_Clicked(self):
        self.item = self.LetterList.currentRow()
        
        
    def submit(self):
        code = self.lst_code[self.item]
        res = self.client.getLetter(code,self.spinbox.value(),self.passwordbar.text())
        if(len(res) == 0):

            print('전송 오류 : ',res)
            return 400
        res['title'] = self.lst_title[self.item]
        res['author'] = self.lst_author[self.item]
        res['relation'] = self.lst_relation[self.item]
        res['password'] = self.passwordbar.text()
        self.command.emit(res)
        self.close()

    def delete(self):
        res = self.client2.deleteContent(self.siteId,self.lst_code[self.item],self.passwordbar.text(),self.spinbox.value())
        if(res == 200):
            print('삭제 성공')

        self.searchLetter()
        self.passwordbar.setText("")

    def showModal(self):
        return super().exec_()



    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyModifyApp()
   sys.exit(app.exec_())