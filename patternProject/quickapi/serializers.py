# serializer선언 (데이터표현 관련 정의)

from dataclasses import field
from pyexpat import model
# from django.contrib.auth.models import User
from home.models import User , Lecture    # 내가 만든 모델 import하기
from rest_framework import serializers

# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'id', 'pw')

class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('lec_idx','subject','professor','student','class_time','learing_time','completion')
