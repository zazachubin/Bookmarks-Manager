from PyQt5.QtWidgets import QApplication, QHeaderView, QDialog, QLineEdit, QPushButton, QHBoxLayout, QColorDialog, QFontDialog, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor, QBrush
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from functools import partial 
from operator import ne
import sys
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ insert column name ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HeaderName(QDialog):
    def __init__(self, header, column, parent = None):
        QDialog.__init__(self, parent)
        self.header = header
        self.column = column
        self.setWindowTitle("სვეტის დასახელება")                                # call method which sets window title
        self.setWindowIcon(QtGui.QIcon("img/finance.png"))                      # Set main window icon
        hbox = QHBoxLayout()
        self.textbox = QLineEdit(self)
        self.Ok = QPushButton('დადასტურება', self)
        self.Can = QPushButton('გაუქმება', self)
        self.textbox.setText(self.header[self.column])

        #hbox.addWidget(self.LabelColumn)
        hbox.addWidget(self.textbox)
        hbox.addWidget(self.Ok)
        hbox.addWidget(self.Can)
        self.setLayout(hbox)

        self.Ok.clicked.connect(self.applyHeader)
        self.Can.clicked.connect(self.CancelHeader)
        self.show()
# ++++++++++++++++++++++++++++++++++++++++++++++++ Apply header_1 text +++++++++++++++++++++++++++++++++++++++++++++
    def applyHeader(self):
        mes = self.textbox.text()
        self.header.insert(self.column + 1, mes)
        self.header.remove(self.header[self.column])
        self.close()
        #return self.header
