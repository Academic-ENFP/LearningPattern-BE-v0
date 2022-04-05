from django.shortcuts import render
from home.models import User,Lecture
from rest_framework import generics, viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.models import AuthToken
from quickapi.serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer, LectureSerializer


@api_view(["GET"])
def HelloAPI(request):
    return Response("hello world!")


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["name"]) < 6 or len(request.data["pw"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# class UserViewSet(viewsets.ModelViewSet):
#     # 사용자를 보거난 편집할 수 있는 API endpoint
#     queryset = User.objects.all().order_by()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
    

# class LectureViewSet(viewsets.ModelViewSet):
#     queryset = Lecture.objects.all().order_by()
#     serializer_class = LectureSerializer
#     permission_classes = [permissions.IsAuthenticated]
