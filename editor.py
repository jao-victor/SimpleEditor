from PyQt5 import QtWidgets
import sys
from  classEditor import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Editor(QMainWindow):

	def __init__(self):
		super().__init__()
		self.editor = Ui_MainWindow()
		self.editor.setupUi(self)

		self.editor.actionSalvar_como_2.triggered.connect(self.salvar)
		self.editor.actionAbrir.triggered.connect(self.abrir)

	def salvar(self):

		caminho = QtWidgets.QFileDialog.getSaveFileName()[0]
		self.codigo = self.editor.areaCodigo.toPlainText() #captura o conteúdo do editor

		with open(caminho + '.py', 'w') as file:
			file.write(self.codigo)
			file.close()

	def abrir(self):

		caminho = QtWidgets.QFileDialog.getOpenFileName()[0]
		with open(caminho, 'r') as arquivo:
			self.codigo = arquivo.read()
			self.editor.areaCodigo.setPlainText(self.codigo)



app = QtWidgets.QApplication([])

editor = Editor()
editor.show()

sys.exit(app.exec_())