# ++++++++++++++++++++++++++++++++++++++++++++++++ Cancel header text ++++++++++++++++++++++++++++++++++++++++++++++
    def CancelHeader(self):
        self.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TableView ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TableView(QTableWidget):
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ ++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, table_data, col_width_array, *args):
        QTableWidget.__init__(self, *args)
        self.col_width_array = col_width_array
        self.table_data = table_data
        self.selected_items = []
        self.setHeaders()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setSortingEnabled(False)
        for key in self.col_width_array:
            self.setColumnWidth(key,self.col_width_array[key])
        self.setWordWrap(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.cellChanged.connect(self.tabEvent)
        self.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)
        #self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# +++++++++++++++++++++++++++++++++++++++++++++++++++ setHeaders +++++++++++++++++++++++++++++++++++++++++++++++++++
    def setHeaders(self):
        self.setHorizontalHeaderLabels(self.table_data['header'])
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
            for c in range(min_col, max_col):
                try:
                    s += str(self.item(r,c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"
        self.clip.setText(s)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ paste +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def paste(self):
        try:
            #copied text is split by '\n' and '\t' to paste to the cells
            copyText = self.clip.text().split('\n')
            copyText.remove('')
            for r, row in enumerate(copyText):
                for c, text in enumerate(row.split('\t')):
                    self.setItem(self.currentRow() + r, self.currentColumn() + c, QTableWidgetItem(text))
                    self.item(self.currentRow() + r, self.currentColumn() + c).setTextAlignment(Qt.AlignCenter)
                    list_font = QtGui.QFont()
                    list_font.fromString('MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular')
                    self.item(self.currentRow() + r, self.currentColumn() + c).setFont(list_font)
                    for table_item in self.table_data['table']:
                        if table_item[0] == self.currentRow() + r and table_item[1] == self.currentColumn() + c:
                            table_item[2] = str(self.item(self.currentRow() + r, self.currentColumn() + c).text())
                        else:
                            self.table_data['table'].append([self.currentRow() + r, self.currentColumn() + c, str(self.item(self.currentRow() + r, self.currentColumn() + c).text()),'MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'])
                            break
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ Insert Row ++++++++++++++++++++++++++++++++++++++++++++++++++
    def insRow(self):
        selected_Row = self.currentRow()
        try:
            for item in self.table_data['table']:
                if item[0] >= selected_Row:
                    item[0] += 1
            self.insertRow(selected_Row)
        except:
            pass
        
        for item in self.table_data['Merge']:
            if selected_Row <= item[0]:
                item[0] += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++ Delete table Row ++++++++++++++++++++++++++++++++++++++++++++++++
    def delRow(self):
        selected_Row = self.currentRow()
        try:
            for item in self.table_data['table']:
                if item[0] == selected_Row:
                    self.table_data['table'] = list(filter(partial(ne, item), self.table_data['table']))
            self.removeRow(selected_Row)
        except:
            pass

        try:
            for item in self.table_data['table']:
                if item[0] >= selected_Row:
                    item[0] -= 1
        except:
            pass

        for M_item in self.table_data['Merge']:
            if M_item[0] == selected_Row:
                self.table_data['Merge'] = list(filter(partial(ne, M_item), self.table_data['Merge']))

        for item in self.table_data['Merge']:
            if selected_Row <= item[0]:
                item[0] -= 1
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
            self.table_data['Merge'].append(t_Merge)
        else:
            for M_item in self.table_data['Merge']:
                if t_Merge[0] == M_item[0] and t_Merge[1] == M_item[1]:
                    self.table_data['Merge'] = list(filter(partial(ne, M_item), self.table_data['Merge']))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Font +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            for item in self.selectedIndexes():
                try:
                    self.item(item.row(), item.column()).setFont(font)
                    for table_item in self.table_data['table']:
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
                    for table_item in self.table_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[5] = list(color.getRgb())
                except AttributeError:
                    pass
# ++++++++++++++++++++++++++++++++++++++++++++++ Text bachground color +++++++++++++++++++++++++++++++++++++++++++++
    def FontBackColor(self):
        BGColor = QColorDialog.getColor()
        for item in self.selectedIndexes():
            try:
                self.item(item.row(),item.column()).setBackground(BGColor)
                if list(BGColor.getRgb()) != list([255,255,255,255]):
                    for table_item in self.table_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[4] = list(BGColor.getRgb())
                else:
                    for table_item in self.table_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[4] = []
                        if table_item[2] == None:
                            self.table_data['table'] = list(filter(partial(ne, table_item), self.table_data['table']))

            except AttributeError:
                newitem = QTableWidgetItem(None)
                self.setItem(item.row(), item.column(), newitem)
                newitem.setBackground(BGColor)
                if list(BGColor.getRgb()) != list([255,255,255,255]):
                    self.table_data['table'].append([item.row(),item.column(),None,'',list(BGColor.getRgb()),[],'C'])
# +++++++++++++++++++++++++++++++++++++++++++++++++++ TABLE EVENT ++++++++++++++++++++++++++++++++++++++++++++++++++
    def tabEvent(self):
        try:
            item = self.item(self.currentRow(), self.currentColumn())
            self.value = item.text()
            if self.value is not '':
                if len(self.table_data['table']) == 0:
                    self.table_data['table'].append([self.currentRow(),self.currentColumn(),self.value,'MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'])
                    self.item(self.currentRow(), self.currentColumn()).setTextAlignment(Qt.AlignCenter)
                    list_font = QtGui.QFont()
                    list_font.fromString('MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular')
                    self.item(self.currentRow(), self.currentColumn()).setFont(list_font)
                else:
                    add = False
                    for table_item in self.table_data['table']:
                        if table_item[0] == self.currentRow() and table_item[1] == self.currentColumn():
                            table_item[2] = str(self.value)
                            add = False
                            break
                        else:
                            add = True
                    if add == True:
                        self.table_data['table'].append([self.currentRow(),self.currentColumn(),self.value,'MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'])
                        self.item(self.currentRow(), self.currentColumn()).setTextAlignment(Qt.AlignCenter)
                        list_font = QtGui.QFont()
                        list_font.fromString('MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular')
                        self.item(self.currentRow(), self.currentColumn()).setFont(list_font)
            else:
                for item in self.table_data['table']:
                    if item[0] == self.currentRow() and item[1] == self.currentColumn():
                        self.table_data['table'].remove(item)
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++ Calculations ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def calculations(self,table_data):
        self.table_data = table_data
        calc_col1 = []
        calc_col2 = []
        for item in self.table_data['table']:
            if item[1] == 1 and item[2] != None :
                calc_col1.append(item[2])

        for item in self.table_data['table']:
            if item[1] == 2 and item[2] != None :
                calc_col2.append(item[2])
        calc = []
        for i in range(len(calc_col2)):
            try:
                newitem = QTableWidgetItem(str(int(calc_col1[i])/int(calc_col2[i])*100) + "%")
                self.setItem(i, 3, newitem)
                calc.append(str(int(calc_col1[i])/int(calc_col2[i])*100))
            except ZeroDivisionError:
                newitem = QTableWidgetItem('Inf')
                self.setItem(i, 3, newitem)
                calc.append(str("Inf"))
            except ValueError:
                newitem = QTableWidgetItem('clock')
                self.setItem(i, 3, newitem)
                calc.append(str("clock"))
            except IndexError:
                pass

        return calc_col1, calc_col2, calc
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ Clear +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            for item in self.selectedIndexes():
                self.setItem(item.row(), item.column(), None)
                for table_item in self.table_data['table']:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        self.table_data['table'] = list(filter(partial(ne, table_item), self.table_data['table']))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignLeft +++++++++++++++++++++++++++++++++++++++++++++++++++
    def alignLeft(self):
        try:
            if len(self.selectedIndexes()) != 0 :
                for item in self.selectedIndexes():
                    self.item(item.row(), item.column()).setTextAlignment(Qt.AlignLeft)
                    for table_item in self.table_data['table']:
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
                    for table_item in self.table_data['table']:
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
                    for table_item in self.table_data['table']:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[6] = 'C'
        except AttributeError:
            pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ openData +++++++++++++++++++++++++++++++++++++++++++++++++++
    def openData(self,table_data):
        self.table_data = table_data
        for item in self.table_data['table']:
            try:
                newitem = QTableWidgetItem(item[2])
                self.setItem(item[0], item[1], newitem)
            except:
                pass

            try:
                if item[6] != '':
                    if item[6] == 'C':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignCenter)
                    if item[6] == 'R':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignRight)
                    if item[6] == 'L':
                        self.item(item[0], item[1]).setTextAlignment(Qt.AlignLeft)
            except:
                pass
            
            list_font = QtGui.QFont()
            try:
                if item[3] != "":
                    list_font.fromString(item[3])
                    self.item(item[0], item[1]).setFont(list_font)
            except:
                pass
            
            try:
                CellBgColor = QtGui.QColor(item[4][0],item[4][1],item[4][2],item[4][3])
                self.item(item[0], item[1]).setBackground(CellBgColor)
            except:
                pass

            try:
                TxtColor = QtGui.QColor(item[5][0],item[5][1],item[5][2],item[5][3])
                self.item(item[0], item[1]).setForeground(TxtColor)
            except:
                pass

        for index in self.table_data['Merge']:
            self.setSpan(index[0], index[1], index[2], index[3])
                
        self.setHeaders()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ Finde item ++++++++++++++++++++++++++++++++++++++++++++++++++
    def find_items(self, text):
        if text != "":
            if len(self.selected_items) != 0:
                for item in self.selected_items:
                    CellBgColor = QtGui.QColor(0,0,0,0)
                    self.item(item.row(), item.column()).setBackground(CellBgColor)
            for item in self.table_data['table']:
                try:
                    CellBgColor = QtGui.QColor(item[4][0],item[4][1],item[4][2],item[4][3])
                    self.item(item[0], item[1]).setBackground(CellBgColor)
                except:
                    pass
            self.selected_items = self.findItems(text, QtCore.Qt.MatchContains)

            selected_items_rowArr = []
            for item in self.selected_items:
                selected_items_rowArr.append(item.row())

            if len(selected_items_rowArr) != 0:
                startItemRow = min(selected_items_rowArr)
                self.selectRow(startItemRow)

            for item in self.selected_items:
                CellBgColor = QtGui.QColor(255,0,0,255)
                self.item(item.row(), item.column()).setBackground(CellBgColor)
        else:
            if len(self.selected_items) != 0:
                for item in self.selected_items:
                    CellBgColor = QtGui.QColor(0,0,0,0)
                    self.item(item.row(), item.column()).setBackground(CellBgColor)
            for item in self.table_data['table']:
                try:
                    CellBgColor = QtGui.QColor(item[4][0],item[4][1],item[4][2],item[4][3])
                    self.item(item[0], item[1]).setBackground(CellBgColor)
                except:
                    pass
            self.selected_items = []
        return len(self.selected_items)
# ++++++++++++++++++++++++++++++++++++++++++++++++ change header name ++++++++++++++++++++++++++++++++++++++++++++++
    def changeHorizontalHeader(self):
        col = self.currentColumn()
        diag = HeaderName(self.table_data['header'], col)
        diag.exec_()
        self.setHeaders()
####################################################################################################################
if __name__ == '__main__':
    data_tab1 = { 'header':['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
                  'Merge':[],
                  'table':[] }
    app = QApplication(sys.argv)
    col_width_array_tab1 = {0 : 500, 1 : 120, 2 : 120, 4 : 500, 5 : 360}
    ex = TableView(data_tab1, col_width_array_tab1, 10, len(data_tab1['header']))
    ex.show()
    sys.exit(app.exec_())