from django import forms
from django.contrib.auth.forms import UserCreationForm
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
            'address',
            'phone_number',
            'abstarct_file',
            'user_type',
        )
