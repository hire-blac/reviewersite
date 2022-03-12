from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from . models import UserProfile

class UserProfileSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return UserProfile.objects.all()

    def lastmod(self, obj):
        return obj.date_created