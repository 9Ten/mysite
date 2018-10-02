# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

# Create your views here.
from account.models import User
from account.forms import RegisterForm, PasswordResetForm
from dashboard.forms import ProfileForm

# permission
from django.contrib.auth.decorators import login_required

# use User model
User = get_user_model()


def register(request):
    if request.method == 'POST':
        request_post = request.POST
        register = RegisterForm(request_post)
        usrprofile = ProfileForm(request_post)
        if register.is_valid() and usrprofile.is_valid():
            # Check exists email Error
            user = register.save()
            usrprofile = ProfileForm(
                request_post,
                instance=user.userprofile
            )
            usrprofile.save()
            password = register.cleaned_data.get('password1')
            user = authenticate(
                username=user,
                password=password
            )
            if user is not None:
                login(request, user)
            return redirect('index')
        else:
            userform = RegisterForm(request_post)
            userprofileform = ProfileForm(request_post)
            return render(
                request, 
                'register.html', 
                {
                    'userform': userform, 
                    'userprofileform': userprofileform
                }
            )
    else:
        # request.GET
        userform = RegisterForm()
        userprofileform = ProfileForm()
    return render(
        request, 
        'register.html', 
        {
            'userform': userform, 
            'userprofileform': userprofileform
        }
    )
