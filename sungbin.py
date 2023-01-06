import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import pandas as pd

form_class = uic.loadUiType("inquiry.ui")[0]
class check(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('초등학교 인원')
        font_path = "c:\windows\Fonts\gulim.ttc"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)
        self.research_btn.clicked.connect(self.research)
        self.table.doubleClicked.connect(self.update)
        self.add_btn.clicked.connect(self.add_col)
        self.back_btn.clicked.connect(self.back)
        self.delete_btn.clicked.connect(self.delete_sel)
        self.stick_btn.clicked.connect(self.stick)
        self.checkBox.stateChanged.connect(self.choice_db)
        self.checkBox_2.stateChanged.connect(self.choice_db)
        self.checkBox_3.stateChanged.connect(self.choice_db)
        # self.first_csv = 'elementary'
        # self.formatted = self.first_csv
        #
        # conn = p.connect(host='localhost', port=3306, user='root', password='1234',
        #                  db='pro', charset='utf8')
        #
        # self.cursor = conn.cursor()
        # self.cursor.execute(f'SELECT * FROM {self.formatted}')
        #
        # self.b = self.cursor.fetchall()
        # self.cursor.close()
        # conn.close()
        # self.table.setRowCount(len(self.b))
        # self.table.setColumnCount(len(self.b[0]))
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # for i in range(len(self.b)):
        #     for j in range(len(self.b[0])):
        #         self.table.setItem(i, j, QTableWidgetItem(str(self.b[i][j])))

    def choice_db(self):
        self.first_csv = 'elementary'
        self.second_csv = 'solo'
        self.third_csv = 'new_marry'
        # box1 = self.checkBox.isChecked()
        # self.checkBox.released.connect(self.delete_sel)
        if self.checkBox.isChecked():
            pass

        elif self.checkBox_2.isChecked():
            self.first_csv=self.second_csv
            # self.third_csv=self.second_csv

            self.formatted =self.first_csv
            print(self.formatted,"1번조건")
        elif self.checkBox_3.isChecked():
            self.first_csv=self.third_csv
            # self.second_csv=self.third_csv

            # self.formatted = f'{first_csv} = {third_csv}'
            self.formatted =self.first_csv
            print(self.formatted,"2번조건")
            print("222")
        else:
            # self.second_csv=self.first_csv
            # self.third_csv = self.first_csv
            self.first_csv = self.first_csv


            self.formatted = self.first_csv
            print(self.formatted,"3번조건")
            print("333")


    def delete_sel(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()
        # self.cursor.execute('SELECT * FROM {self.formatted}')
        # self.b = self.cursor.fetchall()
        self.ro = self.table.currentIndex().row()
        self.col = self.table.currentIndex().column()
        money = self.b[self.ro][self.col]
        print(self.ro)
        print(self.b[self.ro][0])
        print("1")
        self.cursor.execute("set SQL_SAFE_UPDATES = 0")
        year = self.combo_year.currentText()
        if year == "선택안함":
            self.cursor.execute(f'update {self.formatted} set {self.b[0][self.col]}년 = NULL WHERE 행정구역별 ="{self.b[self.ro][0]}"')
        else:
            self.cursor.execute(f'update {self.formatted} set {year}년 = NULL WHERE 행정구역별 ="{self.b[self.ro][0]}"')

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

    def back(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute(f'ALTER TABLE `pro`.`{self.formatted}`DROP COLUMN `2021년`')
        conn.commit()
        conn.close()

        self.table.setRowCount(len(self.b))
        self.table.setColumnCount(len(self.b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.b[i][j])))

    def add_col(self):
        print("11111111111")

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')
        print("2222222222")
        self.cursor = conn.cursor()
        self.cursor.execute(f'ALTER TABLE `pro`.`{self.formatted}` ADD COLUMN `2021년` INT NULL DEFAULT NULL AFTER `2020년`')
        self.cursor.execute(f'update {self.formatted} set 2021년=case WHEN 행정구역별="행정구역별" THEN 2021 WHEN 행정구역별="전국" THEN 2672340 WHEN 행정구역별="서울특별시" THEN 399435 WHEN 행정구역별="부산광역시" THEN 153921 WHEN 행정구역별="대구광역시" THEN 121308 WHEN 행정구역별="인천광역시" THEN 155271 WHEN 행정구역별="광주광역시" THEN 84998 WHEN 행정구역별="대전광역시" THEN 77884 WHEN 행정구역별="울산광역시" THEN 66919 WHEN 행정구역별="세종특별자치시" THEN 30726 WHEN 행정구역별="경기도" THEN 763912  WHEN 행정구역별="강원도" THEN 72373 WHEN 행정구역별="충청북도" THEN 84263 WHEN 행정구역별="충청남도" THEN 118771 WHEN 행정구역별="전라북도" THEN 92914 WHEN 행정구역별="전라남도" THEN 91229 WHEN 행정구역별="경상북도" THEN 127912 WHEN 행정구역별="경상남도" THEN 189176  WHEN 행정구역별="제주특별자치도" THEN 41328  END')

        print("333333")

        conn.commit()
        conn.close()

        self.table.setRowCount(len(self.b))
        self.table.setColumnCount(len(self.b[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.b[i][j])))




    def update(self):

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()
        # self.cursor.execute('SELECT * FROM {self.formatted}')
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
        print(self.b[0][self.col],"^^^^^")
        print(self.col)
        print(self.b[self.ro][0], "@@@@")
        sung=int(self.liner.text())
        # year=['2016년','2017년','2018년','2019년','2020년']
        self.cursor.execute("set SQL_SAFE_UPDATES = 0")
        year = self.combo_year.currentText()
        if year == "선택안함":
            self.cursor.execute(f'update {self.formatted} set {self.b[0][self.col]}년 = {sung} WHERE 행정구역별 ="{self.b[self.ro][0]}"')
        else:
            self.cursor.execute(f'update {self.formatted} set {year}년 = {sung} WHERE 행정구역별 ="{self.b[self.ro][0]}"')

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
    def stick(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='pro', charset='utf8')

        self.cursor = conn.cursor()
        self.cursor.execute('SELECT * FROM ele_ratio')
        self.ele = self.cursor.fetchall()

        self.cursor.execute('SELECT * FROM marry_ratio')
        self.couple = self.cursor.fetchall()

        self.cursor.execute('SELECT * FROM solo')
        self.individual = self.cursor.fetchall()
        area = []
        # 비율
        percent = []
        for i in range(1,19):

            h=self.ele[i][0]
            k=self.ele[i][1]
            area.append(h)
            percent.append(k)

        percent_two = []
        for i in range(1, 19):
            co1 = self.couple[i][1]
            percent_two.append(co1)

        percent_three = []
        for i in range(1, 19):
            indi1 = (self.individual[i][1])/4
            percent_three.append(indi1)
        # 2016년
        # print(self.b[1][0],self.b[18][0],"@@@")
        # 도시지역
        # print(self.ele[1][0],self.ele[18][0],"!!!!")
        # 비율
        # print(self.b[1][1],self.b[18][1],"^^^")
        plt.rc('font',size=6)
        plt.figure(figsize=(15, 12))

        df=pd.DataFrame({'초등학생 비율':percent,'혼인율':percent_two,'1인가구 비율/4':percent_three},index=area)
        df
        bar_width=0.2

        index = np.arange(18)

        b1=plt.bar(index,df['초등학생 비율'], bar_width, alpha=0.4,color='b',label='초등학생 비율')
        b2=plt.bar(index+bar_width,df['혼인율'],bar_width,alpha=0.4,color='g',label='혼인율')
        b3=plt.bar(index+2*bar_width,df['1인가구 비율/4'],bar_width,alpha=0.4,color='r',label='1인가구 비율/4')

        plt.xticks(np.arange(bar_width,len(area)+bar_width,1),area)
        plt.xlabel('지역',size=10)
        plt.ylabel('인구수별 비율', size=10)
        plt.legend()



        plt.show()

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
            self.cursor.execute(f'SELECT * FROM {self.formatted}')
        # 지역 만 선택
        elif year=="선택안함":
            self.cursor.execute(f'SELECT * FROM {self.formatted} where 행정구역별= "{nation}"')
        # 연도만 선택
        elif nation=="선택안함":
            self.cursor.execute(f'SELECT 행정구역별,{year}년 FROM {self.formatted}')

        else:
            self.cursor.execute(f'SELECT 행정구역별,{year}년 FROM {self.formatted} WHERE 행정구역별 ="{nation}"')



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
