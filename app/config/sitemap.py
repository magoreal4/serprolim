from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.contrib.sites.models import Site
from django.urls import reverse

class Site:
    domain = 'limpiezapozossepticos.com'

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(PostSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        return Post.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date_added
    
    def location(self, obj):
        return '/blog/%s' % (obj.slug)
 
class StaticSitemap(Sitemap):
    changefreq = "monthly"
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
    priority = 1

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(MainSitemap, self).get_urls(site=site, **kwargs)


    def items(self):
      return [self]

