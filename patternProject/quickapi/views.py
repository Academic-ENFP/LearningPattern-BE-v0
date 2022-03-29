from django.shortcuts import render
from home.models import User,Lecture
from rest_framework import viewsets
from rest_framework import permissions
from quickapi.serializers import UserSerializer, LectureSerializer


class UserViewSet(viewsets.ModelViewSet):
    # 사용자를 보거난 편집할 수 있는 API endpoint
    queryset = User.objects.all().order_by()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all().order_by()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated]
