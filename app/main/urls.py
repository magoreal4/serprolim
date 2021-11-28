from django.urls import path
from main import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.contrib.sitemaps.views import sitemap
# from main.sitemap import PostSitemap

# sitemaps={
#     'posts':PostSitemap
# }

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    # path('sitemap.xml',sitemap,{'sitemaps':sitemaps}, name='django.contrib.sitemap.views.sitemaps')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()