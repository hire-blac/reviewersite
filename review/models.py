from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
from accounts.models  import CustomUser as User
from product.models import Product

# Create your models here.

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)
    slug = models.SlugField(max_length=30, null=True, unique=True)
    upvotes = models.ManyToManyField(User, default=None, blank=True, related_name='upvote')
    downvotes = models.ManyToManyField(User, default=None, blank=True, related_name='downvote')
    comments = models.ManyToManyField(User, default=None, blank=True, related_name='comments', unique=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.review

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.review)
        return super().save(*args, **kwargs)

    @property
    def num_upvotes(self):
        return self.upvotes.all().count()

    @property
    def num_downvotes(self):
        return self.downvotes.all().count()
    
    def get_absolute_url(self):
        return reverse('review_details', kwargs={'slug': self.slug})

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


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comment", null=True)
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.comment) 
