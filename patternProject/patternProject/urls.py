"""patternProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
# from patternProject.quickapi import views
from quickapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lectures', views.LectureViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickapi/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('home.urls')),
    path('stamp/', include('timestamp.urls')),
    path('memo/', include('memo.urls')),
    path('chart/', include('chart.urls')),
    path('user/', include('userpage.urls')),
    path('chrom/', include('chrom.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
