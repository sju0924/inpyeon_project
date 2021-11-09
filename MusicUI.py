import sys
from PyQt5.QtWidgets import (QApplication, QListWidget, QWidget, QGridLayout, QLabel, QLineEdit,QPushButton,QTextEdit,QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from src.Client.MusicClient import MusicClient,lyricClient

class MyUIApp(QWidget):
    
# 내용
    command = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.is_over = 0
        self.lst_code =[]
        #Listbox
        
        self.client = MusicClient()
        self.lyricclient = lyricClient()
    
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

        # 리스트
        self.searchBar = QLineEdit()
        self.btn_search = QPushButton('검색',self)
        self.btn_search.clicked.connect(self.searchMusic)
        
        self.MusicList =QListWidget()
        self.MusicList.itemDoubleClicked.connect(self.List_Clicked)
        #그리드 설정
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('음악 검색'), 0, 0,1,4)
        grid.addWidget(self.searchBar,1,0,1,3)
        grid.addWidget(self.btn_search,1,3)
        grid.addWidget(self.MusicList, 2,0,1,4)
        grid.addWidget(self.btn, 3,3)
        
        


        self.setWindowTitle('인편 전송기 ver0.0.1')
        self.setWindowIcon(QIcon('asset\캡처ss.PNG'))
        self.center()
        self.resize(600, 400)
        self.show()

    def searchMusic(self):
        self.client.clear()
        self.lst_code = []
        key = self.searchBar.text()
        data = self.client.searchMusicByTitle(key)

        for i in range(len(data[0])):
            data[1][i] = data[1][i].replace("<b>","")
            data[1][i] = data[1][i].replace("</b>","")
            self.MusicList.insertItem(i, data[1][i]+'-'+data[2][i])

        self.lst_code = data[0]

    def List_Clicked(self):
        item = self.MusicList.currentRow()
        code = self.lst_code[item]

        
        res = self.lyricclient.getLyricByCode(code)

        self.command.emit(res)
        self.close()

    def showModal(self):
        return super().exec_()



    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyUIApp()
   sys.exit(app.exec_())