from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Lecture, Notes
from .serializers import SubjectSerializer, LectureSerializer, NotesSerializer
from .viewset import SubjectViewSet, LectureViewSet, NotesViewSet
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

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    

    # def list(self, request):
    #     subject = Subject.objects.all()
    #     serializer = SubjectSerializer(subject, many=True)
    #     return Response(serializer.data)


    # def create(self, request):
    #     serializer = SubjectViewSet(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def retrieve(self, request, pk=None):
    #     queryset = Subject.objects.all()
    #     subject = get_object_or_404(queryset, pk=pk)
    #     serializer = SubjectSerializer(subject)
    #     return Response(serializer.data)



class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer



# urlpatterns =[
#     path('blog/', blog_list),
#     path('blog/<int:pk>/', blog_detail),
# ]