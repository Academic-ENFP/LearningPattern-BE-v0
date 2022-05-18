from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('subject', views.SubjectViewSet, basename='subject')

urlpatterns = [
    # path('', views.subject, name='subject'),
]