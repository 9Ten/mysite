from dashboard.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from dashboard.forms import *
from django.core.mail import send_mail
from django.conf import settings

@login_required(login_url='/login/')
def dashboard_view(request):
    queryset = UserProfile.objects.values(
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
        'update',
    )
    user = get_object_or_404(queryset, user=request.user)
    return render(
        request, 'dashboard_view.html', 
        {'profile_user': user}
    )


@login_required(login_url='/login/')
def dashboard_edit(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')
    else:
        form = EditProfileForm(instance=user)
    return render(
        request, 'dashboard_edit.html', 
        {'form': form}
    )


@login_required(login_url='/login/')
def dashboard_status(request):
    queryset = UserProfile.objects.values(
        'user_status',
        'abstarct_file_status',
        'payment_status'
    )
    user = get_object_or_404(queryset, user=request.user)
    return render(
        request, 'dashboard_status.html', 
        {'status_user': user}
    )


@login_required(login_url='/login/')
def dashboard_abstract(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UploadAbstractForm(
            request.POST,
            request.FILES,
            instance=user
        )
        if form.is_valid():
            form.save()
            check_url = 'http://{}/myadmin/dashboard/userprofile/'.format(settings.ALLOWED_HOSTS[0])
            send_mail(
                'ASA2018-Abstract-{}'.format(str(user)),
                'Please check upload {}'.format(check_url),
                settings.DEFAULT_FROM_EMAIL,
                ['ArachnologyConference@gmail.com',],
            )
            return redirect('dashboard_abstract')
    else:
        form = UploadAbstractForm(instance=user)
    return render(
        request, 'dashboard_abstract.html',
        {'form': form}
    )


@login_required(login_url='/login/')
def dashboard_payment(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        if request.FILES:
            bank_form = UploadPaymentBankForm(
                request.POST,
                request.FILES, 
                instance=user
            )
            if bank_form.is_valid():
                bank_form.save()
                check_url = 'http://{}/myadmin/dashboard/userprofile/'.format(settings.ALLOWED_HOSTS[0])
                send_mail(
                    'ASA2018-Payment-{}'.format(str(user)),
                    'Please check upload {}'.format(check_url),
                    settings.DEFAULT_FROM_EMAIL,
                    ['ArachnologyConference@gmail.com',],
                )
                return redirect('dashboard_payment')
        else:
            paypal_form = UploadPaymentPaypalForm(
                request.POST,
                instance=user
            )
            if paypal_form.is_valid():
                paypal_form.save()
                check_url = 'http://{}/myadmin/dashboard/userprofile/'.format(settings.ALLOWED_HOSTS[0])
                send_mail(
                    'ASA2018-Payment-{}'.format(str(user)),
                    'Please check upload {}'.format(check_url),
                    settings.DEFAULT_FROM_EMAIL,
                    ['ArachnologyConference@gmail.com',],
                )
                return redirect('dashboard_payment')
    else:
        bank_form = UploadPaymentBankForm(instance=user)
        paypal_form = UploadPaymentPaypalForm(instance=user)
    return render(
        request, 'dashboard_payment.html', 
        {
            'bank_form': bank_form, 
            'paypal_form': paypal_form
        }
    )
