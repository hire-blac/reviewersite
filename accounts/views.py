from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import EditProfileForm

from accounts.models import CustomUser, UserFollowing, UserProfile


# Create your views here.

# view profile page
@login_required(login_url='/accounts/login/')
def my_profile(response):
    user = response.user
    my_profile = user.userprofile
    reviews = user.review.all()
    following = user.following.all()
    followers = user.follower.all()

    context = {
        'title':'My Profile',
        'profile':my_profile,
        'reviews': reviews,
        'following': following,
        'followers': followers
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
def follow(response, id):
    user = response.user
    following_user = CustomUser.objects.get(id=id)
    UserFollowing.objects.create(user=user, following_user=following_user)
    return redirect('/')

@login_required(login_url='/accounts/login/')
def unfollow(response, id):
    user = response.user
    following_user = CustomUser.objects.get(id=id)
    UserFollowing.objects.filter(user=user, following_user=following_user).delete()
    return redirect('/')


def user_profile(response, id):
    if id == response.user.id:
        return redirect(my_profile)

    profile = UserProfile.objects.get(id=id)
    reviews = profile.user.review.all()
    following = profile.user.following.all()
    followers = profile.user.follower.all()
    is_follower = False

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
        'is_follower': is_follower
    }

    return render(response, 'account/userprofile.html', context)