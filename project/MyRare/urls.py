from django.urls import path, include
from django.contrib import admin
from . import views
# from .views import Registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('user/registration/', views.registration, name='registration'),
    path('profile/', views.profile_view, name='profile'),
]
