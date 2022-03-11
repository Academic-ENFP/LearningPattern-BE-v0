import fractions
import imp
from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading


@gzip.gzip_page
def chrom(request):
    # return HttpResponse("Hello, world. You're at the chrom index.")
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'chrom.html')


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
        
        # 프레임 크기출력
        # print('Frame w: ', int(image.get(cv2.CAP_PROP_FRAME_WIDTH)))
       
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            
        
        
def gen(camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음
    while True:
        frame = camera.get_frame()
        
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        

# 프레임단위로 출력할 수 있는지 
# 이미지를 폴더에 저장하기
