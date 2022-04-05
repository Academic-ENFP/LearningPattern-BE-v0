import fractions
import imp
from turtle import delay
import cv2, threading, os
from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
from numpy import save


# @gzip.gzip_page
def chrom(request):
    return render(request, 'chrom/chrom.html')

# 강의명 받아오기
def classroom(request, subject):
    return render(request, 'chrom/classroom.html',{
        'subject' : subject
    })


# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)    # 윈도우 디폴트 카메라 사용
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            self.video.release()
            cv2.destroyAllWindows()

    
def gen(camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음       
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        
@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    
