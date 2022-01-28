from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import EditProfileForm

from accounts.models import UserProfile


# Create your views here.

# view profile page
@login_required(login_url='/login/')
def user_profile(response):
    my_profile = response.user.userprofile
    reviews = response.user.review.all()
    context = {
        'title':'My Profile',
        'profile':my_profile,
        'reviews': reviews
        }

    return render(response, 'account/myprofile.html', context )

@login_required(login_url='/login/')
def edit_profile(response):

    profile = response.user.userprofile
    form = EditProfileForm(instance=profile)

    if response.method == 'POST':
        form = EditProfileForm(response.POST, response.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')
            
    form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'title':'Edit my profile',
        'profile':profile,
        }
        
    return render(response, 'account/edit-profile.html', context)