from dataclasses import field
from pyexpat import model
from home.models import User , Lecture    # 내가 만든 모델 import하기
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model, authenticate


class LectureInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        field = '__all__'