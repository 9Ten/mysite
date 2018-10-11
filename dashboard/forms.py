from django import forms
from dashboard.models import UserProfile

from django.utils import timezone
import pytz

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

            'presentation_type',
            'shirt_size',
            'dietary_restriction',
            'dietary_other',
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

            'presentation_type',
            'shirt_size',
            'dietary_restriction',
            'dietary_other',
        )


class UploadPaymentBankForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'slip_pic',
        )
        fields_required = ('slip_pic',)

    def save(self, commit=True):
        user = super(UploadPaymentBankForm, self).save(commit=False)
        user.payment_uploaded = timezone.now()
        user.payment_status = True
        user.user_status = 'ready'
        if commit:
            user.save()
        return user


class UploadPaymentPaypalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'paypal_trans_id',
        )
        fields_required = ('paypal_trans_id',)

    def save(self, commit=True):
        user = super(UploadPaymentPaypalForm, self).save(commit=False)
        user.payment_uploaded = timezone.now()
        user.payment_status = True
        user.user_status = 'ready'
        if commit:
            user.save()
        return user


class UploadAbstractForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'abstarct_file',
        )
        fields_required = ('abstarct_file',)

    def save(self, commit=True):
        user = super(UploadAbstractForm, self).save(commit=False)
        user.abstarct_file_uploaded = timezone.now()
        user.abstarct_file_status = True
        user.user_status = 'pending'
        if commit:
            user.save()
        return user
