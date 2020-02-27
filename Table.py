from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from functools import partial 
from operator import ne
import sys

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TableView ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TableView(QTableWidget):
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ ++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, temp_data, *args):
        QTableWidget.__init__(self, *args)
        self.temp_data = temp_data
        self.setHeaders()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setSortingEnabled(False)
        self.setColumnWidth(0,500)
        self.setColumnWidth(1,120)
        self.setColumnWidth(2,120)
        self.setColumnWidth(4,500)
        self.setColumnWidth(5,360)
        self.setWordWrap(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.cellChanged.connect(self.tabEvent)
        #self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# +++++++++++++++++++++++++++++++++++++++++++++++++++ setHeaders +++++++++++++++++++++++++++++++++++++++++++++++++++
    def setHeaders(self):
        self.setHorizontalHeaderLabels(self.temp_data['header'])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ copy +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def copy(self):
        self.clip = QApplication.clipboard()
        self.selected = self.selectedRanges()
        t_row = []
        t_col = []
        for i in range(len(self.selected)):
            t_col.append(self.selected[i].leftColumn())
            t_row.append(self.selected[i].topRow())

        max_row = max(t_row) + 1
        min_row = min(t_row)

        max_col = max(t_col) + 1
        min_col = min(t_col)
     
        s = ""
        for r in range(min_row, max_row):
            #self.term(str(r))
            for c in range(min_col, max_col):
                #self.term(str(c))
                try:
                    s += str(self.item(r,c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"
        self.clip.setText(s)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ paste +++++++++++++++++++++++++++++++++++++++++++++++++++++ # data paste bug need fix
    def paste(self):
        try:
            #copied text is split by '\n' and '\t' to paste to the cells
            for r, row in enumerate(self.clip.text().split('\n')):
                for c, text in enumerate(row.split('\t')):
                    self.setItem(self.currentRow() + r, self.currentColumn() + c, QTableWidgetItem(text))
                    for table_item in self.temp_data['table']:
                        if table_item[0] == self.currentRow() + r and table_item[1] == self.currentColumn() + c:
                            table_item[2] = str(self.item(self.currentRow() + r, self.currentColumn() + c).text())
                        else:
                            self.temp_data['table'].append([self.currentRow() + r, self.currentColumn() + c, str(self.item(self.currentRow() + r, self.currentColumn() + c).text()),'',[],[],''])
                            break
            self.statusBarMessage('ჩაკვრა')
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ Insert Row ++++++++++++++++++++++++++++++++++++++++++++++++++
    def insRow(self):
        self.insertRow(self.currentRow())
        try:
            for j in range(len(self.temp_data['table'])):
                if self.temp_data['table'][j][0] >= self.currentRow():
                    self.temp_data['table'][j][0] = self.temp_data['table'][j][0] + 1
        except IndexError:
            pass
        
        for i in range(len(self.temp_data['Merge'])):
            if self.currentRow() <= self.temp_data['Merge'][i][0]:
                self.temp_data['Merge'][i][0] = self.temp_data['Merge'][i][0] + 1
# ++++++++++++++++++++++++++++++++++++++++++++++++ Delete table Row ++++++++++++++++++++++++++++++++++++++++++++++++
    def delRow(self):
        self.removeRow(self.currentRow())
        try:
            for item in self.temp_data['table']:
                if item[0] == self.currentRow():
                    self.temp_data['table'] = list(filter(partial(ne, item), self.temp_data['table']))
        except IndexError:
            pass

        try:
            for j in range(len(self.temp_data['table'])):                
                if self.temp_data['table'][j][0] >= self.currentRow():
                    self.temp_data['table'][j][0] = self.temp_data['table'][j][0] - 1
        except IndexError:
            pass
        
        for i in range(len(self.temp_data['Merge'])):
            if self.currentRow() < self.temp_data['Merge'][i][0]:
                self.temp_data['Merge'][i][0] = self.temp_data['Merge'][i][0] - 1

        for M_item in self.temp_data['Merge']:
            if M_item[0] == self.currentRow():
                self.temp_data['Merge'] = list(filter(partial(ne, M_item), self.temp_data['Merge']))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ merge +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def merge(self):
        r = []
        c = []
        for item in self.selectedIndexes():
            r.append(item.row())
            c.append(item.column())
        if len(r) > 0 or len(c) > 0:
            self.setSpan(r[0], c[0], max(r)-min(r)+1, max(c)-min(c)+1)
            t_Merge = [r[0], c[0], max(r)-min(r)+1, max(c)-min(c)+1]
        
        if t_Merge[2] != t_Merge[3]:
            self.temp_data['Merge'].append(t_Merge)
        else:
            for M_item in self.temp_data['Merge']:
                if t_Merge[0] == M_item[0] and t_Merge[1] == M_item[1]:
                    self.temp_data['Merge'] = list(filter(partial(ne, M_item), self.temp_data['Merge']))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Font +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def font(self):
        try:
            font, ok = QFontDialog.getFont()
            if ok:
                for item in self.selectedIndexes():
                    self.item(item.row(), item.column()).setFont(font)
                    for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[3] = font.toString()
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ color +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for item in self.selectedIndexes():
                try:
                    self.item(item.row(),item.column()).setForeground(QBrush(color))
                    for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[5] = list(color.getRgb())
                    self.statusBarMessage('ფერები')
                except AttributeError:
                    pass
# ++++++++++++++++++++++++++++++++++++++++++++++ Text bachground color +++++++++++++++++++++++++++++++++++++++++++++
    def FontBackColor(self):
        empty_cell = []
        BGColor = QColorDialog.getColor()
        for item in self.selectedIndexes():
            empty_cell = []
            try:
                self.item(item.row(),item.column()).setBackground(BGColor)
                for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[4] = list(BGColor.getRgb())
            except AttributeError:
                newitem = QTableWidgetItem(None)
                self.setItem(item.row(), item.column(), newitem)
                newitem.setBackground(BGColor)
                empty_cell.append(item.row())
                empty_cell.append(item.column())
                empty_cell.append(None)
                empty_cell.append('')
                empty_cell.append(list(BGColor.getRgb()))
                empty_cell.append([])
                empty_cell.append('C')
                self.temp_data['table'].append(empty_cell)
# +++++++++++++++++++++++++++++++++++++++++++++++++++ TABLE EVENT ++++++++++++++++++++++++++++++++++++++++++++++++++
    def tabEvent(self):
        try:
            item = self.item(self.currentRow(), self.currentColumn())
            self.value = item.text()
            if self.value is not '':
                if len(self.temp_data['table']) == 0:
                    self.temp_data['table'].append([self.currentRow(),self.currentColumn(),self.value,'Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'])
                    self.item(self.currentRow(), self.currentColumn()).setTextAlignment(Qt.AlignCenter)
                    list_font = QtGui.QFont()
                    list_font.fromString('Times New Roman,11,-1,5,50,0,0,0,0,0,Regular')
                    self.item(self.currentRow(), self.currentColumn()).setFont(list_font)
                else:
                    add = False
                    for table_item in self.temp_data['table']:
                        if table_item[0] == self.currentRow() and table_item[1] == self.currentColumn():
                            table_item[2] = str(self.value)
                            add = False
                            break
                        else:
                            add = True
                    if add == True:
                        self.temp_data['table'].append([self.currentRow(),self.currentColumn(),self.value,'Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'])
                        self.item(self.currentRow(), self.currentColumn()).setTextAlignment(Qt.AlignCenter)
                        list_font = QtGui.QFont()
                        list_font.fromString('Times New Roman,11,-1,5,50,0,0,0,0,0,Regular')
                        self.item(self.currentRow(), self.currentColumn()).setFont(list_font)
            else:
                for item in self.temp_data['table']:
                    if item[0] == self.currentRow() and item[1] == self.currentColumn():
                        self.temp_data['table'].remove(item)
            
        except AttributeError:
            pass
        #print("row--> {} && col --> {}".format(self.currentRow(), self.currentColumn()))
        #print("data>>> {}".format(self.temp_data['table']))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ Clear +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            for item in self.selectedIndexes():
                self.setItem(item.row(), item.column(), None)
                for table_item in self.temp_data['table']:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        self.temp_data['table'] = list(filter(partial(ne, table_item), self.temp_data['table']))

            #print("row--> {} && col --> {}".format(self.currentRow(), self.currentColumn()))
            #print("data>>> {}".format(self.temp_data['table']))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignLeft +++++++++++++++++++++++++++++++++++++++++++++++++++
    def alignLeft(self):
        try:
            if len(self.selectedIndexes()) != 0 :
                for item in self.selectedIndexes():
                    self.item(item.row(), item.column()).setTextAlignment(Qt.AlignLeft)
                    for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[6] = 'L'
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignRight ++++++++++++++++++++++++++++++++++++++++++++++++++
    def alignRight(self):
        try:
            if len(self.selectedIndexes()) != 0 :
                for item in self.selectedIndexes():
                    self.item(item.row(), item.column()).setTextAlignment(Qt.AlignRight)
                    for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[6] = 'R'
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignCenter +++++++++++++++++++++++++++++++++++++++++++++++++
    def alignCenter(self):
        try:
            if len(self.selectedIndexes()) != 0 :
                for item in self.selectedIndexes():
                    self.item(item.row(), item.column()).setTextAlignment(Qt.AlignCenter)
                    for table_item in self.temp_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[6] = 'C'
        except AttributeError:
            pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ openData +++++++++++++++++++++++++++++++++++++++++++++++++++
    def openData(self,temp_data):
        self.temp_data = temp_data
        for item in self.temp_data['table']:
            try:
                newitem = QTableWidgetItem(item[2])
                self.setItem(item[0], item[1], newitem)
            except IndexError:
                pass
            try:
                if item[6] != '':
                    if item[6] == 'C':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignCenter)
                    if item[6] == 'R':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignRight)
                    if item[6] == 'L':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignLeft)
            except IndexError:
                pass
            
            list_font = QtGui.QFont()
            try:
                if item[3] != "":
                    list_font.fromString(item[3])
                    self.item(item[0], item[1]).setFont(list_font)
            except IndexError:
                pass
            
            try:
                CellBgColor = QtGui.QColor(item[4][0],item[4][1],item[4][2],item[4][3])
                self.item(item[0], item[1]).setBackground(CellBgColor)
            except IndexError:
                pass

            try:
                TxtColor = QtGui.QColor(item[5][0],item[5][1],item[5][2],item[5][3])
                self.item(item[0], item[1]).setForeground(TxtColor)
            except IndexError:
                pass

        for index in self.temp_data['Merge']:
            self.setSpan(index[0], index[1], index[2], index[3])
                
        self.setHeaders()
############################################################################################################
if __name__ == '__main__':
    temp_data = { 'header':['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
              'config': {'tableColNumber' : 6,'language' : 'georgian','length': 500, 'width' : 500},
              'Merge':[],
              'table':[] }
    app = QApplication(sys.argv)
    #diag.exec_()
    #print (diag.applySettings())
    #print(ex.Row())
    ex = App('Bookmarks',50,30,1850,900,"img/link.png")
    ex = TableView(temp_data)
    ex.setCentralWidget(table)
    ex.show()
    sys.exit(app.exec_())