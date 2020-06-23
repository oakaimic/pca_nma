#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
Py40 PyQt5 tutorial 
 
This example shows a tooltip on 
a window and a button.
 
author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""
 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import rpy2.robjects as robjects
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import requests
import urllib3.request
import os
import subprocess
import platform
import numpy as np
from multiprocessing import Pool
import gc
from pymol import cmd
class downloadwindow(QWidget):
	def  __init__(self):
		QWidget.__init__(self)
		self.initUI()
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')
		
		self.setGeometry(500, 300, 300, 200)

		self.label=QLabel(self)
		self.label.move(60,100)
		self.label.resize(530,40)
		self.label.setText("input file names")

		self.textbox = QLineEdit(self)
		self.textbox.move(170,110)
		self.textbox.resize(80, 20)
		btn2 = QPushButton('download files', self)
		btn2.move(50, 50)
		btn2.clicked.connect(self.downloadfiles)
	
	def downloadfiles(self):
		print(self.textbox.text())

		name=str(self.textbox.text())

		url='http://ufq.unq.edu.ar/codnas/php/entry_conformers_ws.php'
		post_data={'ID_POOL':name}
		response=requests.post(url,data=post_data)
		r=response.text
		# r = r.encode('unicode-escape').decode('string_escape')
		r=r[:-2]
		r=r[2:]
		r=r.replace('}','')
		r=r.replace('{','')
		array=r.split(',') 
		print(array)
		# os.mkdir('./'+name2)
		#"PDB_id":"1GHD_A"
		with open("./name.txt","w+") as n:
			n.write('name'+"\n")
			for i in range(0,len(array)):
				if array[i].find('PDB_id')>=0:
					pdbID="".join(list(array[i])[10:-1])
					print(pdbID[0:4])
					n.write(pdbID+"\n")
		print("download from now on")
		robjects.r.source("download_c.r")

	def start(self):
		if not self.isVisible():
			self.show()
			
	def close(self):
		self.close()
class pcawindow(QWidget):
	def  __init__(self):
		QWidget.__init__(self)
		self.initUI()
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')
		
		self.setGeometry(500, 300, 300, 200)

		btn2 = QPushButton('choose  files', self)
		btn2.move(50, 50)
		btn2.clicked.connect(self.chooses)

		btn3 = QPushButton('pca analysis  files', self)
		btn3.move(50, 80)
		btn3.clicked.connect(self.anals)

		self.label=QLabel(self)
		self.label.move(60,100)
		self.label.resize(530,40)
		self.label.setText("input pc number")

		self.textbox = QLineEdit(self)
		self.textbox.move(170,110)
		self.textbox.resize(40, 20)
		btn4 = QPushButton('generate pc trajectory', self)
		btn4.move(50, 130)
		btn4.clicked.connect(self.generate)

		self.label01=QLabel(self)
		self.label01.move(160, 110)
		self.label01.setFixedSize(350, 350)

	def generate(self):
		cmd.bg_color("white")
		number=self.textbox.text()
		
		n=str(number)+".py"
		print(n)
		cmd.run(n)
		cmd.png("pc"+str(number)+".png")
		
		imgName01="pc"+str(number)+".png"
		jpg = QtGui.QPixmap(imgName01).scaled(self.label01.width(), self.label01.height())
		self.label01.setPixmap(jpg)
	def anals(self):
		print(self.filename)
		with open("./name1.txt","w+") as n:
			n.write('name'+"\n")
			for i in range(0,len(self.filename)):
					print(self.filename[i])
					n.write(self.filename[i]+"\n")
		robjects.r.source('download1.r')

	def chooses(self):
		self.filename,_ =QFileDialog.getOpenFileNames(self)
		#把选中的文件名写入文件，随后用r进行nma分析
		reply=QMessageBox.information(self,'提示','已经选中这些文件',QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)

	def start(self):
		if not self.isVisible():
			self.show()
			print("a")
	def close(self):
		self.close()
	def pca_analysis(self):
		print("pca analysis")
		robjects.r.source("download.r")

		
