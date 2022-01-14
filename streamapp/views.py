from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
from streamapp.camera import GreyVideoCamera
from streamapp.camera import BinaryVideoCamera
# Create your views here.


def index(request):
	return render(request, 'streamapp/home.html')

def grey_scale_page(request):
	return render(request, 'streamapp/grey.html')

def binary_scale_page(request):
	return render(request, 'streamapp/binary.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def grey_scale(request):
	return StreamingHttpResponse(gen(GreyVideoCamera()),
								 content_type='multipart/x-mixed-replace; boundary=frame')

def binary_scale(request):
	return StreamingHttpResponse(gen(BinaryVideoCamera()),
								 content_type='multipart/x-mixed-replace; boundary=frame')

