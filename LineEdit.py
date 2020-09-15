from PyQt5.QtWidgets import QLineEdit
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Push button design ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LineEdit(QLineEdit):
	def __init__(self, parent=None):
		super(LineEdit, self).__init__(parent)
		self.setStyleSheet("""	margin: 1px;
										padding: 7px;
										background-color: rgba(0,255,255,100); 
										color: rgba(255,255,255,255); 
										border-style: solid; 
										border-radius: 3px; 
										border-width: 0.5px; 
										border-color: rgba(0,140,255,255);""")
