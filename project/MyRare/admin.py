from django.contrib import admin
from .models import Profile, RecordBook, Discipline, Rare


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user', 'third_name', 'birth_day', 'group', 'img']


@admin.register(RecordBook)
class RecordBookAdmin(admin.ModelAdmin):
    search_fields = ['profile', 'rare']


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'number_of_hours', 'semester']


@admin.register(Rare)
class RareAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'rare', 'teacher']



