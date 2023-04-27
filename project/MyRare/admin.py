from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile, RecordBook, Discipline, Rare


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_email', 'group', 'get_username', 'birth_day', 'get_html_img')
    search_fields = ['user', 'third_name', 'birth_day', 'group', 'img']

    @admin.display(description='img')
    def get_html_img(self, obj):
        if obj.img:
            return mark_safe(f"<img src='{obj.img.url}' width=50>")

    @admin.display(description='username')
    def get_username(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.third_name}'

    @admin.display(description='email')
    def get_email(self, obj):
        return obj.user.email


@admin.register(RecordBook)
class RecordBookAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'profile', 'get_username',)
    search_fields = ['profile', 'rare']

    @admin.display(description='username')
    def get_username(self, obj):
        return f'{obj.profile.user.last_name} {obj.profile.user.first_name} {obj.profile.third_name}'


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id', 'discipline', 'number_of_hours', 'semester')
    search_fields = ['discipline', 'number_of_hours', 'semester']


@admin.register(Rare)
class RareAdmin(admin.ModelAdmin):
    list_display = ('id', 'discipline_id', 'get_discipline', 'rare', 'teacher', 'get_semester', 'get_course')
    search_fields = ['discipline', 'rare', 'teacher']

    @admin.display(description='discipline')
    def get_discipline(self, obj):
        return obj.discipline.discipline

    @admin.display(description='semester')
    def get_semester(self, obj):
        return obj.discipline.semester

    @admin.display(description='course')
    def get_course(self, obj):
        return (obj.discipline.semester % 2) + (obj.discipline.semester // 2)