class nmawindow(QDialog):
	def  __init__(self):
		QDialog.__init__(self)
		self.initUI()
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
	
		self.setToolTip('This is a <b>QWidget</b> widget')
		# btn0 = QPushButton('nma on a set of structures', self)
		# btn0.move(50, 50)
		# self.setGeometry(500, 300, 300, 200)
		# btn0.clicked.connect(self.nma_analysis)
		
		# self.label=QLabel(self)
		# self.label.move(50,80)
		# self.label.resize(530,40)
		


		btn2 = QPushButton('choose  files', self)
		btn2.move(50, 50)
		btn2.clicked.connect(self.chooses)

		btn3 = QPushButton('nma analysis  files', self)
		btn3.move(50, 100)
		btn3.clicked.connect(self.anals)

	def anals(self):
		print(self.filename)
		with open("./name1.txt","w+") as n:
			n.write('name'+"\n")
			for i in range(0,len(self.filename)):
					print(self.filename[i])
					n.write(self.filename[i]+"\n")
		robjects.r.source('normalModePDBS1.r')
	
	def chooses(self):
		self.filename,_ =QFileDialog.getOpenFileNames(self)
		#把选中的文件名写入文件，随后用r进行nma分析
		reply=QMessageBox.information(self,'提示','已经选中这些文件',QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)

	def start(self):
		if not self.isVisible():
			self.show()
			print("a")
	def close(self):
		self.close()
	def nma_analysis(self):

		self.label.setText('analysed...\n eigenvector has been written into file "./modeVectortxt')
		robjects.r.source("normalModePDBS.r")

class cmptwindow(QDialog):
	close_signal = pyqtSignal()
	def  __init__(self):
		QDialog.__init__(self)
		self.initUI()
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')
		# btn0 = QPushButton('comparison', self)
		# self.setGeometry(500, 300, 300, 200)

		btn1 = QPushButton('projection trajectory for pc1', self)
		btn1.move(50, 50)
		btn1.clicked.connect(self.projection1)

		btn2 = QPushButton('projection trajectory for pc2', self)
		btn2.move(550, 50)

		btn1.clicked.connect(self.projection1)
		btn2.clicked.connect(self.projection2)
		self.label01=QLabel(self)
		self.label01.move(160, 110)
		self.label01.setFixedSize(350, 350)

		self.label02=QLabel(self)
		self.label02.move(580, 110)
		self.label02.setFixedSize(350, 350)
	def projection2(self):
		os.system("python test.py")
		robjects.r.source('pro.r')
		f = open("name.txt","r") 
		name=[]
		line=f.readline()
		numofstructure=0
		while line:
			
			line = f.readline().strip()
			name.append("./aaa/split_chain/"+line+".pdb")
			numofstructure=numofstructure+1
		f="project.txt"
		m=self.getVector(f,len(name)-1)
		print(m[:,0])
		print(m[:,1])
	
		max_1_index=np.argmax(m[:,0])+1
		min_1_index=np.argmin(m[:,0])+1

		max_2_index=np.argmax(m[:,1])+1
		min_2_index=np.argmin(m[:,1])+1
		print(max_1_index,min_1_index)
		print(max_2_index,min_2_index)
		min1="proj_pc1_"+str(min_1_index)
		max1="proj_pc1_"+str(max_1_index)
		min2="proj_pc2_"+str(min_2_index)
		max2="proj_pc2_"+str(max_2_index)
		print(min1,max1,min2,max2)
		cmd.bg_color("white")
		cmd.run("2.py")
		cmd.load(min2+".pdb")
		cmd.load(max2+".pdb")
		cmd.color("green",min2)
		cmd.color("gray","prot")
		cmd.color("blue",max2)
		cmd.png("2.png")
		imgName02="2.png"
		jpg = QtGui.QPixmap(imgName02).scaled(self.label02.width(), self.label02.height())
		self.label02.setPixmap(jpg)

	def projection1(self):
		os.system("python test.py")
		robjects.r.source('pro.r')
		f = open("name.txt","r") 
		name=[]
		line=f.readline()
		numofstructure=0
		while line:
			
			line = f.readline().strip()
			name.append("./aaa/split_chain/"+line+".pdb")
			numofstructure=numofstructure+1
		f="project.txt"
		m=self.getVector(f,len(name)-1)
		print(m[:,0])
		print(m[:,1])
	
		max_1_index=np.argmax(m[:,0])+1
		min_1_index=np.argmin(m[:,0])+1

		max_2_index=np.argmax(m[:,1])+1
		min_2_index=np.argmin(m[:,1])+1
		print(max_1_index,min_1_index)
		print(max_2_index,min_2_index)

		cmd.bg_color("white")
		cmd.run("1.py")
		min1="proj_pc1_"+str(min_1_index)
		max1="proj_pc1_"+str(max_1_index)
		min2="proj_pc2_"+str(min_2_index)
		max2="proj_pc2_"+str(max_2_index)
		print(min1,max1,min2,max2)
		cmd.load(min1+".pdb")
		cmd.load(max1+".pdb")
		cmd.load("avg.pdb")
		cmd.color("green",min1)
		cmd.color("gray","prot")
		cmd.color("black","avg")
		cmd.color("blue",max1)
		cmd.png("1.png")

		

		imgName01="1.png"
		jpg = QtGui.QPixmap(imgName01).scaled(self.label01.width(), self.label01.height())
		self.label01.setPixmap(jpg)
		
		
	def getVector(self,file,number):
		f=open(file,"r")
		s=f.read()
		a=s.split("\n")

		vectorMatrix=np.zeros((number,int(len(a)/number)))

		k=0
		
		for i in range(0,number):
			for j in range(0,int(len(a)/number)):
				if a[k]=='NA':
					a[k]=0
				vectorMatrix[i][j]=a[k]
				k=k+1

		return vectorMatrix
	def start(self):
		if not self.isVisible():
			self.show()
			
	def close(self):
		self.close()
