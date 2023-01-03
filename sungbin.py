#test.
import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv

form_class = uic.loadUiType("inquiry.ui")[0]
class check(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('초등학교 인원')
        self.research_btn.clicked.connect(self.research)
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute('SELECT * FROM elementary')
        b = self.cursor.fetchall()
        self.table.setRowCount(len(b))
        self.table.setColumnCount(len(b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(b)):
            for j in range(len(b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(b[i][j])))



    def boom(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='pro', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM elementary')
        b = self.cursor.fetchall()
        self.table.setRowCount(len(b))
        self.table.setColumnCount(6)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(b)):
            for j in range(6):
                self.table.setItem(i,j,QTableWidgetItem(b[i][j]))
    def research(self):
        print("1")
        # b=[]
        # c = self.liner.text()
        # if self.combo_nation.currentText() == '선택안함':

        #
        #
        # for i in range(0,len(self.a)):
        #     b.append(self.a[i][idx])
        # self.d=[]
        #
        # count=0
        # self.index=[]
        # for i in range(0,len(self.a)):
        #     count+=1
            # if c in b[i]:
            #     self.d.append(self.a[i])
            #     self.index.append(count)
            # else:
            #     pass
            # count+=1
        #
        # self.book_btn.clicked.connect(self.book)
        # self.table.setRowCount(len(self.d))
        # self.table.setColumnCount(9)
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # for i in range(len(self.d)):
        #     for j in range(9):
        #         self.table.setItem(i, j, QTableWidgetItem(self.d[i][j]))
        # row = self.table.currentIndex().row()
        # self.t = self.d[row]
        # self.v = self.a.index(self.t)
        # self.a[row]=self.a[v]



    #
    # #
    # def exception(self):
    #     row = self.table.currentIndex().row()
    #     for i in range(len(self.a)):
    #         if self.a[i] == self.d[row]:
    #             print("111111111")
    #             self.a[i] = self.d[row]
    #         else:
    #             print("^1234^^^^^^^^^^^^^^^^^^^^^^")
    #     self.connect(self.book)
    # 예매하기 클릭 시





if __name__ == "__main__" :

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = check()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


