from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from product.models import Product

class ProductSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Product.objects.all()