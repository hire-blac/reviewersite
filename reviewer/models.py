from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="review", null=True)
    product = models.CharField(max_length=200)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.product
	