from django.contrib.sitemaps import Sitemap
from review.models import  Review

# dynamic views sitemaps
class ReviewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Review.objects.all()

    def lastmod(self, obj):
        return obj.created