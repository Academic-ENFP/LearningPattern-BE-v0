from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.

def subject(request):
    return HttpResponse("Hello, world. You're at the subject.")

# 강의 영상 선택 & 강의 페이지 이동
@api_view(['POST'])
def video_select():
    # 입력받은 강의정보로 lecture 필드 생성
    # 입력받은 강의 url 통해 lecture 페이지 이동
    pass

# 학습시작 기록
@api_view(['POST'])
def start():
    pass

# 학습종료 기록
@api_view(['POST'])
def finish():
    pass

#결과 페이지 이동

# 메모 중간저장
@api_view(['POST'])
def note_autosave():
    pass

# 마이페이지 강의 선택 (user view에 구현)
# 복습환경 이동




# ViewSet 사용
