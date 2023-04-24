from django.contrib import admin
from .models import Profile, RecordBook, Discipline, Rare


class ProfileAdmin(admin.ModelAdmin):
    search_field = ['user', 'third_name', 'birth_day', 'group', 'img']


class RecordBookAdmin(admin.ModelAdmin):
    search_fields = ['profile', 'rare']


class DisciplineAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'number_of_hours', 'semester']


class RareAdmin(admin.ModelAdmin):
    search_fields = ['discipline', 'rare', 'teacher']


admin.site.register(Rare, RareAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(RecordBook, RecordBookAdmin)
admin.site.register(Discipline, DisciplineAdmin)
