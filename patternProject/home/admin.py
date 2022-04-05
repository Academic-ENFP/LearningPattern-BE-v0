import imp
from django.contrib import admin

# Register your models here.
from .models import User,Lecture

admin.site.register(User)
admin.site.register(Lecture)

