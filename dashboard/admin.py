from django.contrib import admin

# Register your models here.
from dashboard.models import UserProfile


# send email acception
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
    list_display = (
        'user', 'user_type', 'accept', 
        'abstarct_file', 'paypal_trans_id', 'country', 'update'
    )
    list_filter = [
        'accept', 
        'user_type',
        'user_status', 
        'abstarct_file_status',
        'payment_status'
    ]
    search_fields = ['user__email', 'paypal_trans_id', 'country']
    list_display_links = ['user', 'abstarct_file', 'slip_pic']
    list_per_page = 25
    ordering = ['update']

    fieldsets = (
        ('Profile', {
            'fields': (
                'user', 'title', 'first_name', 'mid_name', 'last_name', 
                'country',  'unit', 'department', 'degree', 
                'institution_country', 'phone_number', 'address',
            )
        }),
        ('Abstarct', {
            'fields': (
                'abstarct_file',
                'abstarct_file_uploaded', 
                'abstarct_file_status',
            )
        }),
        ('Payment', {
            'fields': (
                'slip_pic'
                'paypal_trans_id', 
                'paypal_uploaded',
                'payment_status',
            )
        }),
        ('Approvement', {
            'fields': (
                'user_type', 
                'user_status', 
                'update',
                'timestamp',
                'accept',
            )
        })
    )
    readonly_fields = (
        'user', 'title', 'first_name', 'mid_name', 'last_name', 
        'country', 'unit', 'department', 'degree', 
        'institution_country', 'phone_number', 'address', 
        'abstarct_file', 'abstarct_file_uploaded', 
        'slip_pic', 'paypal_trans_id', 'paypal_uploaded',
        'user_type', 'update','timestamp',
    )
    actions = [accept_action, unaccept_action]

    class Meta:
        model = UserProfile

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.disable_action('delete_selected')
