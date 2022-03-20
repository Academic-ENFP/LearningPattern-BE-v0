from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.chrom, name='chrom'),
    path('detectme/', views.detectme, name='detectme'),
]