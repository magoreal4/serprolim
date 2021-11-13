# https://www.youtube.com/watch?v=m3hhLE1KR5Q&t=772s
from django.db import models
from tinymce import HTMLField

class Post(models.Model):

    # options = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published')
    # )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    slug = models.SlugField()
    img = models.ImageField()
    excerpt = models.TextField()
    content = HTMLField()
    # content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
       
    class Meta:
        ordering = ['-date_added']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title

class Imagen(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True)    

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Comment_detail", kwargs={"pk": self.pk})

