from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Student
from django.urls import reverse

def redirect_on_login(request):
    return redirect('authentication')


def index(request, id):
    student = get_object_or_404(Student, id=id)
    data = {
        'student': student
    }
    return render(request, 'MyRare/index.html', context=data)


@require_http_methods(['GET', 'POST'])
def authentication(request):
    if request.method == 'GET':
        return render(request, 'MyRare/login.html')

    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        data = {
            'login': login,
            'password': password,
        }
        error = validate(data)
        data['error'] = error
        students = Student.objects.all()
        if error:
            return render(request, 'MyRare/login.html', context=data)
        for student in students:
            if student.login == login and student.password == password:
                return redirect('index', student.id)
        data['error'] = 'Login or password is wrong'
        return render(request, 'MyRare/login.html', context=data)


def validate(data):
    for field in data:
        if field == 'error':
            continue
        if field is None:
            return "Login or password is wrong"


def edit(request):
    pass
