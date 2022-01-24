from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields here

    def __str__(self):
        return self.email

    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(default="random", max_length=200, null=True)
    last_name = models.CharField(default="person", max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile_pic.png", null=True, blank=True)
    followers = models.ManyToManyField(CustomUser, default=None, related_name="followers")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # create user profile after user has been created
    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    # save user profile
    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return (self.user.username)
    