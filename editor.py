from PyQt5 import QtWidgets
import sys
from  classEditor import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Editor(QMainWindow):

	def __init__(self):
		super().__init__()
		self.editor = Ui_MainWindow()
		self.editor.setupUi(self)

		self.editor.actionSalvar_como.triggered.connect(self.salvar)

	def salvar(self):

		arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
		self.codigo = self.editor.areaCodigo.toPlainText() #captura o conteúdo do editor

		with open(arquivo + '.py', 'w') as file:
			file.write(self.codigo)


app = QtWidgets.QApplication([])

editor = Editor()
editor.show()

sys.exit(app.exec_())
