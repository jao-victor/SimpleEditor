from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from  classEditor2 import Ui_SimpleEditor
from PyQt5.QtWidgets import QMainWindow
import os

class Editor(QMainWindow):

	def __init__(self):
		super().__init__()
		self.editor = Ui_SimpleEditor()
		self.editor.setupUi(self)
		self.editor.actionSalvar_como.triggered.connect(self.salvar)
		self.editor.actionAbrir.triggered.connect(self.abrir)
		self.editor.rodar.clicked.connect(self.executar)
		self.editor.actionPython.triggered.connect(self.python)
		self.editor.actionC.triggered.connect(self.C)
		self.editor.actionJava.triggered.connect(self.java)

		self.caminho = ' '
		self.comp = 'python3'
		self.ext = '.py'


	def python(self):
		import platform
		self.ext = '.py'
		if (platform.system() == "Windows"):
			self.comp = "python"
		else:
			self.comp = "python3"

	def java(self):
		self.ext = '.java'

	def C (self):
		self.ext = '.c'

	def salvar(self):

		self.codigo = self.editor.areaCodigo.toPlainText() #captura o conteúdo do editor

		if(self.caminho != ' '):
			with open(self.caminho+self.ext, 'w') as file:
				file.write(self.codigo)
				self.file = file
				file.close()

		else:

			self.caminho = QtWidgets.QFileDialog.getSaveFileName()[0]

			if(self.ext == '.py'):
				with open(self.caminho + '.py', 'w') as file:
					file.write(self.codigo)
					self.file = file
					file.close()

			if (self.ext == '.java'):
				with open(self.caminho + '.java', 'w') as file:
					file.write(self.codigo)
					self.file = file
					file.close()

			if (self.ext == '.c'):
				with open(self.caminho + '.c', 'w') as file:
					file.write(self.codigo)
					self.file = file
					file.close()

	def abrir(self):

		self.caminho = QtWidgets.QFileDialog.getOpenFileName()[0]
		print(self.caminho)
		with open(self.caminho, 'r') as arquivo:
			self.codigo = arquivo.read()
			self.editor.areaCodigo.setPlainText(self.codigo)



			

	def executar(self):

		if(self.caminho != ' ' and self.ext == '.java'):
			os.system(f'javac {self.caminho}.java')
			os.system(f'java {self.caminho.split("/")[-1]}')

		elif(self.caminho != ' ' and self.ext == '.c'):
			os.system(f'gcc {self.caminho}.c -o {self.caminho.split("/")[-1]}')
			os.system(f'./{self.caminho.split("/")[-1]}')

		elif(self.caminho != ' ' and self.ext == '.py'):
			os.system(f'{self.comp} {self.caminho}.py')

		else:
			msg = QMessageBox()
			msg.setWindowTitle("WARNING")
			msg.setText("Salve seu arquivo")
			msg.setIcon(QMessageBox.Critical)
			msg.exec()

app = QtWidgets.QApplication([])

editor = Editor()
editor.show()

sys.exit(app.exec_())
