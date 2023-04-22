from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.redirect_on_login, name='redirect_on_login'),
    path('admin/', admin.site.urls),
]
