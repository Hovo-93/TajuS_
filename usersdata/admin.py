from django.contrib import admin

# Register your models here.
from django.contrib import admin

from usersdata.models import User, Passport, MigrationCard, WorkPermit
from jet.admin import CompactInline


class PassportModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'serial', 'nationality', 'date_of_issue',
                    'passport_expiration_date', 'img_preview')


class MigrationCardModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'serial', 'number', 'citizenship', 'duration_of_stay_from',
                    'duration_of_stay_to', 'card_preview')


class WorkPermitModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'serial', 'number', 'date_of_issue',
                    'patent_preview')


class PassportInline(CompactInline):
    model = Passport
    extra = 0


class MigrationCardInline(CompactInline):
    model = MigrationCard
    extra = 0


class WorkPermitInline(CompactInline):
    model = WorkPermit
    extra = 0


class UserModelAdmin(admin.ModelAdmin):
    def has_passport(self, obj):
        return obj.passport.exists()

    has_passport.boolean = True
    has_passport.short_description = 'Passport'
    list_display = ('username', 'first_name', 'last_name', 'patronymic', 'birthday',
                    'email', 'avatar_preview', 'role', 'has_passport')
    inlines = [PassportInline, MigrationCardInline, WorkPermitInline, ]


admin.site.register(User, UserModelAdmin)
admin.site.register(Passport, PassportModelAdmin)
admin.site.register(MigrationCard, MigrationCardModelAdmin)
admin.site.register(WorkPermit, WorkPermitModelAdmin)
