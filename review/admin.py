from django.contrib import admin
from . models import Comment, Review, Vote

# Register your models here.
admin.site.register(Review)
admin.site.register(Vote)
admin.site.register(Comment)