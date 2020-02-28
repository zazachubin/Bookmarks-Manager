##!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------- Libraries ---------------------------------------------------
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QPlainTextEdit, QLineEdit, QSplitter, QLabel, QHeaderView, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from Table import TableView
import datetime
import json
import sys

data = {'config': {'tableColNumber' : 6,'language' : 'georgian','length': 1850, 'width' : 900},
        'data_tab1' : {'header': ['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
                       'Merge' : [[0, 0, 1, 6],[2, 0, 1, 6],[4, 0, 1, 6]],
                       'table' : [[0,0,'LabVIEW','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
                                  [1,0,'Labview tutorial Enable integration','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [1,1,'42','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [1,2,'42','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [1,4,r'https://www.youtube.com/playlist?list=PLdNp0fxltzmPvvK_yjX-XyYgfVW8WK4tu','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [1,5,'გაკვეთილი','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [2,0,'Qt C++','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
                                  [3,0,'Udemy - C Plus Plus programming in Qt FrameWork Part I','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [3,1,'8','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [3,2,'11','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [3,4,r'D:\Courses\Programing\C\Qt_C++\Udemy - C Plus Plus programming in Qt FrameWork Part I','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [3,5,'001 QMainWindow Structure','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [4,0,'ფიზიკა','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
                                  [5,0,'ზოგადი ფიზიკის კურსი I ტომი','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [5,1,'395','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [5,2,'490','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [5,4,r'D:\Library\ფიზიკა\ზოგადი ფიზიკის კურსი  I ტომი.pdf','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [6,0,'EPD ამაჩქარლების ფიზიკა','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [6,1,'38','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [6,2,'366','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                  [6,4,r'D:\Library\ამაჩქარებლები\EPD ამაჩქარლების ფიზიკა.pdf','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C']]},
        'data_tab2' : { 'header': ['შინაარსი','ლინკი','კომენტარი'],
                        'Merge' : [[0, 0, 1, 6]],
                        'table' : [[0,0,'LabVIEW','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
                                   [1,0,r'https://www.youtube.com/playlist?list=PLdNp0fxltzmPvvK_yjX-XyYgfVW8WK4tu','Times New Roman,8,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
                                   [1,1,'Labview tutorial Enable integration','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C']]}}
tt = True
ts = True
temp_data = { 'config': {'tableColNumber' : 6,'language' : 'georgian','length': 1850, 'width' : 900},
              'data_tab1' : {'header': ['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
                             'Merge' : [],
                             'table' : []},
              'data_tab2' : {'header': ['შინაარსი','ლინკი','კომენტარი'],
                             'Merge' : [],
                             'table' : []}}
class App(QMainWindow):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ +++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self,title,top,left,iconPath):
        QMainWindow.__init__(self,None)
# -------------------------------------------------- Initialization ------------------------------------------------
        self.title = title                                       # create main window title
        self.top = top                                                 # window ofset distance from top
        self.left = left                                               # window ofset distance from left side
        self.iconPath = iconPath                                       # main window icon
        self.importData('data.json')                                   # import data from file
        self.initUI()                                                  # Run initialization User Interface
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ initUI ++++++++++++++++++++++++++++++++++++++++++++++++++++
    def initUI(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(self.title)                                # sets window title
        self.setWindowIcon(QtGui.QIcon(self.iconPath))                 # Set main window icon
        self.setGeometry(self.left, self.top, int(temp_data['config']['length']), int(temp_data['config']['width'])) # set window size
#----------------------------------------------- set date on status ber --------------------------------------------
        now = datetime.datetime.now()                                  # read date
        self.statusBar().showMessage(now.strftime("%d-%m-%Y"))         # set date to statusBar
# --------------------------------------------------- Create Menu --------------------------------------------------
        mainMenu = self.menuBar()                                      # Create menu
# ------------------------------------------------ create menu options ---------------------------------------------
        viewMenu = mainMenu.addMenu('ინტერფეისი')                         # create menu section
        toggleTool = QAction("ინსტრუმენტთა ველი 1",self,checkable=True)  # create menu option
        toggleTool.triggered.connect(self.handleToggleTool)                # choose menu oprion
        toggleStatus = QAction("Toggle Statusbar",self,checkable=True)     # create menu option
        toggleStatus.triggered.connect(self.handleToggleStatus)            # choose menu oprion
        viewMenu.addAction(toggleTool)                                     # set menu oprion
# ----------------------------------------------------- ToolBar ----------------------------------------------------
# -------------------------------------------------- Exit toolbar --------------------------------------------------
        exitAct = QAction(QIcon('img/close.png'),'გასვლა', self)           # create exit button in toolBar
        exitAct.setShortcut('Ctrl+Q')                                      # key manipulation of exit button
        exitAct.triggered.connect(app.quit)                                # run quit function
#-------------------------------------------------------- Save -----------------------------------------------------
# --------------------------------------------------- Save toolbar -------------------------------------------------
        saveAct = QAction(QIcon('img/save.png'),'შენახვა', self)            # create Save button in toolBar
        saveAct.setShortcut("Ctrl+S")                                      # key manipulation of save button
        saveAct.triggered.connect(lambda : self.save('data.json'))         # run function
# ------------------------------------------------------- copy -----------------------------------------------------
        copyAct = QAction(QIcon('img/copy.png'),'ასლი', self)              # create Copy button in toolBar
        copyAct.setShortcut("Ctrl+C")                                      # key manipulation of Copy button
        copyAct.triggered.connect(lambda : self.table1.copy() if self.tabs.currentIndex() == 0 else self.table2.copy())     # run function
# ------------------------------------------------------ paste -----------------------------------------------------
        pasteAct = QAction(QIcon('img/paste.png'),'ჩაკვრა', self)           # create paste button in toolBar
        pasteAct.setShortcut("Ctrl+V")                                     # key manipulation of paste button
        pasteAct.triggered.connect(lambda : self.table1.paste() if self.tabs.currentIndex() == 0 else self.table2.paste())
# ------------------------------------------------------- play -----------------------------------------------------
        playAct = QAction(QIcon('img/play.png'),'გაშვება', self)            # create play button in toolBar
        playAct.setShortcut("Ctrl+P")                                      # key manipulation of play button
        playAct.triggered.connect(self.play)                               # run function
#--------------------------------------------- Row - Column manipulation -------------------------------------------
# ------------------------------------------------ insert Row toolbar ----------------------------------------------
        insRowAct = QAction(QIcon('img/addRow.png'), 'სტრიქონის დამატება', self) # create addRow button in toolBar
        insRowAct.triggered.connect(lambda : self.table1.insRow() if self.tabs.currentIndex() == 0 else self.table2.insRow())                # run function
# ------------------------------------------------ Delete Row toolbar ----------------------------------------------
        DelRowAct = QAction(QIcon('img/DelRow.png'), 'სტრიქონის წაშლა', self)    # create delRow button in toolBar
        DelRowAct.triggered.connect(lambda : self.table1.delRow() if self.tabs.currentIndex() == 0 else self.table2.delRow())                 # run function
# ------------------------------------------------------ Menge -----------------------------------------------------
        mergeAct = QAction(QIcon('img/merge.png'), 'შერწყმა', self)               # create Merge button in toolBar
        mergeAct.triggered.connect(lambda : self.table1.merge() if self.tabs.currentIndex() == 0 else self.table2.merge())                   # run function
#-------------------------------------------------------- Font -----------------------------------------------------
# --------------------------------------------------- Font toolbar -------------------------------------------------
        FontAct = QAction(QIcon('img/Font.png'), 'ფონტები', self)                # create Font button in toolBar
        FontAct.triggered.connect(lambda : self.table1.font() if self.tabs.currentIndex() == 0 else self.table2.font())                     # run function
# --------------------------------------------------- color palete -------------------------------------------------
        colorAct = QAction(QIcon('img/color.png'), 'ტექსტის ფერები', self)       # create Font button in toolBar
        colorAct.triggered.connect(lambda : self.table1.color() if self.tabs.currentIndex() == 0 else self.table2.color())                  # run function
# ------------------------------------------------- background color -----------------------------------------------
        backColorAct = QAction(QIcon("img/background-color.png"),"ფონის ფერი",self)  # create Font button in toolBar
        backColorAct.triggered.connect(lambda : self.table1.FontBackColor() if self.tabs.currentIndex() == 0 else self.table2.FontBackColor())           # run function
# ---------------------------------------------------- alignLeft  --------------------------------------------------
        alignLeftAct = QAction(QIcon('img/alignLeft.png'), 'ტექსტი მარცხნივ', self)  # create Font button in toolBar
        alignLeftAct.triggered.connect(lambda : self.table1.alignLeft() if self.tabs.currentIndex() == 0 else self.table2.alignLeft())              # run function
# ---------------------------------------------------- alignRight  -------------------------------------------------
        alignRightAct = QAction(QIcon('img/alignRight.png'), 'ტექსტი მარჯვნივ', self) # create Font button in toolBar
        alignRightAct.triggered.connect(lambda : self.table1.alignRight() if self.tabs.currentIndex() == 0 else self.table2.alignRight())             # run function
# --------------------------------------------------- alignCenter  -------------------------------------------------
        alignCenterAct = QAction(QIcon('img/alignCenter.png'), 'ტექსტი ცენტრში', self)
        alignCenterAct.triggered.connect(lambda : self.table1.alignCenter() if self.tabs.currentIndex() == 0 else self.table2.alignCenter())
# ---------------------------------------------------- settings  ---------------------------------------------------
        settingsAct = QAction(QIcon('img/settings.png'), 'პარამეტრები', self)         # create Font button in toolBar
        settingsAct.triggered.connect(self.settings)                                  # run function
# ---------------------------------------------- Print data structure ----------------------------------------------
        printAct = QAction(QIcon('img/print.png'), 'მონაცემთა დაბეჭვდა', self)        # create Font button in toolBar
        printAct.triggered.connect(self.printData)                                    # run function
# ----------------------------------------------- save data template -----------------------------------------------
        saveTemplateAct = QAction(QIcon('img/template.png'), 'მონაცემთა შაბლონი', self)  # create Font button in toolBar
        saveTemplateAct.triggered.connect(self.dataTemplate)                              # run function
        saveTemplateAct.triggered.connect(lambda : self.table1.openData(temp_data['data_tab1']))        # run function
        saveTemplateAct.triggered.connect(lambda : self.table2.openData(temp_data['data_tab2']))        # run function
# ------------------------------------------------------ Test ------------------------------------------------------
        testAct = QAction(QIcon('img/test.png'), 'ტესტი', self)                       # create Test button in toolBar
        #testAct.triggered.connect(lambda : self.table1.calculations(temp_data))        # run function
        testAct.triggered.connect(self.test)                                           # run function
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
        self.toolbar.addSeparator()
        self.toolbar.addAction(printAct)
        self.toolbar.addAction(saveTemplateAct)
        self.toolbar.addAction(testAct)
        self.addToolBarBreak()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.TopToolBarArea , self.toolbar)
# ------------------------------------------------ Create tabs widget ----------------------------------------------
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
# -------------------------------------------------- add tab pages -------------------------------------------------
# ---------------------------------------------------- Add tabs ----------------------------------------------------
        self.tabs.addTab(self.tab1, "მიმდინარე")
        self.tabs.addTab(self.tab2, "ტერმინალი")
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(self.tab3, "გრაფიკები")
# ------------------------------------------------ set tab1 layouts ------------------------------------------------
        self.VlayoutTab1 = QVBoxLayout()
        self.HlayoutTab1 = QHBoxLayout()
# ------------------------------------------------ set tab2 layouts ------------------------------------------------
        self.VlayoutTab2 = QVBoxLayout()
# ------------------------------------------------ set tab3 layouts ------------------------------------------------
        self.tab3.VlayoutTab3 = QVBoxLayout()
        self.HlayoutTab3 = QHBoxLayout()
# --------------------------------------------------- Search_tab1 --------------------------------------------------
        self.HlayoutSearch_tab1 = QHBoxLayout()
        self.search_line_tab1 = QLineEdit()
        self.search_but_tab1 = QPushButton("ძებნა")
        self.search_next_tab1 = QPushButton("შემდეგი")
        self.searchInfoLabel_tab1 = QLabel("    ")
        self.searchInfoLabel_tab1.setText("0")
        self.search_but_tab1.clicked.connect(lambda : self.searchInfoLabel_tab1.setText(str(self.table1.find_items(self.search_line_tab1.text()))))
        self.search_next_tab1.clicked.connect(lambda : self.table1.find_items(self.search_line_tab1.text()))

        self.HlayoutSearch_tab1.addWidget(self.search_line_tab1)
        self.HlayoutSearch_tab1.addWidget(self.search_but_tab1)
        self.HlayoutSearch_tab1.addWidget(self.search_next_tab1)
        self.HlayoutSearch_tab1.addWidget(self.searchInfoLabel_tab1)

        self.VlayoutTab1.addLayout(self.HlayoutSearch_tab1)
# --------------------------------------------------- Search_tab2 --------------------------------------------------
        self.HlayoutSearch_tab2 = QHBoxLayout()
        self.search_line_tab2 = QLineEdit()
        self.search_but_tab2 = QPushButton("ძებნა")
        self.search_next_tab2 = QPushButton("შემდეგი")
        self.searchInfoLabel_tab2 = QLabel("    ")
        self.searchInfoLabel_tab2.setText("0")
        self.search_but_tab2.clicked.connect(lambda : self.searchInfoLabel_tab2.setText(str(self.table2.find_items(self.search_line_tab2.text()))))
        self.search_next_tab2.clicked.connect(lambda : self.table2.find_items(self.search_line_tab2.text()))

        self.HlayoutSearch_tab2.addWidget(self.search_line_tab2)
        self.HlayoutSearch_tab2.addWidget(self.search_but_tab2)
        self.HlayoutSearch_tab2.addWidget(self.search_next_tab2)
        self.HlayoutSearch_tab2.addWidget(self.searchInfoLabel_tab2)

        self.VlayoutTab2.addLayout(self.HlayoutSearch_tab2)
# ----------------------------------- create table1 widget and add on vertical layut -------------------------------
        col_width_array_tab1 = {0 : 500, 1 : 120, 2 : 120, 4 : 500, 5 : 360}
        self.table1 = TableView(temp_data['data_tab1'], col_width_array_tab1, 500, len(temp_data['data_tab1']['header']))
        self.table1.openData(temp_data['data_tab1'])
        self.VlayoutTab1.addWidget(self.table1)                            # add table in vertival layout of tab1
# ----------------------------------- create table2 widget and add on vertical layut -------------------------------
        col_width_array_tab2 = {0 : 580, 1 : 580, 2 : 580}
        self.table2 = TableView(temp_data['data_tab2'], col_width_array_tab2, 500, len(temp_data['data_tab2']['header']))
        self.table2.openData(temp_data['data_tab2'])
        self.VlayoutTab2.addWidget(self.table2)                            # add table in vertival layout of tab1
# ---------------------------------------------------- plot data ---------------------------------------------------
        from Plots import PlotCanvas
        self.plot1 = PlotCanvas(self, width=5, height=4)
        self.plot2 = PlotCanvas(self, width=5, height=4)
        self.plot3 = PlotCanvas(self, width=5, height=4)
        self.plot4 = PlotCanvas(self, width=5, height=4)
#------------------------------------------------------ Spliter ----------------------------------------------------
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.plot1)
        self.splitter1.addWidget(self.plot2)

        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.plot3)
        self.splitter2.addWidget(self.plot4)

        self.HlayoutTab3.addWidget(self.splitter2)
        self.tab3.VlayoutTab3.addLayout(self.HlayoutTab3)
# ------------------------------------------------- set tab 1 layout  ----------------------------------------------
        self.VlayoutTab1.addLayout(self.HlayoutTab1)
        self.tab1.setLayout(self.VlayoutTab1)
# ------------------------------------------------- set tab 2 layout  ----------------------------------------------
        self.tab2.setLayout(self.VlayoutTab2)
# ------------------------------------------------- set tab 3 layout  ----------------------------------------------
        self.tab3.setLayout(self.tab3.VlayoutTab3)
#------------------------------------------------------ Terminal ---------------------------------------------------
        self.terminal = QPlainTextEdit(self)
        self.VlayoutTab2.addWidget(self.terminal)
# ++++++++++++++++++++++++++++++++++++++++++++++ set main window size ++++++++++++++++++++++++++++++++++++++++++++++
    def setWindowSize(self,left,top,Edit_width,height):
        self.setGeometry(left, top, Edit_width, height)
# +++++++++++++++++++++++++++++++++++++++++++++++ StatusBar Message ++++++++++++++++++++++++++++++++++++++++++++++++
    def statusBarMessage(self,message):
        self.statusBar().showMessage(message)
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
# ++++++++++++++++++++++++++++++++++++++++++++++++++ Terminal Print ++++++++++++++++++++++++++++++++++++++++++++++++
    def term(self, Text):
        self.terminal.insertPlainText("-----------------------------\n")
        self.terminal.insertPlainText("----> " + Text + "\n")
        self.terminal.insertPlainText("-----------------------------\n")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ play +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def play(self):
        import os
        try:
            if self.tabs.currentIndex() == 0:
                l = self.table1.item(self.table1.currentRow(), 4)
            if self.tabs.currentIndex() == 1:
                l = self.table2.item(self.table2.currentRow(), 0)
            os.startfile(l.text())
            self.statusBarMessage('გაშვება')
        except:
            print(str(l.text()))
            print("exept")
            pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Save +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def save(self,Path):
        with open(Path, 'w') as outfile:
            json.dump(temp_data, outfile, indent=4)
        self.statusBarMessage('შენახვა')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++ importData ++++++++++++++++++++++++++++++++++++++++++++++++++
    def importData(self,OpenPath):
        self.OpenPath = OpenPath
        global temp_data
        try:
            with open(OpenPath, 'r') as f:
                temp_data = json.load(f)
            return temp_data
        except FileNotFoundError:
            pass
            self.save('data.json')
            self.importData('data.json')
# ++++++++++++++++++++++++++++++++++++++++++ Print data structure button +++++++++++++++++++++++++++++++++++++++++++
    def printData(self):
        self.term(" კონფიგურაცია ---> " + str(temp_data['config']))
        self.term(" ჰედერი 1 ---> " + str(temp_data['data_tab1']['header']))
        self.term(" შერწყმა 1 ---> " + str(temp_data['data_tab1']['Merge']))
        self.term(" ცხრილის 1 ---> " + str(temp_data['data_tab1']['table']))
        self.term(" ცხრილის 1 ზომა ---> " + str(len(temp_data['data_tab1']['table'])))
        self.term(" ჰედერი 2 ---> " + str(temp_data['data_tab1']['header']))
        self.term(" შერწყმა 2 ---> " + str(temp_data['data_tab1']['Merge']))
        self.term(" ცხრილის 2 ---> " + str(temp_data['data_tab2']['table']))
        self.term(" ცხრილის 2 ზომა ---> " + str(len(temp_data['data_tab2']['table'])))
        currentIndex=self.tabs.currentIndex()
        currentWidget=self.tabs.currentWidget()
        self.term(" ფანჯრის ინდექსი ---> " + str(currentIndex))
        self.term(" მიმდინარე ვიდჯეტი ---> " + str(currentWidget))
        self.statusBarMessage("მონაცემთა დაბეჭვდა")
# +++++++++++++++++++++++++++++++++++++++++++++++ save Data template +++++++++++++++++++++++++++++++++++++++++++++++
    def dataTemplate(self):
        global temp_data
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        self.statusBarMessage("მონაცემთა შაბლონის შენახვა")
        temp_data = self.importData('data.json')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ settings +++++++++++++++++++++++++++++++++++++++++++++++++++
    def settings(self):
        from SettingsDialog import Settings
        diag = Settings(temp_data['config'])
        diag.exec_()
        temp_data['config'] = diag.applySettings()
        self.term(str(temp_data['config']))
        self.statusBarMessage("პარამეტრები")
        self.setGeometry(self.left, self.top, int(temp_data['config']["length"]), int(temp_data['config']["width"]))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Test +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test(self):
        print("Test")
####################################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App('Bookmarks',50,30,"img/link.png")
    ex.show()
    sys.exit(app.exec_())
######################################################## Issues ####################################################
# * Setting close bug 
# * add row in first line has bug dont shift data in table