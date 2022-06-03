from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
from accounts.models  import CustomUser as User
from product.models import Product
from reviewer.unique import unique_slug_generator

# Create your models here.

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    upvotes = models.ManyToManyField(User, default=None, blank=True, related_name='upvote')
    downvotes = models.ManyToManyField(User, default=None, blank=True, related_name='downvote')
    comments = models.ManyToManyField(User, default=None, blank=True, related_name='comments', unique=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.review

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.review)
        return super().save(*args, **kwargs)

    @property
    def num_upvotes(self):
        return self.upvotes.all().count()

    @property
    def num_downvotes(self):
        return self.downvotes.all().count()
    
    def get_absolute_url(self):
        return reverse('review_details', kwargs={'slug1': self.product.slug, 'slug': self.slug})


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_image")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
    slug = models.SlugField(unique=True)
    review_image = models.ImageField(upload_to='review-images/')

    def __str__(self):
        return self.slug

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.review.review)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('review_image', kwargs={'slug': self.slug})


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
    slug = models.SlugField(null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.comment)

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.comment)
        return super().save(*args, **kwargs)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reply")
    reply = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.reply)

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.reply)
        return super().save(*args, **kwargs)
        
