from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from models import Mahasiswa
# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mahasiswa, MahasiswaAdmin)