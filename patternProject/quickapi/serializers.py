# serializer선언 (데이터표현 관련 정의)

from dataclasses import field
from pyexpat import model
# from django.contrib.auth.models import User
from home.models import User , Lecture    # 내가 만든 모델 import하기
from rest_framework import serializers
from django.contrib.auth import authenticate


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Mata:
        model = User
        fields = ('name', 'id', 'pw')
        extra_kwargs = {"pw": {"write_only": True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["name"], None, validated_data["pw"]
        )
        return user


# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name")


# 로그인
class LoginUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    pw = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")



class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('lec_idx','subject','professor','student','class_time','learing_time','completion')
