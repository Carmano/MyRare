from django.contrib import admin
from .models import Student, Account, RecordBook, Rare, Discipline
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'second_name', 'third_name', 'course', 'group']


class AccountAdmin(admin.ModelAdmin):
    search_fields = ['login', 'password', 'student']


class RecordBookAdmin(admin.ModelAdmin):
    search_fields = ['student']


class RareAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'rare', 'type', 'teacher']


class DisciplineAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'number_of_hours', 'semester']


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(RecordBook, RecordBookAdmin)
admin.site.register(Rare, RareAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Student, StudentAdmin)
