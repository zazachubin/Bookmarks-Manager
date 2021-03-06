##!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------- Libraries ---------------------------------------------------
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLineEdit, QTableWidgetItem, QListWidget, QProgressBar, QSplitter, QLabel, QHeaderView, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PushButton import PushBut
from LineEdit import LineEdit
from Table import TableView
from pprint import pformat, pprint
import datetime
import json
import sys

data = {'config': {'tableColNumber' : 6,'language' : 'georgian','length': 1850, 'width' : 900},
		'data_tab1' : {'header': ['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
					   'Merge' : [[0, 0, 1, 6],[2, 0, 1, 6],[4, 0, 1, 6]],
					   'table' : [[0,0,'LabVIEW','MS Shell Dlg 2,14,-1,5,75,0,0,0,0,0,Bold',[190, 192, 200, 255],[],'C'],
								  [1,0,'Labview tutorial Enable integration','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [1,1,'42','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [1,2,'42','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [1,4,r'https://www.youtube.com/playlist?list=PLdNp0fxltzmPvvK_yjX-XyYgfVW8WK4tu','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [1,5,'გაკვეთილი','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [2,0,'Qt C++','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
								  [3,0,'Udemy - C Plus Plus programming in Qt FrameWork Part I','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [3,1,'8','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [3,2,'11','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [3,4,r'D:\Courses\Programing\C\Qt_C++\Udemy - C Plus Plus programming in Qt FrameWork Part I','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [3,5,'001 QMainWindow Structure','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [4,0,'ფიზიკა','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
								  [5,0,'ზოგადი ფიზიკის კურსი I ტომი','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [5,1,'395','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [5,2,'490','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [5,4,r'D:\Library\ფიზიკა\ზოგადი ფიზიკის კურსი  I ტომი.pdf','Times New Roman,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [6,0,'EPD ამაჩქარლების ფიზიკა','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [6,1,'38','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [6,2,'366','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								  [6,4,r'D:\Library\ამაჩქარებლები\EPD ამაჩქარლების ფიზიკა.pdf','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C']]},
		'data_tab2' : { 'header': ['შინაარსი','ლინკი','კომენტარი'],
						'Merge' : [[0, 0, 1, 6]],
						'table' : [[0,0,'LabVIEW','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[190, 192, 200, 255],[],'C'],
								   [1,0,r'https://www.youtube.com/playlist?list=PLdNp0fxltzmPvvK_yjX-XyYgfVW8WK4tu','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C'],
								   [1,1,'Labview tutorial Enable integration','MS Shell Dlg 2,11,-1,5,50,0,0,0,0,0,Regular',[],[],'C']]}}
tt = True
ts = True
temp_data = { 'config': {'tableColNumber' : 6,'language' : 'georgian','length': 1850, 'width' : 900},
			  'data_tab1' : {'header': ['დასახელება','მიმდინარე','რაოდენობა','შესრულებული %','ლინკი','კომენტარი'],
							 'Merge' : [],
							 'table' : []},
			  'data_tab2' : {'header': ['შინაარსი','ლინკი','კომენტარი'],
							 'Merge' : [],
							 'table' : []}}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main App ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class App(QMainWindow):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ __init__ +++++++++++++++++++++++++++++++++++++++++++++++++++
	def __init__(self,title,top,left,iconPath):
		QMainWindow.__init__(self,None)
# -------------------------------------------------- Initialization ------------------------------------------------
		self.title = title                                             # create main window title
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
		self.setStyleSheet("""	QWidget {	background-color: rgba(0,41,59,255);}""")
		#self.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0 x2: 0, y2: 1, stop: 0 #00CD00 , stop: 0.2 #0AC92B stop: 1 #00FF33 );")
		self.setGeometry(self.left, self.top, int(temp_data['config']['length']), int(temp_data['config']['width'])) # set window size
#----------------------------------------------- set date on status ber --------------------------------------------
		now = datetime.datetime.now()                                  # read date
		self.statusBar().showMessage(now.strftime("%d-%m-%Y"))         # set date to statusBar
		self.statusBar().setStyleSheet("""QStatusBar{	padding-left:8px;
														color:white;
														font-weight:bold;}""")
# --------------------------------------------------- Create Menu --------------------------------------------------
		mainMenu = self.menuBar()                                         # Create menu
		mainMenu.setStyleSheet("""QWidget {	background-color: rgba(0,41,59,255);
											color:white;
											font-weight:bold;}""")
# ------------------------------------------------ create menu options ---------------------------------------------
		viewMenu = mainMenu.addMenu('ინტერფეისი')                         # create menu section
		viewMenu.setStyleSheet("""QWidget {	background-color: rgba(0,41,150,255);
											color:white;
											font-weight:bold;}""")
		toggleTool = QAction("ინსტრუმენტთა ველი",self,checkable=True)    # create menu option
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
		saveAct.triggered.connect(lambda : self.statusBarMessage("შენახვა"))         # run function
# ------------------------------------------------------- copy -----------------------------------------------------
		copyAct = QAction(QIcon('img/copy.png'),'ასლი', self)              # create Copy button in toolBar
		copyAct.setShortcut("Ctrl+C")                                      # key manipulation of Copy button
		copyAct.triggered.connect(lambda : self.table1.copy() if self.tabs.currentIndex() == 0 else self.table2.copy())     # run function
		copyAct.triggered.connect(lambda : self.statusBarMessage("ასლი"))
# ------------------------------------------------------ paste -----------------------------------------------------
		pasteAct = QAction(QIcon('img/paste.png'),'ასლის ჩაკვრა', self)           # create paste button in toolBar
		pasteAct.setShortcut("Ctrl+V")                                     # key manipulation of paste button
		pasteAct.triggered.connect(lambda : self.table1.paste() if self.tabs.currentIndex() == 0 else self.table2.paste())
		pasteAct.triggered.connect(lambda : self.statusBarMessage("ასლის ჩაკვრა"))
# ------------------------------------------------------- play -----------------------------------------------------
		playAct = QAction(QIcon('img/play.png'),'გაშვება', self)            # create play button in toolBar
		playAct.setShortcut("Ctrl+P")                                      # key manipulation of play button
		playAct.triggered.connect(self.play)                               # run function
		playAct.triggered.connect(lambda : self.statusBarMessage('ლინკის გაშვება')) # run function
#--------------------------------------------- Row - Column manipulation -------------------------------------------
# ------------------------------------------------ insert Row toolbar ----------------------------------------------
		insRowAct = QAction(QIcon('img/addRow.png'), 'სტრიქონის დამატება', self) # create addRow button in toolBar
		insRowAct.triggered.connect(lambda : self.table1.insRow() if self.tabs.currentIndex() == 0 else self.table2.insRow()) # run function
		insRowAct.triggered.connect(lambda : self.statusBarMessage('სტრიქონის დამატება')) # run function
# ------------------------------------------------ Delete Row toolbar ----------------------------------------------
		DelRowAct = QAction(QIcon('img/DelRow.png'), 'სტრიქონის წაშლა', self)    # create delRow button in toolBar
		DelRowAct.triggered.connect(lambda : self.table1.delRow() if self.tabs.currentIndex() == 0 else self.table2.delRow()) # run function
		DelRowAct.triggered.connect(lambda : self.statusBarMessage('სტრიქონის წაშლა')) # run function
# ------------------------------------------------------ Menge -----------------------------------------------------
		mergeAct = QAction(QIcon('img/merge.png'), 'შერწყმა', self)               # create Merge button in toolBar
		mergeAct.triggered.connect(lambda : self.table1.merge() if self.tabs.currentIndex() == 0 else self.table2.merge()) # run function
		mergeAct.triggered.connect(lambda : self.statusBarMessage('უჯრების შერწყმა')) # run function
#-------------------------------------------------------- Font -----------------------------------------------------
# --------------------------------------------------- Font toolbar -------------------------------------------------
		FontAct = QAction(QIcon('img/Font.png'), 'ფონტები', self)                # create Font button in toolBar
		FontAct.triggered.connect(lambda : self.table1.font() if self.tabs.currentIndex() == 0 else self.table2.font()) # run function
		FontAct.triggered.connect(lambda : self.statusBarMessage('ფონტი')) # run function
# --------------------------------------------------- color palete -------------------------------------------------
		colorAct = QAction(QIcon('img/color.png'), 'ტექსტის ფერი', self)       # create Font button in toolBar
		colorAct.triggered.connect(lambda : self.table1.color() if self.tabs.currentIndex() == 0 else self.table2.color()) # run function
		colorAct.triggered.connect(lambda : self.statusBarMessage('ტექსტის ფერი')) # run function
# ------------------------------------------------- background color -----------------------------------------------
		backColorAct = QAction(QIcon("img/background-color.png"),"ფონის ფერი",self)  # create Font button in toolBar
		backColorAct.triggered.connect(lambda : self.table1.FontBackColor() if self.tabs.currentIndex() == 0 else self.table2.FontBackColor()) # run function
		backColorAct.triggered.connect(lambda : self.statusBarMessage('ფონის ფერი')) # run function
# ---------------------------------------------------- alignLeft  --------------------------------------------------
		alignLeftAct = QAction(QIcon('img/alignLeft.png'), 'ტექსტი მარცხნივ', self)  # create Font button in toolBar
		alignLeftAct.triggered.connect(lambda : self.table1.alignLeft() if self.tabs.currentIndex() == 0 else self.table2.alignLeft()) # run function
		alignLeftAct.triggered.connect(lambda : self.statusBarMessage('ტექსტი მარცხნივ')) # run function
# ---------------------------------------------------- alignRight  -------------------------------------------------
		alignRightAct = QAction(QIcon('img/alignRight.png'), 'ტექსტი მარჯვნივ', self) # create Font button in toolBar
		alignRightAct.triggered.connect(lambda : self.table1.alignRight() if self.tabs.currentIndex() == 0 else self.table2.alignRight()) # run function
		alignRightAct.triggered.connect(lambda : self.statusBarMessage('ტექსტი მარჯვნივ')) # run function
# --------------------------------------------------- alignCenter  -------------------------------------------------
		alignCenterAct = QAction(QIcon('img/alignCenter.png'), 'ტექსტი ცენტრში', self)
		alignCenterAct.triggered.connect(lambda : self.table1.alignCenter() if self.tabs.currentIndex() == 0 else self.table2.alignCenter())
		alignCenterAct.triggered.connect(lambda : self.statusBarMessage('ტექსტი ცენტრში'))
# ---------------------------------------------------- settings  ---------------------------------------------------
		settingsAct = QAction(QIcon('img/settings.png'), 'პარამეტრები', self)         # create Font button in toolBar
		settingsAct.triggered.connect(self.settings)                                  # run function
		self.statusBarMessage("პარამეტრები")
# ---------------------------------------------- Print data structure ----------------------------------------------
		printAct = QAction(QIcon('img/print.png'), 'მონაცემთა დაბეჭვდა', self)        # create Font button in toolBar
		printAct.triggered.connect(self.printData)                                    # run function
		printAct.triggered.connect(lambda : self.statusBarMessage('მონაცემთა დაბეჭვდა'))  # run function
# ----------------------------------------------- save data template -----------------------------------------------
		#saveTemplateAct = QAction(QIcon('img/template.png'), 'მონაცემთა შაბლონი', self)  # create Font button in toolBar
		#saveTemplateAct.triggered.connect(self.dataTemplate)                              # run function
		#saveTemplateAct.triggered.connect(lambda : self.table1.openData(temp_data['data_tab1']))        # run function
		#saveTemplateAct.triggered.connect(lambda : self.table2.openData(temp_data['data_tab2']))        # run function
		#saveTemplateAct.triggered.connect(lambda : self.statusBarMessage('მონაცემთა შაბლონი'))        # run function
# ------------------------------------------------------ Test ------------------------------------------------------
		testAct = QAction(QIcon('img/test.png'), 'ტესტი', self)                       # create Test button in toolBar
		#testAct.triggered.connect(lambda : self.table1.calculations(temp_data))        # run function
		testAct.triggered.connect(self.test)                                           # run function
		testAct.triggered.connect(lambda : self.statusBarMessage('ტესტი'))                                           # run function
# ------------------------------------------- add buttons on first toolbar -----------------------------------------
		self.toolbar = self.addToolBar('Tools')
		self.toolbar.setStyleSheet("""QWidget {	background-color: rgba(0,41,59,255);
												color:white;
												font-weight:bold;
												border-style: solid;
												border-radius: 10px; 
												border-width: 1px;
												border-color: rgba(127,127,255,255);}""")
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
		#self.toolbar.addAction(saveTemplateAct)
		self.toolbar.addAction(testAct)
		self.addToolBarBreak()
		self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.addToolBar(Qt.TopToolBarArea , self.toolbar)
# ------------------------------------------------ Create tabs widget ----------------------------------------------
		self.tabs = QTabWidget()
		self.tabs.setStyleSheet("""	QWidget {	background-color: rgba(0,41,59,255);
												color:white;
												font-weight:bold;
												border-style: solid;
												border-radius: 3px;
												border-width: 1px;
												border-color: rgba(0,41,59,255);}""")
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()
# -------------------------------------------------- add tab pages -------------------------------------------------
# ---------------------------------------------------- Add tabs ----------------------------------------------------
		self.tabs.addTab(self.tab1, "მიმდინარე")
		self.tabs.addTab(self.tab2, "ლინკები")
		self.tabs.addTab(self.tab3, "გრაფიკები")
		self.tabs.addTab(self.tab4, "ტერმინალი")
		self.setCentralWidget(self.tabs)
# ------------------------------------------------ set tab1 layouts ------------------------------------------------
		self.VlayoutTab1 = QVBoxLayout()
		self.HlayoutTab1 = QHBoxLayout()
# ------------------------------------------------ set tab2 layouts ------------------------------------------------
		self.VlayoutTab2 = QVBoxLayout()
# ------------------------------------------------ set tab3 layouts ------------------------------------------------
		self.VlayoutTab3 = QVBoxLayout()
# ------------------------------------------------ set tab4 layouts ------------------------------------------------
		self.VlayoutTab4 = QVBoxLayout()
# --------------------------------------------------- Search_tab1 --------------------------------------------------
		self.HlayoutSearch_tab1 = QHBoxLayout()
		self.search_line_tab1 = LineEdit()
		self.search_line_tab1.setPlaceholderText("Search to...")
		self.search_but_tab1 = PushBut("ძებნა")
		self.search_but_tab1.setIcon(QIcon('img/find.png'))
		self.search_next_tab1 = PushBut("შემდეგი")
		self.search_next_tab1.setIcon(QIcon('img/next.png'))
		self.searchInfoLabel_tab1 = QLabel("    ")
		self.searchInfoLabel_tab1.setStyleSheet("""	margin: 1px; 
													padding: 7px;
													background-color: rgba(0,255,255,100); 
													color: rgba(255,255,255,255); 
													border-style: solid; 
													border-radius: 3px; 
													border-width: 0.5px; 
													border-color: rgba(0,140,255,255);""")
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
		self.search_line_tab2 = LineEdit()
		self.search_line_tab2.setPlaceholderText("Search to...")
		self.search_but_tab2 = PushBut("ძებნა")
		self.search_but_tab2.setIcon(QIcon('img/find.png'))
		self.search_next_tab2 = PushBut("შემდეგი")
		self.search_next_tab2.setIcon(QIcon('img/next.png'))
		self.searchInfoLabel_tab2 = QLabel("    ")
		self.searchInfoLabel_tab2.setStyleSheet("""	margin: 1px; 
													padding: 7px;
													background-color: rgba(0,255,255,100); 
													color: rgba(255,255,255,255); 
													border-style: solid; 
													border-radius: 3px; 
													border-width: 0.5px; 
													border-color: rgba(0,140,255,255);""")
		self.searchInfoLabel_tab2.setText("0")
		self.search_but_tab2.clicked.connect(lambda : self.searchInfoLabel_tab2.setText(str(self.table2.find_items(self.search_line_tab2.text()))))
		self.search_next_tab2.clicked.connect(lambda : self.table2.find_items(self.search_line_tab2.text()))

		self.HlayoutSearch_tab2.addWidget(self.search_line_tab2)
		self.HlayoutSearch_tab2.addWidget(self.search_but_tab2)
		self.HlayoutSearch_tab2.addWidget(self.search_next_tab2)
		self.HlayoutSearch_tab2.addWidget(self.searchInfoLabel_tab2)

		self.VlayoutTab2.addLayout(self.HlayoutSearch_tab2)
# --------------------------------------------------- Content List -------------------------------------------------
		self.contentList = QListWidget()
		self.contentList.setWindowTitle('კონტენტი')
		self.contentList.itemClicked.connect(self.test)
		self.contentList.setMaximumWidth(200)
		self.contentList.itemClicked.connect(self.t)
		self.HlayoutTab1.addWidget(self.contentList)
# ----------------------------------- create table1 widget and add on vertical layut -------------------------------
		col_width_array_tab1 = {0 : 500, 1 : 120, 2 : 130, 3 : 170, 4 : 400, 5 : 250}
		self.table1 = TableView(temp_data['data_tab1'], col_width_array_tab1, 50, len(temp_data['data_tab1']['header']))
		self.table1.openData(temp_data['data_tab1'])
		self.HlayoutTab1.addWidget(self.table1)
		self.BGColorCalculation()
		self.table1.cellChanged.connect(self.calculationEvent)
		self.VlayoutTab1.addLayout(self.HlayoutTab1)
# ----------------------------------- create table2 widget and add on vertical layut -------------------------------
		col_width_array_tab2 = {0 : 590, 1 : 590, 2 : 590}
		self.table2 = TableView(temp_data['data_tab2'], col_width_array_tab2, 50, len(temp_data['data_tab2']['header']))
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
		self.splitter1.setStyleSheet("""QSplitter::handle:horizontal {	border: 2px dashed blue;
																		margin: 1px 1px;}""")
		self.splitter1.addWidget(self.plot1)
		self.splitter1.addWidget(self.plot2)

		self.splitter2 = QSplitter(Qt.Vertical)
		self.splitter2.setStyleSheet("""QSplitter::handle:vertical {	border: 2px dashed blue;
																		margin: 1px 1px;}""")
		self.splitter2.addWidget(self.splitter1)
		self.splitter2.addWidget(self.plot3)
		self.splitter2.addWidget(self.plot4)
		self.Hlayout_spliter = QHBoxLayout()
		self.Hlayout_spliter.addWidget(self.splitter2)
		self.VlayoutTab3.addLayout(self.Hlayout_spliter)
#------------------------------------------------------ Terminal ---------------------------------------------------
		self.terminal = QPlainTextEdit(self)
		self.terminal.setStyleSheet("""QWidget {background-color: rgba(0,41,59,255);
												color:white;
												font-weight:bold;
												border-style: solid; 
												border-radius: 10px; 
												border-width: 0.5px;
												border-color: rgba(0,140,255,255);}
									QScrollBar:horizontal {	width: 12px; 
															height: 12px;
															background-color: rgba(0,41,59,255);}
									QScrollBar:vertical {	width: 12px;
															height: 12px;
															background-color: rgba(0,41,59,255);}""")
		self.VlayoutTab4.addWidget(self.terminal)
# ------------------------------------------------- set tab 1 layout  ----------------------------------------------
		self.tab1.setLayout(self.VlayoutTab1)
# ------------------------------------------------- set tab 2 layout  ----------------------------------------------
		self.tab2.setLayout(self.VlayoutTab2)
# ------------------------------------------------- set tab 3 layout  ----------------------------------------------
		self.tab3.setLayout(self.VlayoutTab3)
# ------------------------------------------------- set tab 4 layout  ----------------------------------------------
		self.tab4.setLayout(self.VlayoutTab4)
		self.statusBarMessage("")
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
		self.statusBarMessage("ტერმინალში ბეჭვდა")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ play +++++++++++++++++++++++++++++++++++++++++++++++++++++
	def play(self):
		import os
		try:
			if self.tabs.currentIndex() == 0:
				l = self.table1.item(self.table1.currentRow(), 4)
			if self.tabs.currentIndex() == 1:
				l = self.table2.item(self.table2.currentRow(), 1)
			os.startfile(l.text())
			self.statusBarMessage('გაშვება')
		except:
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
		self.statusBarMessage('მონაცემთა შემოტანა')
# ++++++++++++++++++++++++++++++++++++++++++ Print data structure button +++++++++++++++++++++++++++++++++++++++++++
	def printData(self):
		self.term(" კონფიგურაცია ---> " + str(pformat(temp_data['config'], indent=4)))
		self.term(" ჰედერი 1 ---> " + str(pformat(temp_data['data_tab1']['header'], indent=4)))
		self.term(" შერწყმა 1 ---> " + str(pformat(temp_data['data_tab1']['Merge'], indent=4)))
		self.term(" ცხრილის 1 ---> " + str(pformat(temp_data['data_tab1']['table'], indent=4)))
		self.term(" ცხრილის 1 ზომა ---> " + str(len(temp_data['data_tab1']['table'])))
		self.term(" ჰედერი 2 ---> " + str(pformat(temp_data['data_tab2']['header'], indent=4)))
		self.term(" შერწყმა 2 ---> " + str(pformat(temp_data['data_tab2']['Merge'], indent=4)))
		self.term(" ცხრილის 2 ---> " + str(pformat(temp_data['data_tab2']['table'], indent=4)))
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
		self.statusBarMessage('მონაცემთა შაბლონის შენახვა')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++ settings +++++++++++++++++++++++++++++++++++++++++++++++++++  bug with cancel
	def settings(self):
		from SettingsDialog import Settings
		self.diag = Settings(temp_data['config'])
		self.diag.exec_()
		self.setGeometry(self.left, self.top, int(temp_data['config']["length"]), int(temp_data['config']["width"]))
		self.statusBarMessage("პარამეტრები")
# ++++++++++++++++++++++++++++++++++++++++++++++ Time stamp to seconds +++++++++++++++++++++++++++++++++++++++++++++
	def timeStampToSec(self, timeStamp):
		from datetime import datetime
		try:
			pt = datetime.strptime(timeStamp,'%H:%M:%S')
		except ValueError:
			pt = datetime.strptime(timeStamp,'%M:%S')
		total_seconds = pt.second + pt.minute*60 + pt.hour*3600
		return int(total_seconds)
# ++++++++++++++++++++++++++++++++ Update Background color and progress calculation ++++++++++++++++++++++++++++++++
	def BGColorCalculation(self):
		for row in range(self.table1.rowCount()):
			try:
				if self.table1.item(row, 2).text() != "" and type(int(self.table1.item(row, 2).text()) == type(int(0))):
					newitem = QProgressBar()
					newitem.setAlignment(Qt.AlignCenter)
					newitem.setValue(round(float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text())*100, 1))
					self.table1.setCellWidget(row, 3, newitem)

					if float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) == 1:
						for column in range(self.table1.columnCount()):
							try:
								self.table1.item(row, column).setBackground(QtGui.QColor(0, 170, 0, 255))
							except AttributeError:
								newitem = QTableWidgetItem(None)
								self.table1.setItem(row, column, newitem)
								newitem.setBackground(QtGui.QColor(0, 170, 0, 255))

					if float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) > 0.8 and float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) <= 0.9:
						for column in range(self.columnCount()):
							try:
								self.item(row, column).setBackground(QtGui.QColor(0, 170, 127, 255))
							except AttributeError:
								newitem = QTableWidgetItem(None)
								self.table1.setItem(row, column, newitem)
								newitem.setBackground(QtGui.QColor(0, 170, 127, 255))
					
					if float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) >= 0.3 and float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) <= 0.8:
						for column in range(self.table1.columnCount()):
							try:
								self.table1.item(row, column).setBackground(QtGui.QColor(255, 255, 127, 255))
							except AttributeError:
								newitem = QTableWidgetItem(None)
								self.table1.setItem(row, column, newitem)
								newitem.setBackground(QtGui.QColor(255, 255, 127, 255))

					if float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) < 0.3 and float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) != 0:
						for column in range(self.table1.columnCount()):
							try:
								self.table1.item(row, column).setBackground(QtGui.QColor(255, 170, 0, 255))
							except AttributeError:
								newitem = QTableWidgetItem(None)
								self.table1.setItem(row, column, newitem)
								newitem.setBackground(QtGui.QColor(255, 170, 0, 255))

					if float(self.table1.item(row, 1).text())/float(self.table1.item(row, 2).text()) == 0:
						for column in range(self.columnCount()):
							try:
								self.table1.item(row, column).setBackground(QtGui.QColor(170, 170, 127, 255))
							except AttributeError:
								newitem = QTableWidgetItem(None)
								self.table1.setItem(row, column, newitem)
								newitem.setBackground(QtGui.QColor(170, 170, 127, 255))

			except AttributeError:
				pass
			except ZeroDivisionError:
				newitem = QTableWidgetItem('Inf')
				self.table1.setItem(row, 3, newitem)
				pass
			except ValueError:
				newitem = QProgressBar()
				newitem.setAlignment(Qt.AlignCenter)
				try:
					newitem.setValue(round(self.timeStampToSec(self.table1.item(row, 1).text())/self.timeStampToSec(self.table1.item(row, 2).text())*100, 1))
					self.table1.setCellWidget(row, 3, newitem)
				except ValueError:
					self.table1.removeCellWidget(row, 3)
					pass
				pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++ TABLE EVENT ++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++ Calculation Event +++++++++++++++++++++++++++++++++++++++++++++++
	def calculationEvent(self):
		try:
			item = self.table1.item(self.table1.currentRow(), self.table1.currentColumn())
			self.table1.value = item.text()
			if self.table1.value is not '':
				self.BGColorCalculation()
		except AttributeError:
			pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++ Test +++++++++++++++++++++++++++++++++++++++++++++++++++++
	def test(self):
		#from pprint import pprint
		self.contentNamesList = []
		self.contentList.clear()
		for row in range(self.table1.rowCount()):
			try:
				if isinstance(None, type(self.table1.item(row, 4))):
					self.contentNamesList.append(self.table1.item(row, 0).text())
				else:
					if self.table1.item(row, 4).text() == "" and self.table1.item(row, 2).text() == "":
						self.contentNamesList.append(self.table1.item(row, 0).text())
			except AttributeError:
				pass
		self.term(str(pformat(self.contentNamesList, indent=4)))
		self.contentList.addItems(self.contentNamesList)

		self.statusBarMessage('ტესტი')

	def t(self):
		self.term(str(self.contentList.text()))
####################################################################################################################
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	ex = App('Bookmark Manager',50,30,"img/link.png")
	ex.show()
	sys.exit(app.exec_())


# search cell select bug
# add home and end buttons
# add right cklik cell sub menu
# add undo and redo functions
# add cut function
# search bug fix +
# add content list
# 