from django.db import models


class Student(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=24)
    name = models.CharField(max_length=16)
    second_name = models.CharField(max_length=16)
    third_name = models.CharField(max_length=16)
    course = models.IntegerField()
    group = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.second_name} {self.name} {self.third_name}'


class RecordBook(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


class Rare(models.Model):
    teacher = models.CharField(max_length=32)
    rare = models.CharField(max_length=32)
    type = models.BooleanField(max_length=32)


class Discipline(models.Model):
    discipline = models.CharField(max_length=32)
    number_of_hours = models.IntegerField()
    semester = models.IntegerField()
    id_rare = models.OneToOneField(Rare, on_delete=models.CASCADE)
