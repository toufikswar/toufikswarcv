"""mycv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from maincv.views import home, contact

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("maincv.urls", namespace='cv')),
    path('contact/',contact),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain;charset=utf-8')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps} ,name='django.contrib.sitemaps.views.sitemap'),
    path('summernote/', include('django_summernote.urls')),
]



# static() serves the static files to the static_root from the static_url
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
