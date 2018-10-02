from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

# UserAdminCreationForm
class RegisterForm(forms.ModelForm):
    """ 
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)
        return password1

    def clean_password2(self):
        # cheack that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(
                "This email address is already in use. Please supply a different email address.")
        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False # Send confirmation email
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """ 
    A form for updateing users. Includes all the fields on the user, but replaces the password field with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'admin',)

    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the field does not habe access to the inital value"""
        return self.initial["password"]
        

class PasswordResetForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean_password2(self):
        # cheack that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            return email
        else:
            raise forms.ValidationError(
                "This email is not exist. Please input email again")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(PasswordResetForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


