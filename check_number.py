import cv2
import numpy
try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract
import subprocess
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time


def first_number(str1) :
	f_num = ""

	for i in range(0,len(str1)):

		try:
			int(str1[i])
			f_num+=str1[i]
			if len(f_num) >= 2 :
				break
		except ValueError :
			pass

	return f_num

def second_number(str1) :
	s_num = ""

	for i in range(0,len(str1)):
		if str1[i]==" ":
			s_num=""
		try :
			int(str1[i])
			s_num+=str1[i]
			if len(s_num) >= 4:
				break
			else:
				pass
		except ValueError :
			pass
	return s_num

def kor_word(str1) :
	word=""
	print(str1)

	for i in str1:
		try :
			i = i.encode('ascii')
		except :
			if(ord(i)>=44032 and ord(i)<=55203):
				word+=i

	return word

# def camera_detecting():
# 	camera = PiCamera()
# 	camera.resolution = (400,300)
# 	rawCapture = PiRGBArray(camera)

# 	camera.capture(rawCapture,format="bgr")
# 	image=rawCapture.array

# 	cv2.imwrite("car.jpg",image)


def full_number() :
	# camera_detecting()
	try :
		subprocess.call(["car_Plate.exe"])
		image = cv2.imread('.plate.jpg')
		str1 = pytesseract.image_to_string(image) # rgb 색감 숫자 인식
		kor_str1 = pytesseract.image_to_string(image,lang="kor") #rgb색감 그림 한국어 인식
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		str2 = pytesseract.image_to_string(gray) # gray 색감 숫자 인식
		kor_str2 = pytesseract.image_to_string(gray,lang="kor") #gray색감 그림 한국어 인식

		if len(str1) <= len(str2):
			number = str2
		else :
			number = str1

		if len(kor_str1) <= len(kor_str2):
			kor_number = kor_str2
		else : 
			kor_number = kor_str1

		n=""
		n+=first_number(number)
		n+=kor_word(kor_number)
		n+=" "
		n+=second_number(number)
	except :
		return "감지되는 차량없음"

	return n