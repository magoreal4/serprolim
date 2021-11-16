from django.contrib import admin
from django.utils.html import format_html
from blog import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'publish', 'imagen', 'date_added' )
    prepopulated_fields = {'slug':('title',),}
    list_editable = ('subtitle', 'publish')
    def imagen(self, obj):
        return format_html("<img src={} width='130' height='100'/>", obj.img.url)

@admin.register(models.Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imgurl', 'thumbnail')
    list_editable = ('name',)
    def thumbnail(self, obj):
        return format_html("<img src={} width='130' height='100'/>", obj.img.url)
    def imgurl(self, obj):
        url =  format_html("{}", obj.img.url)
        domain = 'https://limpiezapozossepticos'
        return domain + url
    
@admin.register(models.Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'display', 'name', 'imgurl', 'thumbnail')
    list_editable = ('name','display')
    def thumbnail(self, obj):
        return format_html("<img src={} width='130' height='100'/>", obj.img.url)
    def imgurl(self, obj):
        return format_html("<h3> {} </h3>", obj.img.url)

    # list_display = ('post', 'name', 'email', 'publish', 'status')
    # list_filter = ('status', 'publish')
    # search_fields = ('name', 'email', 'content')

# admin.site.register(Like)