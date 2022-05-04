from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

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