class cmpwindow(QDialog):
	close_signal = pyqtSignal()
	def  __init__(self):
		QDialog.__init__(self)
		self.initUI()
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		
		self.setToolTip('This is a <b>QWidget</b> widget')
		# btn0 = QPushButton('comparison', self)
		# self.setGeometry(500, 300, 300, 200)

		btn1 = QPushButton('projection histogram', self)
		btn1.move(50, 50)
		btn1.clicked.connect(self.projection)


		btn2 = QPushButton('view histogram', self)
		btn2.move(50, 80)
		btn2.clicked.connect(self.view)

		btn3 = QPushButton('cancel view histogram', self)
		btn3.move(200, 80)
		btn3.clicked.connect(self.cancelview)

		self.label01=QLabel(self)
		self.label01.move(160, 110)
		self.label01.setFixedSize(350, 350)

		self.label02=QLabel(self)
		self.label02.move(160, 500)
		self.label02.setFixedSize(350, 350)

		self.label11=QLabel(self)
		self.label11.move(580, 110)
		self.label11.setFixedSize(350, 350)

		self.label12=QLabel(self)
		self.label12.move(580, 500)
		self.label12.setFixedSize(350, 350)

		self.label21=QLabel(self)
		self.label21.move(1000, 110)
		self.label21.setFixedSize(350, 350)

		self.label22=QLabel(self)
		self.label22.move(1000, 500)
		self.label22.setFixedSize(350, 350)

		self.label1=QLabel(self)
		self.label1.move(200, 470)
		

		self.label1_=QLabel(self)
		self.label1_.move(200, 870)
		

		self.label2=QLabel(self)
		self.label2.move(580, 470)
	

		self.label2_=QLabel(self)
		self.label2_.move(580, 870)
		

		self.label3=QLabel(self)
		self.label3.move(1000, 470)
		

		self.label3_=QLabel(self)
		self.label3_.move(1000, 870)

		self.label3_.setText("mode 3 project on pc2")
		self.label1.setText("mode 1 project on pc1")
		self.label1_.setText("mode 1 project on pc2")
		self.label2.setText("mode 2 project on pc1")
		self.label2_.setText("mode 2 project on pc2")
		self.label3.setText("mode 3 project on pc1")
		
	def cancelview(self):
		self.label01.setPixmap(QPixmap(""))
		self.label02.setPixmap(QPixmap(""))
		self.label11.setPixmap(QPixmap(""))
		self.label12.setPixmap(QPixmap(""))
		self.label21.setPixmap(QPixmap(""))
		self.label22.setPixmap(QPixmap(""))

		self.label3_.setText("")
		self.label1.setText("")
		self.label1_.setText("")
		self.label2.setText("")
		self.label2_.setText("")
		self.label3.setText("")
	def projection(self):
		os.system("python normalModeProjectionPCAHistogram.py")

	def view(self):
		imgdir="./normalModeProjectionPCAfigure/"
		with open('./name1.txt') as f:
			s=len(f.readlines())
		print(s)
		imgName01=imgdir+"mode_0_pc1.png"
		jpg = QtGui.QPixmap(imgName01).scaled(self.label01.width(), self.label01.height())
		self.label01.setPixmap(jpg)
		
		imgName02=imgdir+"mode_0_pc2.png"
		jpg = QtGui.QPixmap(imgName02).scaled(self.label02.width(), self.label02.height())
		self.label02.setPixmap(jpg)

		imgName03=imgdir+"mode_1_pc1.png"
		jpg = QtGui.QPixmap(imgName03).scaled(self.label11.width(), self.label11.height())
		self.label11.setPixmap(jpg)


		imgName04=imgdir+"mode_1_pc2.png"
		jpg = QtGui.QPixmap(imgName04).scaled(self.label12.width(), self.label12.height())
		self.label12.setPixmap(jpg)

		imgName05=imgdir+"mode_2_pc1.png"
		jpg = QtGui.QPixmap(imgName05).scaled(self.label21.width(), self.label21.height())
		self.label21.setPixmap(jpg)

		imgName06=imgdir+"mode_2_pc2.png"
		jpg = QtGui.QPixmap(imgName06).scaled(self.label22.width(), self.label22.height())
		self.label22.setPixmap(jpg)

		
	def start(self):
		if not self.isVisible():
			self.show()
			
	def close(self):
		self.close()

