from django import forms


class RegistrationStudentForm(forms.Form):
    name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    third_name = forms.CharField(label='Отчество')
    course = forms.IntegerField(label='Курс')
    group = forms.CharField(label='Группа')
