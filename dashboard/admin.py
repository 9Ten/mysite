from django.contrib import admin

# Register your models here.
from .models import UserProfile


def accept_action(modeladmin, request, queryset):
    for user in queryset:
        user.accept = True
        user.save()

def unaccept_action(modeladmin, request, queryset):
    for user in queryset:
        user.accept = False
        user.save()

accept_action.short_description = 'Accept selected users'
unaccept_action.short_description = 'Unaccept selected users'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'accept', 'abstarct_file', 'paypal_trans_id', 'country', 'update')
    list_filter = ['accept', 'user_type']
    search_fields = ['user__email', 'paypal_trans_id', 'country']
    list_display_links = ['user', 'abstarct_file']
    list_per_page = 25
    ordering = ['accept']

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'title', 'first_name', 'mid_name', 'last_name', 'country',  'unit', 'department', 'degree', 'institution_country', 'address', 'phone_number',)
        }),
        ('Abstarct', {
            'fields': (
                'abstarct_file', 
                'uploaded_at', 
                'accept'
            )
        }),
        ('Payment', {
            'fields': (
                'paypal_trans_id', 
                'user_status', 
                'user_type', 
                'update',
                'timestamp'
            )
        }),
    )
    readonly_fields = ('user', 'title', 'first_name', 'last_name', 'mid_name', 'country', 'unit', 'department', 'degree', 'institution_country', 'address', 'phone_number', 'abstarct_file', 'uploaded_at', 'paypal_trans_id', 'user_status', 'user_type', 'update','timestamp',)
    actions = [accept_action, unaccept_action]

    class Meta:
        model = UserProfile

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ['user', 'title', 'first_name', 'last_name', 'mid_name', 'country', 'unit', 'department', 'degree', 'institution_country', 'address', 'phone_number', 'abstarct_file', 'uploaded_at', 'paypal_trans_id', 'user_status', 'user_type', 'update','timestamp']
    #     else:
    #         return ['update','timestamp']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.disable_action('delete_selected')
