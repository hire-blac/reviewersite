"""ReviewerNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import views
from sitemaps import sitemaps

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # apps urls
    path('', include('reviewer.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('accounts.urls')),
    path('review/', include('review.urls')),
    path('product/', include('product.urls')),
    
    # dynamic sitemap generator urls
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    # admin urls
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

# if settings.LOCAL_SERVE_STATIC_FILES:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.LOCAL_SERVE_MEDIA_FILES:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
