from django.contrib import admin
from django.urls import path, include

from .sitemap import PostSitemap, StaticSitemap, MainSitemap
from django.contrib.sitemaps.views import sitemap

# app_name = "main"

sitemaps = {
    'blog':PostSitemap,
    'static':StaticSitemap,
    'main': MainSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}, name='sitemap')
]

# from django.contrib.sitemaps.views import sitemap
# from blog.sitemaps import PostSitemap

# app_name = "main"




