
from django.contrib import admin
from .models import MyUser
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.backends import ModelBackend

# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    def get_site_name(self, obj):
        return obj.site.name
    get_site_name.short_description = 'Site Name'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'password', )}),

        ('Permissions', {'fields': ('is_superuser',
                                    'is_staff', 'user_permissions')}),
        ('Other', {
            'fields': ('groups',)
        })

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    # def save_model(self, request, obj, form, change):
    #     if change is False:
    #         obj.site = get_current_site(request)
    #     return super(MyUserAdmin, self).save_model(request, obj, form, change)