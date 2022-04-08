from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    # path('signin/', signin),
    path('api-auth/', include('rest_framework.urls')),
]
