
from django.contrib import admin
from django.utils.html import format_html

from main.models import Banner, Cliente, Faq

class Background(admin.ModelAdmin):

    list_display = (
        'name',
        'display',
        'titulo_h1',
        'titulo_h2',
        'fondo',
        'img',
        
    )
    list_editable = ('titulo_h1', 'titulo_h2', 'display')
    list_display_link = ('name',)
    
    def fondo(self, obj):
        return format_html("<img src={} width='130' height='100'/>", obj.imagebg.url)
    
    def img(self, obj):
        if(obj.imagemain):
            return format_html("<img src={} width='130' height='100'/>", obj.imagemain.url)
        else:
            return format_html("<h2>Sin imagen</h2>")

admin.site.register(Banner, Background)
# admin.site.register(Cliente)
class Clientes(admin.ModelAdmin):

    list_display = (
        'id',
        'titulo',
        'resumen',        
        'display',
        'order',
        'img',
    )
    list_editable = ('titulo', 'resumen', 'display', 'order')
    list_display_link = ('id',)
    
    def img(self, obj):
        if(obj.imagen):
            return format_html("<img src={} width='130' height='100'/>", obj.imagen.url)
        else:
            return format_html("<h1>comentario</h1>")

admin.site.register(Cliente, Clientes)

admin.site.register(Faq)

