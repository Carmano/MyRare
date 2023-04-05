from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.redirect_on_login, name='redirect_on_login'),
    path('login/', views.authentication, name='authentication'),
    path('login/registration/', views.registration, name='registration'),
    path('admin/', admin.site.urls),
    path('<int:id>/', views.index, name='index'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('login/registration/', views.registration, name = 'registration'),
]
