from PyQt5.QtWidgets import QPushButton
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Push button design ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PushBut(QPushButton):
	def __init__(self, parent=None):
		super(PushBut, self).__init__(parent)
		self.setMouseTracking(True)
		self.setStyleSheet("""	margin: 1px;
								padding: 7px; 
								background-color: rgba(1,255,255,100);
								color: rgba(0,190,255,255); 
								border-style: solid;
								border-radius: 3px; 
								border-width: 0.5px; 
								border-color: rgba(127,127,255,255);""")

	def enterEvent(self, event):
		if self.isEnabled() is True:
			self.setStyleSheet("""	margin: 1px; 
									padding: 7px;
									background-color: rgba(1,255,255,100); 
									color: rgba(0,230,255,255); 
									border-style: solid; 
									border-radius: 3px;
									border-width: 0.5px;
									border-color: rgba(0,230,255,255);""")
		if self.isEnabled() is False:
			self.setStyleSheet("""	margin: 1px; 
									padding: 7px; 
									background-color: rgba(1,255,255,100); 
									color: rgba(0,190,255,255);
									border-style: solid;
									border-radius: 3px;
									border-width: 0.5px;
									border-color: rgba(127,127,255,255);""")

	def leaveEvent(self, event):
		self.setStyleSheet("""	margin: 1px; padding: 7px;
								background-color: rgba(1,255,255,100);
								color: rgba(0,190,255,255);
								border-style: solid;
								border-radius: 3px; 
								border-width: 0.5px;
								border-color: rgba(127,127,255,255);""")