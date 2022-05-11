from django.urls import path

from patternProject.subject.models import Lecture
from .views import SubjectViewSet, LectureViewSet

subject_list = SubjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
    
subject_detail = SubjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})




# Lectuer
lecture_list = LectureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

lecture_detail = LectureViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns =[
    path('subject/', subject_list),
    path('subject/<int:pk>/', subject_detail),
    path('lecture/', lecture_list),
    path('lecture/<int:pk>/', lecture_detail),
    
]