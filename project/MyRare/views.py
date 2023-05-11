from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
# from .forms import RegistrationUserForm
from .forms import SignUpForm

menu = ['Оценки', 'Редактировать']


def index_redirect(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('login')


@login_required
def profile_view(request):
    context = {
        'menu': menu,
    }
    return render(request, 'MyRare/profile.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user,
                                             third_name=form.cleaned_data.get('third_name'),
                                             phone_number=form.cleaned_data.get('phone_number'),
                                             birth_day=form.cleaned_data.get('birth_day'),
                                             group=form.cleaned_data.get('group'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        form = SignUpForm()
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



