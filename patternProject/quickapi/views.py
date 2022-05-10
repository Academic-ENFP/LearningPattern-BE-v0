from django.shortcuts import render
from home.models import User
# from patternProject.quickapi import serializers
from quickapi.serializers import UserSerializer
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 로그인
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signin(request):
#     if request.method == "POST":
#         serializers = UserSerializer
