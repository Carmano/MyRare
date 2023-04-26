from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User


menu = ['Оценки', 'Редактировать']


def index(request):
    return render(request, 'MyRare/index.html')

