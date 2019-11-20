##!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------- Libraries ---------------------------------------------------
import datetime
import pickle
import time
import json
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QRadioButton, QItemDelegate, QInputDialog, QHeaderView, QComboBox, QFileDialog, QColorDialog, QGroupBox, QDialog, QFontDialog, QPlainTextEdit, QProgressBar, QLineEdit, QSplitter, QLabel, QSizePolicy, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QColor, QBrush
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QDate, QDir, QSettings
from functools import partial 
from operator import ne
# ---------------------------------------------------- Variables ---------------------------------------------------
data = {'header': ['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
        'Merge' : [[0, 0, 1, 6],[2, 0, 1, 6],[4, 0, 1, 6]],
        'config': {'tableColNumber' : 6,'language' : 'georgian'},
        'table' : [[0,0,'LabVIEW','',[190, 192, 200, 255],[],'C'],
                   [1,0,'Labview tutorial Enable integration','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [1,1,'42','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [1,2,'42','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [1,4,r'https://www.youtube.com/playlist?list=PLdNp0fxltzmPvvK_yjX-XyYgfVW8WK4tu','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [1,5,'გაკვეთილი','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [2,0,'Qt C++','',[190, 192, 200, 255],[],'C'],
                   [3,0,'Udemy - C Plus Plus programming in Qt FrameWork Part I','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [3,1,'8','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [3,2,'11','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [3,4,r'D:\Courses\Programing\C\Qt_C++\Udemy - C Plus Plus programming in Qt FrameWork Part I','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [3,5,'001 QMainWindow Structure','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [4,0,'ფიზიკა','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
                   [5,0,'ზოგადი ფიზიკის კურსი I ტომი','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [5,1,'395','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [5,2,'490','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [5,4,r'D:\Library\ფიზიკა\ზოგადი ფიზიკის კურსი  I ტომი.pdf','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [6,0,'EPD ამაჩქარლების ფიზიკა','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [6,1,'38','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [6,2,'366','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                   [6,4,r'D:\Library\ამაჩქარებლები\EPD ამაჩქარლების ფიზიკა.pdf','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C']]}
tt = True
tf = True
ts = True
table = ""
langvage = "ქართული"
config = ""
progressBar = []
col = 0
OpenPath = ""
# ------------------------------------------------- Temporary data -------------------------------------------------
temp_data = { 'header':['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
              'config': {'tableColNumber' : 6,'language' : 'georgian'},
              'Merge':[], 
              'table':[] }
temp_header = temp_data['header']
temp_Merge = temp_data['Merge']
temp_table = temp_data['table']
temp_config = temp_data['config']
# ------------------------------------------------------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Settings Dialog ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Settings(QDialog):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ +++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self,parent = None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("პარამეტრები")
        self.setWindowIcon(QtGui.QIcon("settings.png"))                     # Set main window icon
        self.groupBox = QGroupBox("ენა")                                    # create groupbox with lane
        self.groupBox.setAlignment(Qt.AlignCenter)
 
        VLbox = QVBoxLayout()
        VLbox.addWidget(self.groupBox)

        hboxLayout = QHBoxLayout()

        self.radioButton1 = QRadioButton("ქართული")                       # create radiobutton1
        self.radioButton1.setChecked(True)                                 # set radiobutton1 as default ticked
        self.radioButton1.setIcon(QtGui.QIcon("img/georgia.png"))          # set icon on radiobutton1
        self.radioButton1.setIconSize(QtCore.QSize(40,40))                 # set icon size
        #self.radioButton1.setFont(QtGui.QFont("Acadnusx",13))             # set radiobutton1 font and size
        self.radioButton1.toggled.connect(self.geo)                        # create radiobutton1 and "OnRadioBtn" function conection
        hboxLayout.addWidget(self.radioButton1)                            # add radiobutton1 in horizontal layout

        self.radioButton2 = QRadioButton("ინგლისური")                     # create radiobutton2
        self.radioButton2.setIcon(QtGui.QIcon("img/english.png"))          # set icon on radiobutton2
        self.radioButton2.setIconSize(QtCore.QSize(40,40))                 # set icon size
        hboxLayout.addWidget(self.radioButton2)                            # add radiobutton2 in horizontal layout
        self.radioButton2.toggled.connect(self.eng)

        self.ApplySet = QPushButton("დადასტურება",self)
        self.CancelSet = QPushButton("გაუქმება",self)
        self.ApplySet.clicked.connect(self.applySettings)
        self.CancelSet.clicked.connect(self.CancelSettings)

        self.groupBox.setLayout(hboxLayout)                                # in group box set horizontal layout

        VLbox.addWidget(self.groupBox)
        VLbox.addWidget(self.ApplySet)
        VLbox.addWidget(self.CancelSet)

        self.setLayout(VLbox)
# ++++++++++++++++++++++++++++++++++++++++++++ Georgian language option ++++++++++++++++++++++++++++++++++++++++++++
    def geo(self):
        if self.radioButton1.isChecked():
            global langvage
            langvage = "ქართული"
            App.term(self,langvage)
# +++++++++++++++++++++++++++++++++++++++++++++ English language option ++++++++++++++++++++++++++++++++++++++++++++
    def eng(self):
        if self.radioButton2.isChecked():
            global langvage
            langvage = "ინგლისური"
            App.term(self,langvage)
# +++++++++++++++++++++++++++++++++++++++++++++++++ Apply Settings +++++++++++++++++++++++++++++++++++++++++++++++++
    def applySettings(self):
        global config
        config = "კონფიგურაცია დასრულდა"
        App.term(self,config)
        self.close()
# +++++++++++++++++++++++++++++++++++++++++++++++++ Cancel Settings ++++++++++++++++++++++++++++++++++++++++++++++++
    def CancelSettings(self):
        self.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TableView ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TableView(QTableWidget):
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ ++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, temp_data, *args):
        QTableWidget.__init__(self, *args)
        self.setHeaders()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setSortingEnabled(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# +++++++++++++++++++++++++++++++++++++++++++++++++++ setHeaders +++++++++++++++++++++++++++++++++++++++++++++++++++
    def setHeaders(self):
        self.setHorizontalHeaderLabels(temp_header)
# ==================================================================================================================
# ==================================================================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main window App Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class App(QMainWindow):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ +++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self):
        QMainWindow.__init__(self,None)
# -------------------------------------------------- Initialization ------------------------------------------------
        self.title = 'Bookmarks'                                           # create main window title
        self.top = 100                                                 # create pixel distance variable from top
        self.left = 100                                                # create pixel distance variable from left side
        self.width = 1600                                              # create window width
        self.height = 800                                              # create window height
        self.initUI()                                                  # Run initialization User Interface
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ initUI ++++++++++++++++++++++++++++++++++++++++++++++++++++
    def initUI(self):
        QMainWindow.__init__(self)
#----------------------------------------------- set date on status ber --------------------------------------------
        now = datetime.datetime.now()
        self.statusBar().showMessage(now.strftime("%d-%m-%Y"))
# ------------------------------------------------- Main window icon -----------------------------------------------
        self.setWindowTitle(self.title)                                # call method which sets window title
        self.setWindowIcon(QtGui.QIcon("img/link.png"))             # Set main window icon
        self.setGeometry(self.left, self.top, self.width, self.height) # Set geometry of main window
# --------------------------------------------------- Create Menu --------------------------------------------------
        mainMenu = self.menuBar()                                      # Create menu
# ------------------------------------------------ create menu options ---------------------------------------------
        viewMenu = mainMenu.addMenu('ინტერფეისი')

        toggleTool = QAction("ინსტრუმენტთა ველი 1",self,checkable=True)
        toggleTool.triggered.connect(self.handleToggleTool)

        toggleStatus = QAction("Toggle Statusbar",self,checkable=True)
        toggleStatus.triggered.connect(self.handleToggleStatus)
 
        viewMenu.addAction(toggleTool)
# ----------------------------------------------------- ToolBar ----------------------------------------------------
# -------------------------------------------------- Exit toolbar --------------------------------------------------
        exitAct = QAction(QIcon('img/close.png'),'გასვლა', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(app.quit)
#-------------------------------------------------------- Save -----------------------------------------------------
# --------------------------------------------------- Save toolbar -------------------------------------------------
        saveAct = QAction(QIcon('img/save.png'),'შენახვა', self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.triggered.connect(lambda: self.term('შენახვა'))
        saveAct.triggered.connect(self.save)
# ------------------------------------------------------- copy -----------------------------------------------------
        copyAct = QAction(QIcon('img/copy.png'),'ასლი', self)
        copyAct.setShortcut("Ctrl+C")
        copyAct.triggered.connect(lambda: self.term('ასლი'))
        copyAct.triggered.connect(self.copy)
# ------------------------------------------------------ paste -----------------------------------------------------
        pasteAct = QAction(QIcon('img/paste.png'),'ჩაკვრა', self)
        pasteAct.setShortcut("Ctrl+V")
        pasteAct.triggered.connect(lambda: self.term('ჩაკვრა'))
        pasteAct.triggered.connect(self.paste)
# ------------------------------------------------------- play -----------------------------------------------------
        playAct = QAction(QIcon('img/play.png'),'გაშვება', self)
        playAct.setShortcut("Ctrl+P")
        playAct.triggered.connect(lambda: self.term('გაშვება'))
        playAct.triggered.connect(self.play)
#--------------------------------------------- Row - Column manipulation -------------------------------------------
# ------------------------------------------------ insert Row toolbar ----------------------------------------------
        insRowAct = QAction(QIcon('img/addRow.png'), 'სტრიქონის დამატება', self)
        insRowAct.triggered.connect(self.insRow)
        insRowAct.triggered.connect(lambda: self.term("სტრიქონის დამატება"))
# ------------------------------------------------ Delete Row toolbar ----------------------------------------------
        DelRowAct = QAction(QIcon('img/DelRow.png'), 'სტრიქონის წაშლა', self)
        DelRowAct.triggered.connect(self.delRow)
        DelRowAct.triggered.connect(lambda: self.term("სტრიქონის წაშლა"))
# ------------------------------------------------------ Menge -----------------------------------------------------
        mergeAct = QAction(QIcon('img/merge.png'), 'შერწყმა', self)
        mergeAct.triggered.connect(lambda: self.term('შერწყმა'))
        mergeAct.triggered.connect(self.merge)
#-------------------------------------------------------- Font -----------------------------------------------------
# --------------------------------------------------- Font toolbar -------------------------------------------------
        FontAct = QAction(QIcon('img/Font.png'), 'ფონტები', self)
        FontAct.triggered.connect(lambda: self.term('ფონტები'))
        FontAct.triggered.connect(self.font)
# --------------------------------------------------- color palete -------------------------------------------------
        colorAct = QAction(QIcon('img/color.png'), 'ტექსტის ფერები', self)
        colorAct.triggered.connect(lambda: self.term('ფერები'))
        colorAct.triggered.connect(self.color)
# ------------------------------------------------- background color -----------------------------------------------
        backColorAct = QAction(QIcon("img/background-color.png"),"ფონის ფერი",self)
        backColorAct.triggered.connect(self.FontBackColor)
# ---------------------------------------------------- alignLeft  --------------------------------------------------
        alignLeftAct = QAction(QIcon('img/alignLeft.png'), 'ტექსტი მარცხნივ', self)
        alignLeftAct.triggered.connect(self.alignLeft)
        alignLeftAct.triggered.connect(lambda: self.term("ტექსტი მარცხნივ"))
# ---------------------------------------------------- alignRight  -------------------------------------------------
        alignRightAct = QAction(QIcon('img/alignRight.png'), 'ტექსტი მარჯვნივ', self)
        alignRightAct.triggered.connect(self.alignRight)
        alignRightAct.triggered.connect(lambda: self.term("ტექსტი მარჯვნივ"))
# --------------------------------------------------- alignCenter  -------------------------------------------------
        alignCenterAct = QAction(QIcon('img/alignCenter.png'), 'ტექსტი ცენტრში', self)
        alignCenterAct.triggered.connect(self.alignCenter)
        alignCenterAct.triggered.connect(lambda: self.term("ტექსტი ცენტრში"))
# ---------------------------------------------------- settings  ---------------------------------------------------
        settingsAct = QAction(QIcon('img/settings.png'), 'პარამეტრები', self)
        settingsAct.triggered.connect(lambda: self.term("პარამეტრები"))
        settingsAct.triggered.connect(Settings(self).show)
# ------------------------------------------- add buttons on first toolbar -----------------------------------------
        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(saveAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(playAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(insRowAct)
        self.toolbar.addAction(DelRowAct)
        self.toolbar.addAction(mergeAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(FontAct)
        self.toolbar.addAction(colorAct)
        self.toolbar.addAction(backColorAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(alignLeftAct)
        self.toolbar.addAction(alignRightAct)
        self.toolbar.addAction(alignCenterAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(settingsAct)
        self.addToolBarBreak()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.TopToolBarArea , self.toolbar)
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ Create tabs widget ----------------------------------------------
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
# -------------------------------------------------- add tab pages -------------------------------------------------
# ---------------------------------------------------- Add tabs ----------------------------------------------------
        self.tabs.addTab(self.tab1, "მიმდინარე")
        self.setCentralWidget(self.tabs)
# ------------------------------------------------ set tab1 layouts ------------------------------------------------
        self.tab1.VlayoutTab1 = QVBoxLayout()
        self.HlayoutTab1 = QHBoxLayout()
# ----------------------------------- create table widget and add on vertical layut --------------------------------
        global table
        table = TableView(temp_data, 500, len(temp_header))                             # fixed size table
        self.tab1.VlayoutTab1.addWidget(table)                            # add table in vertival layout of tab1
# -------------------------------------------- selectred cell activation -------------------------------------------
        table.clicked.connect(self.Row)
        table.clicked.connect(self.Column)    
# ----------------------------------------------- Table cell changed -----------------------------------------------
        table.cellChanged.connect(self.tabEvent)
#------------------------------------------------------ Buttons ----------------------------------------------------
# ------------------------------------------------- create A button ------------------------------------------------
        self.pushButton1 = QPushButton("ბეჭვდა")
        self.HlayoutTab1.addWidget(self.pushButton1)
        self.pushButton1.clicked.connect(self.A)
# ------------------------------------------------- create B button ------------------------------------------------
        self.pushButton2 = QPushButton("შაბლონის შენახვა")
        self.HlayoutTab1.addWidget(self.pushButton2)
        self.pushButton2.clicked.connect(self.B)
#------------------------------------------------------ Terminal ---------------------------------------------------
        global terminal
        terminal = QPlainTextEdit(self)
        terminal.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.tab1.VlayoutTab1.addWidget(terminal)
# ------------------------------------------------- set tab 1 layout  ----------------------------------------------
        self.tab1.VlayoutTab1.addLayout(self.HlayoutTab1)
        self.tab1.setLayout(self.tab1.VlayoutTab1)
# ----------------------------------------------------- call open --------------------------------------------------
        self.open()
# ------------------------------------------------- Clear terminal -------------------------------------------------
        terminal.clear()
# ------------------------------------------------- Show main window -----------------------------------------------
        self.show()
# +++++++++++++++++++++++++++++++++++++++++++++++++++ status bar +++++++++++++++++++++++++++++++++++++++++++++++++++
    def process(self, text):
        self.statusBar().showMessage(text)
# ++++++++++++++++++++++++++++++++++++++++++++++++++ Determine Row +++++++++++++++++++++++++++++++++++++++++++++++++
    def Row(self):
        global table
        self.row = table.currentRow()
# +++++++++++++++++++++++++++++++++++++++++++++++++ Determine Column +++++++++++++++++++++++++++++++++++++++++++++++
    def Column(self):
        global table
        self.col = table.currentColumn()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++ A +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def A(self):
        self.term(str(temp_header))
        self.term(str(temp_Merge))
        self.term(str(temp_table))
        self.term(str(len(temp_table)))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++ B +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def B(self):
        self.term("შენახვა")
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ open +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def open(self):
        global table
        global temp_header
        global temp_Merge
        global temp_table
        global temp_config
        global OpenPath

        global temp_data
        try:
            with open('data.pkl', 'rb') as f:
                temp_data = pickle.load(f)

            temp_header = temp_data['header']
            temp_Merge = temp_data['Merge']
            temp_table = temp_data['table']
            temp_config = temp_data['config']

            for item in temp_table:
                try:
                    newitem = QTableWidgetItem(item[2])
                    table.setItem(item[0], item[1], newitem)
                except IndexError:
                    pass
                
                try:
                    if item[6] != '':
                        if item[6] == 'C':
                            table.item(item[0], item[1]).setTextAlignment(Qt.AlignCenter)
                        if item[6] == 'R':
                            table.item(item[0], item[1]).setTextAlignment(Qt.AlignRight)
                        if item[6] == 'L':
                            table.item(item[0], item[1]).setTextAlignment(Qt.AlignLeft)
                except IndexError:
                    pass
                
                list_font = QtGui.QFont()
                try:
                    if item[3] != "":
                        list_font.fromString(item[3])
                        table.item(item[0], item[1]).setFont(list_font)
                except IndexError:
                    pass
                
                try:
                    CellBgColor = QtGui.QColor(item[4][0],item[4][1],item[4][2],item[4][3])
                    table.item(item[0], item[1]).setBackground(CellBgColor)
                except IndexError:
                    pass

                try:
                    TxtColor = QtGui.QColor(item[5][0],item[5][1],item[5][2],item[5][3])
                    table.item(item[0], item[1]).setForeground(TxtColor)
                except IndexError:
                    pass

            for index in temp_Merge:
                table.setSpan(index[0], index[1], index[2], index[3])
                    
            table.setHeaders()
        except FileNotFoundError:
            self.save()
            self.open()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Save +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def save(self):
        with open('data.pkl', 'wb') as f:
            temp_data['header'] = temp_header
            temp_data['Merge'] = temp_Merge
            temp_data['table'] = temp_table

            pickle.dump(temp_data, f)

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ copy +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def copy(self):
        global table
        self.clip = QApplication.clipboard()
        self.selected = table.selectedRanges()

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
                    s += str(table.item(r,c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"
        self.clip.setText(s)
        self.term(str(self.clip.text()))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ paste +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def paste(self):
        global table
        global temp_table
        try:
            first_row = self.row
            first_col = self.col
            #copied text is split by '\n' and '\t' to paste to the cells
            for r, row in enumerate(self.clip.text().split('\n')):
                for c, text in enumerate(row.split('\t')):
                    table.setItem(first_row + r, first_col + c, QTableWidgetItem(text))
                    for table_item in temp_table:
                        if table_item[0] == first_row + r and table_item[1] == first_col + c:
                            table_item[2] = str(table.item(first_row + r, first_col + c).text())
                        else:
                            temp_table.append([first_row + r, first_col + c, str(table.item(first_row + r, first_col + c).text()),'',[],[],''])
                            break
        except AttributeError:
            pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ play +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def play(self):
        import os
        global table
        try:
            l = table.item(self.row, 4)
            os.startfile(l.text())
        except:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ Insert Row ++++++++++++++++++++++++++++++++++++++++++++++++++
    def insRow(self, indexRow = 0):
        global table
        global temp_Merge
        self.row = table.currentRow()
        table.insertRow(self.row)
        try:
            for j in range(len(temp_table)):                
                if temp_table[j][0] >= self.row:
                    temp_table[j][0] = temp_table[j][0] + 1
        except IndexError:
            pass
        
        for i in range(len(temp_Merge)):
            if self.row <= temp_Merge[i][0]:
                temp_Merge[i][0] = temp_Merge[i][0] + 1            
# +++++++++++++++++++++++++++++++++++++++++++++++++++ TABLE EVENT ++++++++++++++++++++++++++++++++++++++++++++++++++
    def tabEvent(self):
        global temp_table
        r = table.currentRow()
        c = table.currentColumn()
        try:
            item = table.item(r, c)
            self.value = item.text()
            if self.value is not '':
                add = False
                for table_item in temp_table:
                    if table_item[0] == r and table_item[1] == c:
                        table_item[2] = str(self.value)
                        add = False
                        break
                    else:
                        add = True
                if add == True:
                    temp_table.append([r,c,self.value,'',[],[],'C'])
                    table.item(r, c).setTextAlignment(Qt.AlignCenter)
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++ Delete table Row ++++++++++++++++++++++++++++++++++++++++++++++++
    def delRow(self):
        global table
        global temp_Merge
        global temp_table
        self.row = table.currentRow()
        table.removeRow(self.row)
        try:
            for item in temp_table:
                if item[0] == self.row:
                    temp_table = list(filter(partial(ne, item), temp_table))
        except IndexError:
            pass

        try:
            for j in range(len(temp_table)):                
                if temp_table[j][0] >= self.row:
                    temp_table[j][0] = temp_table[j][0] - 1
        except IndexError:
            pass
        
        for i in range(len(temp_Merge)):
            if self.row < temp_Merge[i][0]:
                temp_Merge[i][0] = temp_Merge[i][0] - 1

        for M_item in temp_Merge:
            if M_item[0] == self.row:
                temp_Merge = list(filter(partial(ne, M_item), temp_Merge))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ merge +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def merge(self):
        global table
        global temp_Merge
        r = []
        c = []
        for item in table.selectedIndexes():
            r.append(item.row())
            c.append(item.column())
        if len(r) > 0 or len(c) > 0:
            table.setSpan(r[0], c[0], max(r)-min(r)+1, max(c)-min(c)+1)
            t_Merge = [r[0], c[0], max(r)-min(r)+1, max(c)-min(c)+1]
        
        if t_Merge[2] != t_Merge[3]:
            temp_Merge.append(t_Merge)
            self.term(str(temp_Merge))
        else:
            for M_item in temp_Merge:
                if t_Merge[0] == M_item[0] and t_Merge[1] == M_item[1]:
                    temp_Merge = list(filter(partial(ne, M_item), temp_Merge))        
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Font +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def font(self):
        global table
        try:
            font, ok = QFontDialog.getFont()
            if ok:
                for item in table.selectedIndexes():
                    table.item(item.row(), item.column()).setFont(font)
                    for table_item in temp_table:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[3] = font.toString()
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ color +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def color(self):
        global table
        color = QColorDialog.getColor()
        if color.isValid():
            for item in table.selectedIndexes():
                try:
                    table.item(item.row(),item.column()).setForeground(QBrush(color))
                    for table_item in temp_table:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[5] = list(color.getRgb())
                except AttributeError:
                    pass
# ++++++++++++++++++++++++++++++++++++++++++++++ Text bachground color +++++++++++++++++++++++++++++++++++++++++++++
    def FontBackColor(self):
        empty_cell = []
        global table
        global temp_table
        BGColor = QColorDialog.getColor()
        for item in table.selectedIndexes():
            empty_cell = []
            try:
                table.item(item.row(),item.column()).setBackground(BGColor)
                for table_item in temp_table:
                        if table_item[0] == item.row() and table_item[1] == item.column():
                            table_item[4] = list(BGColor.getRgb())
            except AttributeError:
                newitem = QTableWidgetItem(None)
                table.setItem(item.row(), item.column(), newitem)
                newitem.setBackground(BGColor)
                empty_cell.append(item.row())
                empty_cell.append(item.column())
                empty_cell.append(None)
                empty_cell.append('')
                empty_cell.append(list(BGColor.getRgb()))
                empty_cell.append([])
                empty_cell.append('C')
                temp_table.append(empty_cell)
        self.term(str(BGColor.getRgb()))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ settings +++++++++++++++++++++++++++++++++++++++++++++++++++
    #def settings(self):
    #    print("settings")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ Clear +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def keyPressEvent(self, event):
        global table
        global temp_table
        if event.key() == Qt.Key_Delete:
            for item in table.selectedIndexes():
                table.setItem(item.row(), item.column(), None)
                for table_item in temp_table:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        temp_table = list(filter(partial(ne, table_item), temp_table))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ showDate +++++++++++++++++++++++++++++++++++++++++++++++++++
    def showDate(self, date):
        self.CalLabel.setText(date.toString())
# ++++++++++++++++++++++++++++++++++++++++++++++++++ Terminal Print ++++++++++++++++++++++++++++++++++++++++++++++++
    def term(self, Text):
        terminal.insertPlainText("-----------------------------\n")
        terminal.insertPlainText("----> " + Text + "\n")
        terminal.insertPlainText("-----------------------------\n")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignLeft +++++++++++++++++++++++++++++++++++++++++++++++++++
    def alignLeft(self):
        global table
        try:
            for item in table.selectedIndexes():
                table.item(item.row(), item.column()).setTextAlignment(Qt.AlignLeft)
                for table_item in temp_table:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        table_item[6] = 'L'
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignRight ++++++++++++++++++++++++++++++++++++++++++++++++++
    def alignRight(self):
        global table
        try:
            for item in table.selectedIndexes():
                table.item(item.row(), item.column()).setTextAlignment(Qt.AlignRight)
                for table_item in temp_table:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        table_item[6] = 'R'
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ alignCenter +++++++++++++++++++++++++++++++++++++++++++++++++
    def alignCenter(self):
        global table
        try:
            for item in table.selectedIndexes():
                table.item(item.row(), item.column()).setTextAlignment(Qt.AlignCenter)
                for table_item in temp_table:
                    if table_item[0] == item.row() and table_item[1] == item.column():
                        table_item[6] = 'C'
        except AttributeError:
            pass
# ++++++++++++++++++++++++++++++++++++++++++++++++ Toolbar Hide-Show +++++++++++++++++++++++++++++++++++++++++++++++
    def handleToggleTool(self):
        global tt
        if tt == True:
            self.toolbar.hide()
            tt = False
        else:
            self.toolbar.show()
            tt = True
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def handleToggleStatus(self):
        global ts

        if ts == True:
            self.status.hide()
            ts = False
        else:
            self.status.show()
            ts = True
# ------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================
# ==================================================================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#----------------------------------------------------- Reserve -----------------------------------------------------