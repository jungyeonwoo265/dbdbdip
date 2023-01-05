import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

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

        self.b = self.cursor.fetchall()
        self.cursor.close()
        conn.close()
        self.table.setRowCount(len(self.b))
        self.table.setColumnCount(len(self.b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.b[i][j])))
    # def delete(self):
    #     print("1")
    def add_file(self):
        print("2")
        # ALTER TABLE `pro`.`elementary`



    def update(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()
        # self.cursor.execute('SELECT * FROM elementary')
        # self.b = self.cursor.fetchall()
        self.ro = self.table.currentIndex().row()
        self.col = self.table.currentIndex().column()
        money = self.b[self.ro][self.col]
        print(self.ro)
        print(self.b[self.ro][0])
        # print(d.text())
        # print(c)
        f = self.table.selectedItems()
        for i in f:
            print(i.text())
        print(f[0].text(), "!!!!!!!!!!")
        print(self.b[self.ro][0], "@@@@")
        sung=int(self.liner.text())
        # year=['2016년','2017년','2018년','2019년','2020년']
        self.cursor.execute("set SQL_SAFE_UPDATES = 0")
        year = self.combo_year.currentText()
        if year == "선택안함":
            self.cursor.execute(f'update elementary set {self.b[0][self.col]}년 = {sung} WHERE 행정구역별 ="{self.b[self.ro][0]}"')
        else:
            self.cursor.execute(f'update elementary set {year}년 = {sung} WHERE 행정구역별 ="{self.b[self.ro][0]}"')

        print("sunssssss")
        self.cursor.execute("set SQL_SAFE_UPDATES = 1")
        conn.commit()
        conn.close()
        # self.change_btn.connect(self.)

        # print(self.ro,self.col,"!!!!!!")

        self.table.setRowCount(len(self.b))
        self.table.setColumnCount(len(self.b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.b[i][j])))

    def research(self):

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()

        nation = self.combo_nation.currentText()
        year = self.combo_year.currentText()
        self.Header = ['행정구역별', year]
        # self.Header = list(map(str, self.c.fetchone()))
        # print(year)
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



        self.b = self.cursor.fetchall()
        print("sunccess")
        print(self.b[0])
        # print(b[0][self.col],"^^^^")
        # print(b[self.ro][0],"****")

        conn.close()

        self.table.setRowCount(len(self.b))
        self.table.setColumnCount(len(self.b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                self.table.setItem(i,j,QTableWidgetItem(str(self.b[i][j])))
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
