import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("inquiry.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # DB 연결
        db = p.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='3team', charset='utf8')
        self.c = db.cursor()

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.csv = list()
        self.db = 'elementary'
        self.header = '*'
        self.where = ''
        self.join = ''
        self.table_header1()

        self.research_btn.clicked.connect(self.search)
        self.checkBox.stateChanged.connect(self.choice_db)
        self.checkBox_2.stateChanged.connect(self.choice_db)
        self.checkBox_3.stateChanged.connect(self.choice_db)

    def search(self):
        if type(self.db) == str:
            self.condition1()
            self.single_search()
        else:
            self.condition2()
            self.multi_search()

    def condition1(self):
        city = self.combo_nation.currentText()
        year = self.combo_year.currentText()
        if city == '선택안함' and year == '선택안함':
            self.header = '*'
            self.join = ''
            self.where = ''
        elif year == '선택안함':
            self.header = '*'
            self.join = ''
            self.where = f'where 행정구역별 = "{city}"'
        elif city == '선택안함':
            self.header = f'행정구역별 , {year}년'
            self.join = ''
            self.where = ''
        else:
            self.header = f'행정구역별 , {year}년'
            self.join = ''
            self.where = f'where 행정구역별 = "{city}"'
        self.table_header1()

    def single_search(self):
        self.c.execute(f'select {self.header} from {self.db} {self.where};')
        csv_list = self.c.fetchall()
        city = self.combo_nation.currentText()
        if city == '선택안함':
            self.table.setRowCount(len(csv_list) - 1)
            self.table.setColumnCount(len(csv_list[0]))
            for i in range(len(csv_list[0])):
                self.table.setHorizontalHeaderItem(i, QTableWidgetItem(csv_list[0][i]))
            for i in range(len(csv_list) - 1):
                for j in range(len(csv_list[0])):
                    if j != 0 and self.db != 'solo':
                        self.table.setItem(i, j, QTableWidgetItem(f'{int(csv_list[i + 1][j]): ,}'))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i + 1][j]))
        else:
            self.table.setRowCount(len(csv_list))
            self.table.setColumnCount(len(csv_list[0]))
            for i in range(len(csv_list[0])):
                self.table.setHorizontalHeaderItem(i, QTableWidgetItem(self.csv[0][i]))
            for i in range(len(csv_list)):
                for j in range(len(csv_list[0])):
                    if j != 0 and self.db != 'solo':
                        self.table.setItem(i, j, QTableWidgetItem(f'{int(csv_list[i][j]): ,}'))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i][j]))

    def condition2(self):
        city = self.combo_nation.currentText()
        year = self.combo_year.currentText()
        # 2개
        # select / a.행정구역별, a.2016년, b.2016년 / from elementary as a
        # / inner join new_marry as b on a.행정구역별 = b.행정구역별 / where a.행정구역별 ='경기도';

        if len(self.db) == 2:
            if city == '선택안함':
                self.header = f'{self.db[0]}.행정구역별, {self.db[0]}.{year}년, {self.db[1]}.{year}년'
                self.join = f'inner join {self.db[1]} on {self.db[0]}.행정구역별 = {self.db[1]}.행정구역별'
                self.where = f''
            else:
                self.header = f'{self.db[0]}.행정구역별, {self.db[0]}.{year}년, {self.db[1]}.{year}년'
                self.join = f'inner join {self.db[1]} on {self.db[0]}.행정구역별 = {self.db[1]}.행정구역별'
                self.where = f'where {self.db[1]}.행정구역별 = "{city}"'

        # 3개
        # select / a.행정구역별, a.2016년, b.2016년, c.2016년 / from elementary as a
        # / inner join new_marry as b on a.행정구역별 = b.행정구역별
        # inner join solo as c on b.행정구역별 = c.행정구역별 / where a.행정구역별 ='경기도';

        else:
            if city == '선택안함':
                self.header = f'{self.db[0]}.행정구역별, {self.db[0]}.{year}년, {self.db[1]}.{year}년, {self.db[2]}.{year}년'
                self.join = f'inner join {self.db[1]} on {self.db[0]}.행정구역별 = {self.db[1]}.행정구역별 ' \
                            f'inner join {self.db[2]} on {self.db[1]}.행정구역별 = {self.db[2]}.행정구역별'
                self.where = f''
            else:
                self.header = f'{self.db[0]}.행정구역별, {self.db[0]}.{year}년, {self.db[1]}.{year}년, {self.db[2]}.{year}년'
                self.join = f'inner join {self.db[1]} on {self.db[0]}.행정구역별 = {self.db[1]}.행정구역별 ' \
                            f'inner join {self.db[2]} on {self.db[1]}.행정구역별 = {self.db[2]}.행정구역별'
                self.where = f'where {self.db[1]}.행정구역별 = "{city}"'
        self.table_header2()

    def multi_search(self):
        self.c.execute(f'select {self.header} from {self.db[0]} {self.join} {self.where};')
        csv_list = self.c.fetchall()
        city = self.combo_nation.currentText()
        if city == '선택안함':
            self.table.setRowCount(len(csv_list) - 1)
            self.table.setColumnCount(len(csv_list[0]))
            for i in range(len(csv_list[0])):
                self.table.setHorizontalHeaderItem(i, QTableWidgetItem(csv_list[0][i]))
            for i in range(len(csv_list) - 1):
                for j in range(len(csv_list[0])):
                    if j == 0:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i + 1][j]))
                    elif self.db[j-1] != 'solo':
                        self.table.setItem(i, j, QTableWidgetItem(f'{int(csv_list[i + 1][j]): ,}'))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i + 1][j]))
        else:
            self.table.setRowCount(len(csv_list))
            self.table.setColumnCount(len(csv_list[0]))
            for i in range(len(csv_list[0])):
                self.table.setHorizontalHeaderItem(i, QTableWidgetItem(self.csv[0][i]))
            for i in range(len(csv_list)):
                for j in range(len(csv_list[0])):
                    if j == 0:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i][j]))
                    elif self.db[j-1] != 'solo':
                        self.table.setItem(i, j, QTableWidgetItem(f'{int(csv_list[i][j]): ,}'))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(csv_list[i][j]))

    def table_header1(self):
        self.c.execute(f'select {self.header} from {self.db};')
        self.csv = self.c.fetchall()

    def table_header2(self):
        self.c.execute(f'select {self.header} from {self.db[0]} {self.join};')
        self.csv = self.c.fetchall()

    def choice_db(self):
        box1 = self.checkBox.isChecked()
        box2 = self.checkBox_2.isChecked()
        box3 = self.checkBox_3.isChecked()
        if box1 and box2 and box3:
            self.db = list()
            self.db.append('elementary')
            self.db.append('solo')
            self.db.append('new_marry')
            if self.combo_year.itemText(0) == '선택안함':
                self.combo_year.removeItem(0)
        elif box1 and box2:
            self.db = list()
            self.db.append('elementary')
            self.db.append('solo')
            if self.combo_year.itemText(0) == '선택안함':
                self.combo_year.removeItem(0)
        elif box1 and box3:
            self.db = list()
            self.db.append('elementary')
            self.db.append('new_marry')
            if self.combo_year.itemText(0) == '선택안함':
                self.combo_year.removeItem(0)
        elif box2 and box3:
            self.db = list()
            self.db.append('solo')
            self.db.append('new_marry')
            if self.combo_year.itemText(0) == '선택안함':
                self.combo_year.removeItem(0)
        elif self.checkBox.isChecked():
            self.db = str
            self.db = 'elementary'
            if self.combo_year.itemText(0) != '선택안함':
                self.combo_year.insertItem(0, '선택안함')
        elif self.checkBox_2.isChecked():
            self.db = str
            self.db = 'solo'
            if self.combo_year.itemText(0) != '선택안함':
                self.combo_year.insertItem(0, '선택안함')
        elif self.checkBox_3.isChecked():
            self.db = str
            self.db = 'new_marry'
            if self.combo_year.itemText(0) != '선택안함':
                self.combo_year.insertItem(0, '선택안함')
        else:
            self.db = str
            self.db = 'elementary'
            if self.combo_year.itemText(0) != '선택안함':
                self.combo_year.insertItem(0, '선택안함')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
