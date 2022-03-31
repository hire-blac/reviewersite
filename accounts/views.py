from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import EditProfileForm

from accounts.models import CustomUser, UserFollowing, UserProfile
from review.forms import NewComment

# Create your views here.

# view profile page
@login_required(login_url='/accounts/login/')
def my_profile(response):
    user = response.user
    my_profile = user.userprofile
    reviews = user.review.all().order_by('-created')
    following = user.following.all()
    followers = user.follower.all()
    comment_form = NewComment

    context = {
        'title':'My Profile',
        'profile':my_profile,
        'reviews': reviews,
        'following': following,
        'followers': followers,
        'comment_form': comment_form
        }

    return render(response, 'account/myprofile.html', context )

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def follow(response, slug):
    user = response.user
    following_user = UserProfile.objects.get(slug=slug).user
    UserFollowing.objects.create(user=user, following_user=following_user)
    
    return HttpResponseRedirect(following_user.userprofile.get_absolute_url())

@login_required(login_url='/accounts/login/')
def unfollow(response, slug):
    user = response.user
    following_user = UserProfile.objects.get(slug=slug).user
    UserFollowing.objects.filter(user=user, following_user=following_user).delete()
    
    return HttpResponseRedirect(following_user.userprofile.get_absolute_url())


def user_profile(response, slug):
    if not response.user.is_anonymous:
        if slug == response.user.userprofile.slug:
            return redirect(my_profile)

    profile = UserProfile.objects.get(slug=slug)
    reviews = profile.user.review.all().order_by('-created')
    following = profile.user.following.all()
    followers = profile.user.follower.all()
    is_follower = False
    comment_form = NewComment

    for follow in followers:
        if response.user == follow.user:
            is_follower = True
        break

    context = {
        'title': 'User Profile',
        'profile': profile,
        'reviews': reviews,
        'following': following,
        'followers': followers,
        'is_follower': is_follower,
        'comment_form': comment_form
    }

    return render(response, 'account/userprofile.html', context)