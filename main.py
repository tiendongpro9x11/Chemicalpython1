# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import re
import os
import popplerqt4
from displayHidrocacbon import *
import chemical
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)
content = ""
class Ui_Form(object):
	def __init__(self):
		self.kindien = True
		self.styleof = ""
		self.Elemlist = []
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(1200, 577)
		self.area = QtGui.QScrollArea(Form)
		self.area.setGeometry(QtCore.QRect(10,55,1200,800))
		self.lineEdit = QtGui.QLineEdit(Form)
		self.lineEdit.setGeometry(QtCore.QRect(10, 10, 113, 40))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(130, 10, 161, 40))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))

		self.pushButton_2  = QtGui.QPushButton(Form)
		self.pushButton_2.setGeometry(QtCore.QRect(400,10,160,40))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_2.setVisible(False)

		self.comboBox = QtGui.QComboBox(Form)
		self.comboBox.setGeometry(QtCore.QRect(295,10,100,40))
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.comboBox.setVisible(False)

		self.label = QtGui.QLabel(self.area)
		self.label.setText(_fromUtf8(""))
		self.label.setObjectName(_fromUtf8("label"))

		self.pushButton.clicked.connect(self.submit_f1)
		self.pushButton_2.clicked.connect(self.disProperties)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Form", None))
		self.pushButton.setText(_translate("Form", "Display Hidrocacbon", None))
		self.pushButton_2.setText(_translate("Form", "Display properties", None))
		self.lineEdit.setText(_translate("Form", "C4H8", None))
	
	def submit_f1(self):
		if not self.lineEdit.text().isEmpty():
			self.shots = str(self.lineEdit.text())
			self.number_shot = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", self.shots)
			if self.shots == "CH4" or self.shots == "ch4":
				self.number_shot[0] = 1
				self.number_shot.append(4)
			self.show_shots()
	def setAnkin(self):
		self.kindien = True
	def setAnkadien(self):
		self.kindien = False
	def disProperties(self):
		##--display proerties
		ind = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*",self.comboBox.currentText())
		ind = int(ind[0])
		flag = False
		content = "\documentclass[a4paper]{article}\n\setlength{\parindent}{0pt}\n\\newcommand\\tab[1][1cm]{\hspace*{#1}}\n\usepackage{mathtools}\n\usepackage[utf8]{vietnam}\n\usepackage{chemfig}\n\usepackage[margin=2pt]{geometry}\n\\begin{document}\n"
		if self.styleof=="ankan":
			b = chemical.ankan()
			# with open(os.getcwd()+"/logfile.log","w") as F:
			content+= b.display(self.Elemlist[ind])
			flag = True
		if self.styleof=="anken":
			b = chemical.anken()
			# with open(os.getcwd()+"/logfile.log","a") as F:
			content+=b.display(self.Elemlist[ind])
			flag = True
		if flag:
			content = content + '\n\end{document}'
			with open(os.getcwd()+"/test.tex","w") as F:
				F.write(content)
			os.system("pdflatex "+os.getcwd()+"/test.tex")
			self.readpdffile()
	def show_shots(self):
		
		c = int(self.number_shot[0])
		if self.number_shot[1]:
			h = int(self.number_shot[1])
		if c > 8:
			self.showNotification("n < 9")
			return
		content = "\documentclass[a4paper]{article}\n\setlength{\parindent}{0pt}\n\\newcommand\\tab[1][1cm]{\hspace*{#1}}\n\usepackage{mathtools}\n\usepackage[utf8]{vietnam}\n\usepackage{chemfig}\n\usepackage[margin=2pt]{geometry}\n\\begin{document}\n"
		flag = False
		if (c*2+2) == h and c >= 1:
			self.styleof = "ankan"
			a = DisplayHidro()
			res = a.HidroCacbon2tex(c,self.styleof)
			content = content + res
			flag = True
			##--------------
			self.comboBox.clear()
			for x in range(a.getlist(self.styleof)):
				self.comboBox.addItem("Select: "+str(x))
			self.comboBox.setVisible(True)
			self.pushButton_2.setVisible(True)
			##display properties
			self.Elemlist = a.getElementList(self.styleof)
		elif c*2 == h and c >= 2:
			self.styleof = "anken"
			a = DisplayHidro()
			res = a.HidroCacbon2tex(c,self.styleof )
			content = content + res
			flag = True
			##----------
			self.comboBox.clear()
			for x in range(a.getlist(self.styleof )):
				self.comboBox.addItem("Select: "+str(x))
			self.comboBox.setVisible(True)
			self.pushButton_2.setVisible(True)
			##display properties
			self.Elemlist = a.getElementList(self.styleof)
		elif (c*2-2)==h and c >=2 :
			print "Ankadien or Ankin"
			if c>=3:
				
				msg = QtGui.QDialog()
				but1 = QtGui.QPushButton("Ankadien",msg)
				but1.setGeometry(QtCore.QRect(0,0,100,50))
				but1.clicked.connect(self.setAnkadien)
				but1.clicked.connect(msg.close)
				
				but2 = QtGui.QPushButton("Ankin",msg)
				but2.setGeometry(QtCore.QRect(105,0,100,50))
				but2.clicked.connect(self.setAnkin)
				but2.clicked.connect(msg.close)
				retval = msg.exec_()
			a = DisplayHidro()
			if not self.kindien:
				self.styleof = "ankadien"
				res = a.HidroCacbon2tex(c,self.styleof)
				##----------
				self.comboBox.clear()
				for x in range(a.getlist("ankadien")):
					self.comboBox.addItem("Select: "+str(x))
				self.comboBox.setVisible(True)
				self.pushButton_2.setVisible(True)
			else:
				self.styleof = "ankin"
				res = a.HidroCacbon2tex(c,self.styleof)
				##------------
				self.comboBox.clear()
				for x in range(a.getlist(self.styleof)):
					self.comboBox.addItem("Select: "+str(x))
				self.comboBox.setVisible(True)
				self.pushButton_2.setVisible(True)
				# self.comboBox.removeItem
			content = content +res
			flag = True
			##display properties
			self.Elemlist = a.getElementList(self.styleof)
		elif (c*2-6) ==h and c>=6:
			print "Aren"
			a = DisplayAren()
			res = a.Aren2tex(c)
			content = content + res
			flag = True
			##display properties
			self.Elemlist = a.getElementList(self.styleof)
		else:
			print "Hidrocacbon not difine"
		#thuc tuc voi latex va doc pdf
		if flag:
			content = content + '\n\end{document}'
			with open(os.getcwd()+"/test.tex","w") as F:
				F.write(content)
			os.system("pdflatex "+os.getcwd()+"/test.tex")
			self.readpdffile()
		else:
			self.showNotification("Hidrocacbon not difine")
		#----
	def readpdffile(self):
		doc = popplerqt4.Poppler.Document.load(os.getcwd()+"/test.pdf")
		# print doc
		doc.setRenderHint(popplerqt4.Poppler.Document.Antialiasing)
		doc.setRenderHint(popplerqt4.Poppler.Document.TextAntialiasing)
		page = doc.page(0)
		image = page.renderToImage(150,150)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))
		self.area.setWidget(self.label)
	def showNotification(self,info):
		msg = QtGui.QMessageBox()
		msg.setText(info)
		retval = msg.exec_()
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	# Form.showMaximized()
	Form.show()
	sys.exit(app.exec_())
