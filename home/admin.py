from django.contrib import admin
from home.models import User
from django.contrib.admin import AdminSite
from django.http import HttpResponse

# Register your models here.
admin.site.register(User)
