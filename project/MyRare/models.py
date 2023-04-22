from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    third_name = models.CharField(max_length=255, blank=True)
    birth_day = models.DateField(max_length=255, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to='image/', blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RecordBook(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    rare = models.ForeignKey("Rare", on_delete=models.CASCADE)


class Rare(models.Model):
    type_rare = [
        ('Зачёт', 'Зачёт'),
        ("Не зачёт", "Не зачёт"),
        ("Плохо" "Плохо"),
        ("Удовл", "Удовлетворительно"),
        ("Хорошо", "Хорошо"),
        ("Отлично", "Отлично")
    ]
    teacher = models.CharField(max_length=255)
    rare = models.CharField(choices=type_rare)
    discipline = models.OneToOneField('Discipline', on_delete=models.CASCADE)


class Discipline(models.Model):
    discipline = models.CharField(max_length=32)
    number_of_hours = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField()

    def __str__(self):
        return f'{self.discipline}'
