from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name='profile'),
]
