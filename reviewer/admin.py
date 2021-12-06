from django.contrib import admin
from .models import Profile, Review, Vote

# Register your models here.
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Vote)