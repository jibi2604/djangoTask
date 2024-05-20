from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def view_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        print(user_profile.skills)
        print(user_profile.contact_details)
    except UserProfile.DoesNotExist:
        user_profile = None
    return render(request, 'users/viewProfile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/editProfile.html', {'form': form})
