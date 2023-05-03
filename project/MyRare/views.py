from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationUserForm


menu = ['Оценки', 'Редактировать']


def index(request):
    return render(request, 'MyRare/index.html')


@login_required
def profile_view(request):
    context = {
        'menu': menu,
    }
    return render(request, 'MyRare/profile.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationUserForm()
        return render(request, 'registration/register.html', {'form': form})


# class Registration(View):
#     template_name = 'registration/register.html'
#
#     def get(self, request):
#         context = {
#             'form': UserCreationForm()
#         }
#         return render(request, self.template_name, context=context)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('login')
#         return render(request, self.template_name, context={'form': form})



