from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.contrib.sites.models import Site
from django.urls import reverse

class Site:
    domain = 'limpiezapozossepticos.com'

class Siteblog:
    domain = 'limpiezapozossepticos.com/blog/'

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
 
    def get_urls(self, site=None, **kwargs):
        site = Siteblog()
        return super(PostSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        return Post.objects.filter(publish=True)
    
    def location(self, obj):
        return obj.pk
 
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(StaticSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['blog']

    def location(self, item):
        return reverse(item)

class MainSitemap(Sitemap):
    location = "/"
    changefreq = "monthly"
    priority = "1"

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(MainSitemap, self).get_urls(site=site, **kwargs)


    def items(self):
      return [self]

