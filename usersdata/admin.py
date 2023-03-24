from django.contrib import admin

# Register your models here.
from django.contrib import admin
from usersdata.models import User, Passports
from django.utils.html import format_html


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'patronymic', 'birthday',
                    'email', 'avatar', 'role','avatar_preview')


class PassportModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'serial', 'nationality', 'date_of_issue',
                    'passport_expiration_date', 'img_preview')


admin.site.register(User, UserModelAdmin)
admin.site.register(Passports, PassportModelAdmin)
