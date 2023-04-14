"""financial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from wagtail.contrib.sitemaps.views import sitemap

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls

from django.conf import settings
from django.conf.urls.static import static

#Wagtail website's API/headless CMS instructions
from wagtail.api.v2.router import WagtailAPIRouter
from .api import api_router

router = WagtailAPIRouter('wagtailapi')

urlpatterns = [
    # Default URLS
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    #Wagtail website's API/headless CMS instructions
    re_path(r'^api/v2/', api_router.urls),
    # Wagtail URLs
    path('wagtail-admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('images/', include(wagtailimages_urls)),
    path('sitemap.xml', sitemap),
    # Your custom app URLs
    path('loans/', include('loans.urls')),
    # Wagtail URLs should be placed last
    path('', include(wagtail_urls)),
    # ... any other URL patterns ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

