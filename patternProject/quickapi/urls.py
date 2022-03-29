# from django.urls import include, path
# from rest_framework import routers
# from patternProject.quickapi import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'lectures', views.LectureViewSet)

# # quickapi/urls.py에 API URLs연결

# # 자동 url라우팅 사용 api연결
# # + 검색가능한 api에 대한 로그인 url포함

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# # viewset을 사용함으로 router클래스에 viewset등록시 API에 대한 URL conf자동 생성