class Example(QWidget):
    close_signal = pyqtSignal()
    def __init__(self):
    	super().__init__()
    	self.initUI()
 

    def nma_compare_pca(self):
    	print("c")
    
    	os.system("python normalModeProjectionPCAHistogram.py")
    	os.system("python test.py")
    	robjects.r.source("pro.r")

    	


    def initUI(self):
        #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        
        #创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        #创建一个PushButton并为他设置一个tooltip
        self.btn0 = QPushButton('download files', self)
        self.btn = QPushButton('pca analysis on a set of structure', self)
        self.btn1 = QPushButton('nma analysis on a set of structure', self)
        self.btn2 = QPushButton('comparison histogram', self)
        self.btn3=QPushButton('comparison trajectory', self)

        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        #btn.sizeHint()显示默认尺寸
        self.btn.resize(self.btn.sizeHint())
        self.btn1.resize(self.btn.sizeHint())
        self.btn2.resize(self.btn.sizeHint())
        self.btn3.resize(self.btn.sizeHint())

        #移动窗口的位置
        self.btn0.move(50, 20)
        self.btn.move(50, 50)
        self.btn1.move(50, 80)
        self.btn2.move(50, 110)           
        self.btn3.move(50, 140)   
        # btn.clicked.connect(self.pca_analysis)
        # btn1.clicked.connect(self.nma_analysis)
        # btn2.clicked.connect(self.nma_compare_pca)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()
    def closeEvent(self, event):
    	self.close_signal.emit()
    	self.close()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()

    pca=pcawindow()
    ex.btn.clicked.connect(pca.start)
    ex.close_signal.connect(ex.close)
    ex.show()

    nma=nmawindow()
    ex.btn1.clicked.connect(nma.start)
    ex.close_signal.connect(ex.close)
    ex.show()

    cmp=cmpwindow()
    ex.btn2.clicked.connect(cmp.start)
    ex.close_signal.connect(ex.close)
    ex.show()

    cmpt=cmptwindow()
    ex.btn3.clicked.connect(cmpt.start)
    ex.close_signal.connect(ex.close)
    ex.show()


    down=downloadwindow()
    ex.btn0.clicked.connect(down.start)
    ex.close_signal.connect(ex.close)
    sys.exit(app.exec_())

