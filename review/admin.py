from django.contrib import admin
from . models import Comment, Reply, Review, ReviewImage, Vote

# Register your models here

admin.site.register(Review)
admin.site.register(ReviewImage)
admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(Reply)