from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    class UserRoles(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        USER = 'USER', _('User')

    patronymic = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(_('Birth date'), null=True)
    avatar = models.ImageField(_('Avatar'), upload_to='avatar/% Y/% m/% d/', null=True)
    email = models.EmailField(_('Email address'), blank=True)
    role = models.CharField(
        max_length=9, choices=UserRoles.choices, default=UserRoles.USER)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Passports(models.Model):
    class Gender(models.TextChoices):
        FEMALE = 'F', _('Female')
        MALE = 'M', _('Male')

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='passport')
    serial = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    nationality = models.CharField(max_length=30)
    date_of_issue = models.DateField(_('Date of Issue'))
    passport_expiration_date = models.DateField(_('Passport Expiration Date'))
    photo = models.ImageField(_('Passport Photo'), upload_to='passport/photo/% Y/% m/% d/', null=True)

    def img_preview(self):
        return mark_safe('<img src = "{url}" width = "200"/>'.format(
            url=self.photo.url
        ))
