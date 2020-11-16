from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class sbs(admin.ModelAdmin):
    list_display = ['name','roll']