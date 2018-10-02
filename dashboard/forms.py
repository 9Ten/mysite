from django import forms
from dashboard.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'title',
            'first_name',
            'last_name',
            'institution',
            'unit',
            'department',
            'degree',
            'country',
            'phone_number',
            'address',
            'user_type',
        )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'title',
            'first_name',
            'last_name',
            'institution',
            'unit',
            'department',
            'degree',
            'country',
            'phone_number',
            'address',
            'user_type',
        )

class UploadPaymentBankingForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'slip_pic',
        )

class UploadPaymentPaypalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'paypal_trans_id',
        )

class UploadAbstractForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'abstarct_file',
        )

class StatusForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'user_status',
            'abstarct_file_status',
            'payment_status'
        )