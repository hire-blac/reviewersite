from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=CASCADE, null=False)
    product = models.CharField(max_length=200, null=False)
    stars = models.IntegerField()
    review = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product