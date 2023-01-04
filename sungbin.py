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
        self.table.doubleClicked.connect(self.update)

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()
        self.cursor.execute('SELECT * FROM elementary')

        b = self.cursor.fetchall()
        # self.cursor.close()
        self.table.setRowCount(len(b))
        self.table.setColumnCount(len(b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(b)):
            for j in range(len(b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(b[i][j])))



    # def boom(self):
    #     conn = p.connect(host='localhost', port=3306, user='root', password='1234',
    #                           db='pro', charset='utf8')
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute('SELECT * FROM elementary')
    #     b = self.cursor.fetchall()
    #     self.table.setRowCount(len(b))
    #     self.table.setColumnCount(6)
    #     self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    #     for i in range(len(b)):
    #         for j in range(6):
    #             self.table.setItem(i,j,QTableWidgetItem(str(b[i][j])))
    # def update(self):
        # year=['2016년','2017년','2018년','2019년','2020년']
        # nation=[]
        # self.Header = ['행정구역별', year]
        #
        # print("11")
        # b = self.cursor.fetchall()
        # print("22")
        # self.ro = self.table.currentIndex().row()
        # self.col = self.table.currentIndex().column()
        # c = b[self.ro][self.col]
        # print(c)

        # a=self.table.currentRow()
        # d=self.table.currentColumn()
        # print(b[0])
        # print(b[a][d])
        # print(c)
        # print(a,d)
        # f=self.selecteditems()

        # e=self.sele
        # self.horizontalHeaderItem(d)
        # self.table.setHorizontalHeaderLabels(self.Header)



        # a=self.table.currentitem()
        # print(a.text())

        # self.cursor.execute('SELECT * FROM elementary')
        # self.cursor.execute(f'SELECT 행정구역별 FROM elementary WHERE 행정구역별 ="{nation}"')
        # self.cursor.execute(f'update elementary set 행정구역별='{c}'  WHERE 행정구역별 ="{text}"')



    def research(self):
        nation = self.combo_nation.currentText()
        year = self.combo_year.currentText()
        self.Header = ['행정구역별', year]
        # self.Header = list(map(str, self.c.fetchone()))
        print(year)
        if nation=="선택안함" and year=="선택안함":
            self.cursor.execute('SELECT * FROM elementary')
        # 지역 만 선택
        elif year=="선택안함":
            self.cursor.execute(f'SELECT * FROM elementary where 행정구역별= "{nation}"')
        # 연도만 선택
        elif nation=="선택안함":
            self.cursor.execute(f'SELECT 행정구역별,{year}년 FROM elementary')

        else:
            self.cursor.execute(f'SELECT 행정구역별,{year}년 FROM elementary WHERE 행정구역별 ="{nation}"')

        b = self.cursor.fetchall()
        # self.cursor.close()
        self.table.setRowCount(len(b))
        self.table.setColumnCount(len(b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(b)):
            for j in range(len(b[0])):
                self.table.setItem(i,j,QTableWidgetItem(str(b[i][j])))
        self.table.setHorizontalHeaderLabels(self.Header)














if __name__ == "__main__" :

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = check()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
