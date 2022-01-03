from django import dispatch
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)
    upvotes = models.ManyToManyField(User, default=None, blank=True, related_name='upvote')
    downvotes = models.ManyToManyField(User, default=None, blank=True, related_name='downvote')
    
    def __str__(self):
        return self.review

    @property
    def num_upvotes(self):
        return self.upvotes.all().count()

    @property
    def num_downvotes(self):
        return self.downvotes.all().count()
    

VOTE_CHOICES = {
    ('Upvote', 'Upvote'),
    ('Downvote', 'Downvote')
}

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    value = models.CharField(choices=VOTE_CHOICES, max_length=10)
    
    def __str__(self):
        return str(self.review) 
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile_pic.png", null=True, blank=True)
    followers = models.ManyToManyField(User, default=None, related_name="followers")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # create user profile after user has been created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    # save user profile
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return (self.user.username + " Profile")
    