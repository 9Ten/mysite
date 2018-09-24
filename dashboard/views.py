from dashboard.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from dashboard.forms import EditProfileForm


@login_required(login_url='/login/')
def dashboard_view(request):
    # Attributes set by middleware
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_view.html', {'profile_user': user})


@login_required(login_url='/login/')
def dashboard_edit(request):
    userprofile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')
    else:
        form = EditProfileForm(instance=userprofile)
    return render(request, 'dashboard_edit.html', {'form': form})


@login_required(login_url='/login/')
def dashboard_status(request):
    # Attributes set by middleware
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_status.html', {'profile_user': user})

@login_required(login_url='/login/')
def dashboard_abstract(request):
    # Attributes set by middleware
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_abstract.html', {'profile_user': user})

@login_required(login_url='/login/')
def dashboard_payment(request):
    # Attributes set by middleware
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'dashboard_payment.html', {'profile_user': user})

