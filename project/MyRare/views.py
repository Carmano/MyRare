from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Student, Account
from .forms import RegistrationStudentForm


menu = ['Оценки', 'Редактировать']


def redirect_on_login(request):
    return redirect('authentication')


def index(request, id):
    student = get_object_or_404(Student, id=id)
    data = {
        'student': student,
        'menu': menu,
    }
    return render(request, 'MyRare/index.html', context=data)


def registration(request):
    form = RegistrationStudentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            student = Student(
                name=form.cleaned_data['name'],
                second_name=form.cleaned_data['second_name'],
                third_name=form.cleaned_data['third_name'],
                course=form.cleaned_data['course'],
                group=form.cleaned_data['group'],
            )
            student.save()
    if request.method == 'GET':
        return render(request, 'MyRare/registration.html', {'form': form})


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
        users = Account.objects.all()
        if error:
            return render(request, 'MyRare/login.html', context=data)
        for user in users:
            if user.login == login and user.password == password:
                return redirect('index', user.id)
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
