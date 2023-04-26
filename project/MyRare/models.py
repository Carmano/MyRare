from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    third_name = models.CharField(max_length=255, blank=True)
    birth_day = models.DateField(max_length=255, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RecordBook(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'Зачетная книжка {self.profile.user.username}'


@receiver(post_save, sender=Profile)
def create_record_book(sender, instance, created, **kwargs):
    if created:
        RecordBook.objects.create(profile=instance)


class Rare(models.Model):
    type_rare = [
        (0, "Не зачёт"),
        (1, 'Зачёт'),
        (2, "Плохо"),
        (3, "Удовлетворительно"),
        (4, "Хорошо"),
        (5, "Отлично")
    ]
    teacher = models.CharField(max_length=255)
    rare = models.IntegerField(choices=type_rare)
    discipline = models.OneToOneField('Discipline', on_delete=models.CASCADE)
    record_book = models.ForeignKey("RecordBook", on_delete=models.CASCADE)


class Discipline(models.Model):
    discipline = models.CharField(max_length=32)
    number_of_hours = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField()

    def __str__(self):
        return f'{self.discipline}'
