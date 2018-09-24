from django.contrib import admin
from django.contrib.auth import get_user_model 

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
from account.forms import UserAdminChangeForm, RegisterForm

User = get_user_model()


# Todo Deactivate acction
def user_action(modeladmin, request, queryset):
    for user in queryset:
        user.active = False
        user.save()

user_action.short_description = 'Deactivate selected users'


# Todo custom view
class UserAdmin(BaseUserAdmin):
    # The froms to add and change user instances
    form = UserAdminChangeForm # update view

    # add_form = UserAdminCreationForm # create view
    add_form = RegisterForm

    # The fields to be userd in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on aut.Users
    list_display = ('email', 'admin', 'created')
    list_filter = ('admin', 'active')
    list_per_page = 25
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal Info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    actions = [user_action]


admin.site.register(User, UserAdmin)
# To remove Group Model from admin
admin.site.unregister(Group)
