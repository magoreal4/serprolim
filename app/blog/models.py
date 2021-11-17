# https://www.youtube.com/watch?v=m3hhLE1KR5Q&t=772s
from django.db import models
from tinymce import HTMLField
from django.contrib.sites.models import Site

class Post(models.Model):

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    img = models.ImageField()
    excerpt = HTMLField()
    content = HTMLField()
    publish = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    metaDescription = models.TextField(max_length=170, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-date_added']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title

class Imagen(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField()    

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return self.name

class Anuncio(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField()
    display = models.BooleanField(default=False)    

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    def __str__(self):
        return self.name

    # options = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published')
    # )