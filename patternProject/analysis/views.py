from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def analysis(request):
    return HttpResponse("Hello, world. You're at the analysis.")
# 학습 일시정지 기록
@api_view(['POST'])
def pause():
    pass

# 학습 일시정지 해제 기록
@api_view(['POST'])
def redo():
    pass

# 학습 영상 넘기기 기록
@api_view(['POST'])
def fast_forward():
    pass

# 학습 영상 뒤로가기 기록
@api_view(['POST'])
def rewind():
    pass