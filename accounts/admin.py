from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # при желании можно добавить поля отображения:
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('middle_name', 'phone_number', 'bio')}),
    )
