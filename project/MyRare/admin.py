from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['login', 'password', 'name', 'second_name', 'third_name', 'cours', 'group']


admin.site.register(Student, StudentAdmin)
