import click as click
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import pyautogui
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings



# function for detecting left mouse click

class VideoCamera(object):

	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
		self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
		width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
		height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
		print(width, height)


	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()


class GreyVideoCamera(object):

	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
		self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
		width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
		height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		frame_flip = cv2.flip(gray, 1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

class BinaryVideoCamera(object):

	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
		self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
		width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
		height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		(thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
		frame_flip = cv2.flip(blackAndWhiteImage, 1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()