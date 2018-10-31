from django.contrib import admin

# Register your models here.
from dashboard.models import UserProfile
from django.core.mail import send_mail
from django.conf import settings


def accept_action(modeladmin, request, queryset):
    send_list = []
    for user in queryset:
        if user.user_status == 'pending':
            user.user_status = 'accepted'
            user.save()
            send_list.append(str(user))

    # check_url = 'http://{}/dashboard/payment/'.format(settings.ALLOWED_HOSTS[0])
    # send_mail(
    #     'ASA2018-Accept-Conference',
    #     'The 5th Asian Society of Arachnology Conference \n Thank You! Please check your payment for join us. {}'.format(check_url),
    #     settings.DEFAULT_FROM_EMAIL,
    #     send_list,
    # )


def unaccept_action(modeladmin, request, queryset):
    for user in queryset:
        if user.user_status == 'accepted':
            user.user_status = 'pending'
            user.save()


# def decline_action(modeladmin, request, queryset):
#     send_list = []
#     for user in queryset:
#         if user.user_status == 'pending':
#             user.user_status = 'decline'
#             user.save()
#             send_list.append(str(user))

#     check_url = 'http://{}/dashboard/abstract/'.format(settings.ALLOWED_HOSTS[0])
#     send_mail(
#         'ASA2018-Accept-Conference',
#         'The 5th Asian Society of Arachnology Conference \n Sorry! Please check your abstract. {}'.format(check_url),
#         settings.DEFAULT_FROM_EMAIL,
#         send_list,
#     )

accept_action.short_description = 'Accept selected users'
unaccept_action.short_description = 'Unaccept selected users'
# decline_action.short_description = 'Decline selected users'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'user_type', 'registration_type', 'presentation_type', 'user_status', 
        'abstarct_file_status', 'abstarct_file', 'payment_status', 'slip_pic', 'paypal_trans_id', 
        'update', 'shirt_size', 'dietary_restriction', 'dietary_other',
    )
    list_filter = [
        'user_type',
        'user_status', 
        'abstarct_file_status',
        'payment_status',

        'registration_type',
        'presentation_type',
        'shirt_size',
        'dietary_restriction',
    ]
    search_fields = ['user__email', 'paypal_trans_id']
    list_display_links = ['user', 'abstarct_file', 'slip_pic']
    list_per_page = 25
    ordering = ['update']

    fieldsets = (
        ('Profile', {
            'classes': ('collapse',),
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
                'slip_pic',
                'paypal_trans_id', 
                'payment_uploaded',
                'payment_status',
            )
        }),
        ('Approvement', {
            'fields': (
                'user_type', 
                'registration_type',
                'presentation_type',
                'shirt_size',
                'dietary_restriction',
                'dietary_other',

                'user_status', 
                'update',
                'timestamp',
            )
        })
    )
    readonly_fields = (
        'user', 'title', 'first_name', 'mid_name', 'last_name', 
        'country', 'unit', 'department', 'degree', 
        'institution_country', 'phone_number', 'address', 
        'abstarct_file', 'abstarct_file_uploaded', 
        'slip_pic', 'paypal_trans_id', 'payment_uploaded',
        'user_type', 'update','timestamp', 'registration_type', 'presentation_type', 'shirt_size', 'dietary_restriction', 'dietary_other',
    )
    actions = [accept_action, unaccept_action,]

    class Meta:
        model = UserProfile

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.disable_action('delete_selected')
