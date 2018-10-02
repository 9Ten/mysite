from dashboard.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from dashboard.forms import EditProfileForm, 

@login_required(login_url='/login/')
def dashboard_view(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_view.html', {'profile_user': user})


@login_required(login_url='/login/')
def dashboard_edit(request):
    user = get_object_or_404(UserProfile, user=request.user)
    # userprofile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'dashboard_edit.html', {'form': form})


@login_required(login_url='/login/')
def dashboard_status(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_status.html', {'profile_user': user})


@login_required(login_url='/login/')
def dashboard_abstract(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_abstract.html', {'profile_user': user})


@login_required(login_url='/login/')
def dashboard_payment(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UploadPaymentForm(
            request.POST, 
            request.FILES, 
            instance=user
        )
        if form.is_valid():
            form.save()
            return redirect('dashboard_status')
    else:
        form = UploadPaymentForm(instance=user)
    return render(request, 'dashboard_payment.html', {'form': form})
