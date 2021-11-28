from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def item(self):
        return Post.objects.filter(publish=True)
    # def lastmod(sefl,obj):
    #     return obj.updated