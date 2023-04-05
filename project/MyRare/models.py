from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=16)
    second_name = models.CharField(max_length=16)
    third_name = models.CharField(max_length=16, null=True, blank=True)
    course = models.IntegerField()
    group = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        if self.third_name is None:
            return f'{self.second_name} {self.name}'
        return f'{self.second_name} {self.name[0]}. {self.third_name[0]}.'


class Account(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=24)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.student.second_name} {self.student.name[0]}. {self.student.third_name[0]}.'


class RecordBook(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    rare = models.ForeignKey("Rare", on_delete=models.CASCADE)


class Rare(models.Model):
    type_rare = [
        (True, 'Зачет'),
        (False, 'Экзамен'),
    ]
    teacher = models.CharField(max_length=32)
    rare = models.CharField(max_length=32)
    type = models.BooleanField(choices=type_rare)
    discipline = models.OneToOneField('Discipline', on_delete=models.CASCADE)


class Discipline(models.Model):
    discipline = models.CharField(max_length=32)
    number_of_hours = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField()

    def __str__(self):
        return f'{self.discipline}'
