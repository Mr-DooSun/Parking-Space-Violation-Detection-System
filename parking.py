from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import cv2
import check_number

import tkinter as tk
# import RPi.GPIO as GPIO
from time import sleep

try:
	import Image
except ImportError:
	from PIL import Image

import pytesseract
import threading
import database

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		root = tk.Tk()
		width = root.winfo_screenwidth()
		height = root.winfo_screenheight()
		MainWindow.setObjectName("MainWindow")
		#MainWindow.showFullScreen()
		MainWindow.resize(1200,800)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.picture = QtWidgets.QLabel(self.centralwidget)
		self.picture.setGeometry(QtCore.QRect(100, 250, 400, 300))
		self.picture.setObjectName("picture")
		
		self.disabled_car = QtWidgets.QLabel(self.centralwidget)
		self.disabled_car.setGeometry(QtCore.QRect(600,400, 1500, 100))
		self.disabled_car.setObjectName("disabled_car")
		self.disabled_car.setFont(QtGui.QFont("맑은 고딕",25))

		self.disabled_or_public = QtWidgets.QLabel(self.centralwidget)
		self.disabled_or_public.setGeometry(QtCore.QRect(600,500, 1500, 100))
		self.disabled_or_public.setObjectName("disabled_or_public")
		self.disabled_or_public.setFont(QtGui.QFont("맑은 고딕",40))

		self.detecting_number = QtWidgets.QLabel(self.centralwidget)
		self.detecting_number.setGeometry(QtCore.QRect(600, 300, 1500, 100))
		self.detecting_number.setObjectName("detecting_number")
		self.detecting_number.setFont(QtGui.QFont("맑은 고딕",40))

		self.car_number = QtWidgets.QLabel(self.centralwidget)
		self.car_number.setGeometry(QtCore.QRect(600, 200, 1500, 100))
		self.car_number.setObjectName("car_number")
		self.car_number.setFont(QtGui.QFont("맑은 고딕",25))

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(width/2.5, height/3, 800, 21))
		self.menubar.setObjectName("menubar")

		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.detecting_number.setText(_translate("MainWindow", ""))
		self.disabled_car.setText("장애인 차량여부")
		self.car_number.setText("인식된 차량 번호")

	# def IR_Sensor(self, MainWindow):
	#     while True :
	#         GPIO.setwarnings(False)
	#         GPIO.setmode(GPIO.BCM)
	#         GPIO.setup(14,GPIO.IN)
	#         while True:
	#             if GPIO.input(14) :
	#                 Check()
	#             else :
	#                 self.label.setText(_translate("MainWindow", ""))
	#             sleep(0.5)

	def Check(self,MainWindow):
		while True:
			number=check_number.full_number()

			print(number)

			self.detecting_number.setText(number)
			self.picture.setPixmap(QPixmap('car.jpg'))
			who=database.main(number)
			self.disabled_or_public.setText(who)
			
	# def IR_Sensor_start(self,MainWindow):
	# 	thread=threading.Thread(target=self.IR_Sensor,args=(self,))
	# 	thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
	# 	thread.start()

	def Check_thread(self,MainWindow):
		thread=threading.Thread(target=self.Check,args=(self,))
		thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
		thread.start()




if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()

	ui.setupUi(MainWindow)
	# ui.IR_Sensor_starts(MainWindow)
	ui.Check_thread(MainWindow)

	MainWindow.show()

	sys.exit(app.exec_())