from operator import imod
from review.sitemaps import ReviewSitemap
from product.sitemaps import ProductSitemap
from accounts.sitemaps import UserProfileSitemap

sitemaps = {
    'review': ReviewSitemap,
    'product': ProductSitemap,
    'user': UserProfileSitemap,
}